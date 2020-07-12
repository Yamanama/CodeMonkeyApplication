# CodeMonkeyApplication

Trivial Purfuit Game

## Codebase location

[src](src)

### Working together

- Make sure to work in an indepentant branch
  
  `git branch featureName`

- Make sure commit messages are descriptive of the work done

- Feel free to ask for git help if you're unfamiliar

### Sample

Check out [Dice](src/Dice.py) as a sample python class that will be useful in the creation of our project!

## Unit Testing

### Sample

Check out [TestDice](src/TestDice.py) as a sample unittest class for testing our code!

### Coverage
```
cd src
coverage run --source=. .\TestSuite.py
coverage report -m
```
Sample coverage output:
```
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
Board.py                     6      0   100%
Computer.py                 14      0   100%
DatabaseHandler.py          42      0   100%
Dice.py                      8      0   100%
Game.py                     35      0   100%
Human.py                     5      0   100%
Player.py                   11      0   100%
QuestionHandler.py          27      0   100%
SettingsHandler.py          21      0   100%
TestBoard.py                 7      0   100%
TestComputer.py             12      0   100%
TestDatabaseHandler.py      20      0   100%
TestDice.py                 11      0   100%
TestGame.py                  8      0   100%
TestHuman.py                 6      0   100%
TestPlayer.py                8      0   100%
TestQuestionHandler.py      23      0   100%
TestSettingsHandler.py      12      0   100%
TestSuite.py                23      0   100%
------------------------------------------------------
TOTAL                      299      0   100%
```
