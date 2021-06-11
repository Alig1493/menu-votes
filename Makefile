up-build:
	./scripts/check_postgres.sh
	docker-compose up --build -d
