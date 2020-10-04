# monopoly-masters

### Team name
Monopoly Masters

### Team members
Pete Buwembo, Cindy Cheng, Christine Kao, Shih Chieh Lin and Aary Sheoran

### How to run the application instruction
#### Requirements
* Python 3.7
* pip 19.0.3
* Virtual Environment 16.4.0

#### Run application
TBD

#### Run script
TBD

#### Tests
Run pytest

### Application concept:
We are building a virtual version of the popular board game Monopoly, to be played by between 2 and 4 players through python. During the quarantine, this game is a fun but socially distanced way to socialize with friends. Using randomness generators and graphical interfaces within python, we can create a virtual simulation of the game that stays true to the original while being quicker and easier.

### Stakeholders
Players who are into classic board games. New players who are looking for digital board games to play and also spend time with their friends.  

### User stories 
1. **User welcome page** - priority 10 - 5 days
   - As a user, I can see a welcome page.  
2. **Set number of players** - priority 20 - 10 days
   - As a user, I can set the number of players.  
3. **Roll dice** - priority 20 - 5 days
   - As a user, I can roll the dice and move around the board. 
4. **Choose character token** - priority 40 - 5 days
   - As a user, I am able to pick character.  
5. **Banker selection** - priority 40 - 5 days
   - As a user, I am able to create bank. 

#### Decomposition of user stories 
##### 5 days - priority 10 
1. As a user, I can see a welcome page when I first logged on.  The welcome page allows me to sign in or register. 

##### 10 days, priority 20
2. As a user, after the game start I MUST be able to enter the number of players [between 2 and 4]. 
If I press Cancel, then I MUST be able to exit the game.

##### 5 days, priority 20
3. As a player, I must be allowed to roll the dice and move my characters around the board, clockwise.
Roll the dice to see who goes first. This highest roll begins the game 

##### 5 days, priority 40
4. As a user, I must be able to pick or choose a token to represent me on the board.

##### 5 days, priority 40
5. As a user, I must be able to create a bank and identify one player to be the banker. 

#### Milestone 1.0
#### Iteration # 1 [Task 1]

As a user, I can see a welcome page when I first logged on. The welcome page allows me to sign in or register.
- Create the home app[front page] for the monopoly application [HTML, CSS, Bootstrap(http://getbootstrap.com/
- We should be able to test the home page by accessing the URL http://<name>:<port>
- Create the following pages:
	- Signup page [signup.html][userame, email & password]
	- Login page [login.html][username & password]
	- set the virtualEnv
#### Iteration # 2 [Task 2]

- Our information store is going to be SQLAlchemy [ User information storage as well as the game information]
- Create a database and populate users [Testing]

#### Iteration # 3 [ Task 3]

As a user, after the game start I MUST be able to enter the number of players [between 2 and 4]. 
If I press Cancel, then I MUST be able to exit the game.
- create the logic to support this capability in py.

#### Iteration # 4 [ Task 4]

As a user, I must be able to pick or choose a token to represent me on the board.
- Create / code the logic to allow the users to choose a token to represent them on th board.

##### # of Iterations for Milestone 1.0
1. TBD
2. TBD
3. TBD

#### Milestone 2.0
1. TBD
2. TBD
3. TBD

##### # of Iterations for Milestone 2.0
1. TBD
2. TBD
3. TBD

### Velocity
Timeline: xx days until Milestone 1.0 is due, xx days until Milestone 2.0 is due
Velocity: xx%
