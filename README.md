# **IST-303-Team-C-Project**

### Team name

Monopoly Masters

 
### Team members

Pete Buwembo, Cindy Cheng, Christine Kao, Shih Chieh Lin and Aary Sheoran

### November 3, 2020 Slide Deck link: 
https://docs.google.com/presentation/d/1_iKEWX8EElyx1-7d6KfkixPc8DYAO7kmoEqaD10auKo/edit#slide=id.p

### How to run the application instruction

#### Requirements and Setup

* Python 3.6.9
* pip 20.2.2
* Flask 0.12.2
* Flask-SQLAlchemy
* Virtual Environment 16.4.0
 
#### Instructions to run the application

* git clone https://github.com/pete-buwembo/monopoly-masters.git
* cd monopoly-masters
* virtualenv venv -p python3
* source venv/bin/activate
* pip3 install -r requirements.txt
* python3 app.py

#### Run script

TBD


#### Tests

Run pytest by: 
1. From the main GitHub repo (https://github.com/pete-buwembo/monopoly-masters.git), go to Code and download zipfile
2. Go to the Download Folder, unzip the monopoly masters masters folder
3. Find the project_pytest folder and drag to Desktop
4. Open terminal window, install pytest by entering "$ pip install pytest" 
5. Enter "$ cd desktop" to go to Desktop
6. Enter "$ cd project_pytest" to go to project_pytest folder on Desktop
7. Enter "$ ls" to see the test files
8. Enter "$ pytest --emoji" to run pytest

** Pytest results: 15 failed and 15 passed **


 
### Application concept:

We are building a virtual version of the popular board game Monopoly, to be played by between 2 and 4 players through python. During the quarantine, this game is a fun but socially distanced way to socialize with friends. Using randomness generators and graphical interfaces within python, we can create a virtual simulation of the game that stays true to the original while being quicker and easier.

 
 
### Stakeholders

Players who are into classic board games. New players who are looking for digital board games to play and also spend time with their friends.

 

### User stories

1. **User welcome page** - priority 10 - 5 days

   - As a user, I can see a welcome page.

2. **Roll dice** - priority 20 - 5 days

   - As a user, I can roll the dice and move around the board.

3. **Cards** - priority 20 - 5 days

   - As a user, I can pick cards from Chance and Chest decks.

4. **Set number of players** - priority 20 - 10 days

   - As a user, I can set the number of players.

5. **Choose character token** - priority 40 - 5 days

   - As a user, I am able to pick character.

6. **Banker selection** - priority 40 - 5 days

   - As a user, I am able to create bank.

 

#### Decomposition of user stories

##### 5 days - priority 10

1. As a user, I can see a welcome page when I first logged on. 

   - The welcome page allows user sign in.

   - The welcome page allows user to register.

 

##### 5 days, priority 20

2. As a user, I can roll the dice and move around the board.

   - User must allow must be allowed to roll the dice.

   - User must be able to move character around the board clockwise.

   - User must be able to roll and see who goes first with the highest roll to start the game.

 

##### 5 days, priority 20

3. As a user, I can pick cards from Chance and Chest decks.

   - User must be able to pick from card deck. 

 

##### 5 days, priority 20

4. As a user, I must be able to enter the number of players [between 2 and 4].

   - User must be able to specify the number of players in a game.

 

##### 5 days, priority 40

5. As a user, I am able to pick character.

   - User must be able to choose character token to represent him/herself.

 

##### 5 days, priority 40

6. As a user, I am able to create bank.

   - User must be able to create bank.

   - User must be able to designate one other user as banker.


#### Milestone 1.0

1. Welcome page

2. Roll Dices

3. Chest and Chance Cards

 

##### 2 Iterations for Milestone 1.0: 4 weeks

##### Iteration 1 (2 weeks)

1. Create welcome page with Flask - Done

2. Create roll dices function - Done

3. Create Chest and Chance card functions - Done

 

##### Iteration 2 (2 weeks)

1. Link welcome page & Login to database - Done

2. Test roll dices function

3. Test card functions

 

#### Milestone 2.0

1. Home app and database linking

2. Roll dices function completion [2-4 players]

2. Chest and Chance card functions demo


##### # of Iterations for Milestone 2.0

1. Linking the flask app to the monoply game after a user is registered or logged in

2. Linking all features of the application

3. Functional and User Acceptance Testing

 

### Velocity

Timeline: 20 days until Milestone 1.0 is due, 20 days until Milestone 2.0 is due

Velocity: 30%
