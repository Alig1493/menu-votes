# Menu of the day

You ever have that office conundrum where you and your colleagues can't decide on a place to eat out?
No? Me neither, because God bless the pandemic and it's cheaper to eat in and I'm not exactly a spendthrift myself.
HOWEVER, in the off chance that you do face that problem, this application is for you. Upload your menus of
the day of your favourite restaurants and vote away. The highest votes gets selected to be the place of choice
for that day and after that, you can do it all over again, for as long as you want.

### Disclaimer:
- The first commit might have a bit too much work done on it simply based on the fact that I usually have 
a base structure that I use occasionally when building django projects.

- I usually keep env separate (maybe in a private repo or somewhere secure we can access the variables from)
as opposed to submitting them in the git repo like this, however it is being done so here for the sake of the project.

### User Registration:
- User registration here is a direct api call where the superuser submits the employee name and password.
Normally when registering an employee/user in an organization, an admin created the user entity in the 
system, and an email is sent with a unique link to the user confirming the user creation and asking the user to set 
a new password before using the system. I've bypassed all of that for the sake of testing and usability
for this prototype application.
- After the superuser creates the user with a username and password, the user can be logged in by requesting for 
a jwt token and using that to authenticate oneself as the organization's user where it is required to do so.