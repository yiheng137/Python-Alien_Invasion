# Python-Alien_Invasion

This project is based on the Alien Invasion game introduced in the book PYTHON CRASH COURSE. I did many modification on the data structure, functions, and panels.  

Description of Projects:  
In Alien Invasion, the player controls a ship that appears at the bottom center of the screen. The player can move the ship up, down, right, and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. The player shoots and destroys the aliens to gain as many as scores. If the player shoots all the aliens, a new fleet appears. If any alien hits the player’s ship or reaches the bottom of the screen, the player loses a ship. If the player loses three ships, the game ends. A rank of top-three scores with the player's name will be displayed on the game over panel.

Description of Main Files:  
run.py: start the game by running this code.  
alien_invasion.py: includes the main game loop for listening the events and switch the game panels.  
game_stats.py: stores the player's states, such as HP of the ship, score, and rank.  
GUI.py: stores the different game panels, such as title panel, game play panel, and game over panel.  
settings.py: stores all game and GUI settings.  

Display of the Game:  
<img width="500" alt="1" src="https://user-images.githubusercontent.com/39048778/198061309-6b6442e7-c01d-42a5-ae1d-054bf164e7a0.png">  
<img width="300" alt="1" src="https://user-images.githubusercontent.com/39048778/198046241-f03c8d15-101d-4679-acfa-ec0835abee1e.png">
<img width="300" alt="2" src="https://user-images.githubusercontent.com/39048778/198046748-92dd208a-1653-4280-8de4-caac5a41fcfb.png">
<img width="300" alt="3" src="https://user-images.githubusercontent.com/39048778/198046805-bbe52656-c152-4766-a902-12b344088a9e.png">

Note: This project is only used for python practice (No intension for the business purpose). Some resources are gained from Python Crash Course. Please manually make the folders: objects and panels as sources root. 

Requirements:
  - Python 3 (v3.8)
  - Pygame (v2.1.2)

Cloning the Repository:  
$ git clone https://github.com/yiheng137/Python-Alien_Invasion.git  
$ cd Python-Alien_Invasion  

Play the game:  
$ python run.py
