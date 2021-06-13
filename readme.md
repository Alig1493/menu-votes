# Menu of the day

You ever have that office conundrum where you and your colleagues can't decide on a place to eat out?
No? Me neither, because God bless the pandemic and it's cheaper to eat in and I'm not exactly a spendthrift myself.
HOWEVER, in the off chance that you do face that problem, this application is for you. Upload your menus of
the day of your favourite restaurants and vote away. The highest votes gets selected to be the place of choice
for that day and after that, you can do it all over again, for as long as you want.

### Disclaimer:
* The first commit might have a bit too much work done on it simply based on the fact that I usually have 
a base structure that I use occasionally when building django projects.

* I usually keep env separate (maybe in a private repo or somewhere secure we can access the variables from)
as opposed to submitting them in the git repo like this, however it is being done so here for the sake of the project.

### User Registration:
* User registration here is a direct api call where the superuser submits the employee name and password.
Normally when registering an employee/user in an organization, an admin created the user entity in the 
system, and an email is sent with a unique link to the user confirming the user creation and asking the user to set 
a new password before using the system. I've bypassed all of that for the sake of testing and usability
for this prototype application.
* After the superuser creates the user with a username and password, the user can be logged in by requesting for 
a jwt token and using that to authenticate oneself as the organization's user where it is required to do so.


### Voting constraints:
I've assumed some of the constraints that wasn't explicitly mentioned in the requirements such as:
* Users cannot vote for menus uploaded in the past
* Users can vote for different menus. So that's multiple votes on the same ay but for different menus only
* I'm retrieving a single object when asking for published vote results instead of a list.
* I'm putting an api to publish the results that any authenticated employee can access and publish since the superuser
might not be present at the organization and people will still be able to vote and decide.

### Getting Started:
* Clone the repository in to the directory and machine of choice.
* Note, that this is built on docker and docker-compose version 3 so make sure you have those 
necessary modules installed and running in your system.
* Start the application using: `make up-build`
* Run the tests using: `make test`
* Create a superuser to access admin panel using: `make createsuperuser` and follow the prompts.
* Go to: `http://0.0.0.0:8000` on your browser of choice to view the docs.
* Go to: `http://0.0.0.0:8000/admin` on your browser of choice to view the admin panel.