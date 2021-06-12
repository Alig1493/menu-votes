from _pytest.python_api import raises
from django.urls import reverse
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.tokens import RefreshToken


class TestToken:
    obtain_pair_url = reverse("api_v1:users:token_obtain_pair")
    obtain_refresh_url = reverse("api_v1:users:token_refresh")

    def validate_access_token(self, access_token, user):
        access_token_payload = token_backend.decode(access_token, True)
        assert access_token_payload.get("token_type", "") == "access"
        assert access_token_payload.get("user_id", "") == user.id

    def validate_refresh_token(self, refresh_token, user):
        refresh_token_payload = token_backend.decode(refresh_token, True)
        assert refresh_token_payload.get("token_type", "") == "refresh"
        assert refresh_token_payload.get("user_id", "") == user.id

    def test_token_obtain_pair(self, client, user, password):
        response = client.post(
            self.obtain_pair_url, {"username": user.username, "password": password}
        )
        assert response.status_code == 200
        access_token = response.data.get("access", "")
        refresh_token = response.data.get("refresh", "")
        self.validate_access_token(access_token, user)
        self.validate_refresh_token(refresh_token, user)

    def test_token_obtain_refresh(self, client, user):
        refresh_token = str(RefreshToken.for_user(user))
        response = client.post(self.obtain_refresh_url, {"refresh": refresh_token})
        assert response.status_code == 200
        access_token = response.json().get("access", "")
        new_refresh_token = response.json().get("refresh", "")
        self.validate_access_token(access_token, user)
        self.validate_refresh_token(new_refresh_token, user)

        with raises(TokenError) as token_error:
            RefreshToken(refresh_token).check_blacklist()
            assert token_error

    def test_inactive_user_token_obtain_pair(self, client, user, password):
        user.is_active = False
        user.save()
        response = client.post(
            self.obtain_pair_url, {"username": user.username, "password": password}
        )
        assert response.status_code == 401

    def test_token_obtain_pair_with_invalid_credentials(self, client, user):
        response = client.post(
            self.obtain_pair_url, {"username": user.username, "password": "invalid"}
        )
        assert response.status_code == 401
