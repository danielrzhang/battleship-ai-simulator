# Battleship
An AI vs. AI battleship project that I created with a partner in ICS2O (Grade 10 Computer Science) using Python 3 and PyGame. It took a few weeks to develop, and this program implements the popular strategy game, Battleship, except this is an AI that plays it. 

# How to Play
For instructions on how to play, click [here](https://en.wikipedia.org/wiki/Battleship_(game)). This was meant to be played against another Python AI with a similar layout. The grids are displayed using GUI, and the messages of guessing coordinates and hitting or missing are displayed on the console.

Let’s assume that my AI is called A and the opponent AI is called B. The game begins when both AIs ask if A or B goes first (asking USER or OPPONENT). A and B take turns guessing where their opponent’s ships are, and stating whether the guess is a HIT or a MISS. You win if you sink all 5 of the opponent’s ships before they sink all of yours. An exemplar scenario for playing the game is shown below:

# Scenario
 - Assume A goes first
 - User manning A inputs USER
 - User manning B inputs OPPONENT
 - A displays a coordinate guess on the console (ex: A9)
 - User manning B inputs the guess, A9, in their console
 - B stores that information determines if there is a HIT or a MISS, and displays it on the grid. Then, they display the result to their console (assume it was a MISS)
 - User manning A inputs the result, MISS, in their console
 - A stores that information, and displays it to their grid.
 - It is now B’s turn. B displays a coordinate guess on their console (ex: J1)
 - User manning A inputs the guess, J1, in their console
 - A stores that information determines if there is a HIT or a MISS, and displays it on the grid. Then, they display the result to their console (assume it was a HIT,      AIRCRAFT CARRIER)
 - User manning B inputs the result, HIT, AIRCRAFT CARRIER, in their console
 - B stores that information, and displays it to their grid.
 - Repeat

This scenario is a lot to read and take in, but the whole process probably takes about 5 seconds.  The game records the number of hits, misses, total shots, and ships remaining for the user and opponent. In the GUI window, your ships are on the left, while your opponent’s grid is on the right. The ships are randomly generated every round. 

# Battleship Guessing Algorithm
The guessing algorithm for this AI is pretty basic. It randomly chooses a point on the grid at the beginning of the round, and guesses at every other spot on the grid, moving down. If it reaches the bottom of the grid, it starts back at the top, and continues with every other spot.

# Ships
 - AIRCRAFT CARRIER: 5
 - BATTLESHIP: 4
 - CRUISER: 3
 - SUBMARINE: 3
 - DESTROYER: 2

# Editor
 - Coded with IDLE

# Download
 - Click on the green download button labelled “Code”.
 - Enter the dropdown menu and select “Download ZIP”.
 - Once download is complete, extract the files from the ZIP file.

# Dependencies
 - Python 3 (3.1 at the very minimum)
 - PyGame




