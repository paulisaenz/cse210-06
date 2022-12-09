# CSE 210-06
Final Project for CSE 210 - Pac-Man Game

# **Overview:**
- Pac-Man is a maze action game. The player controls the character through an enclosed maze. The objective of the game is to eat all of the dots placed in the maze while avoiding four colored ghosts.

## **Rules:**
- Players can move up, down, left, and right. 
- Player moves using the up, down, left and right keys. 
- Player has to escape from the ghosts, while eating all the dots.
- Pac-Man can eat blue ghosts for bonus points; when a ghost is eaten, their eyes make their way back to the center box in the maze, where the ghost "regenerates" and resumes their normal activity.
- If Pac-Man is caught by a ghost, he will lose a life; the game ends when all lives are lost.

**Requirements:**
- The program includes a README file.
- The program includes class and method comments.  
- The program contains 20 classes.
- The game remains true to game play described in the overview.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- cse210-06           (source code for game)
  +-- assets            (game resources)
    +-- data            (information visual resources)
    +-- fonts           (game visual resources)
    +-- images          (game visual resources)
    +-- sounds          (game sonorus resources)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## **Authors: (Team E)**

- Diab, Garren Mark (dia22004@byui.edu)
- Mazzarella-Woelzl, Alison Reed (maz12005@byui.edu)
- Saenz, Paula (sae21002@byui.edu)