# Battleship AI Simulator
This project presents an AI vs. AI Battleship simulation, using a combination of Python 3 and PyGame. The implementation showcases the popular strategy game, Battleship.

# How to Use
For comprehensive instructions on gameplay, please refer to the following [link](https://en.wikipedia.org/wiki/Battleship_(game)). The design of this simulation assumes it to be played against another Python AI employing a similar framework. The grids are rendered using the PyGame GUI, while the console efficiently handles the coordination of guesses and outcome notifications.

Allow us to establish the framework for this simulation. Designate one AI as "A" and the opposing AI as "B." The game commences once both AIs request to know whether A or B will take the first turn (USER or OPPONENT). Subsequently, A and B alternate turns, strategically guessing the location of their adversary's ships and promptly declaring whether the guess results in a HIT or a MISS. The objective is to sink all five of the opponent's ships before they can successfully sink A's fleet. A scenario outlining the gameplay is presented below:

# Scenario
 - Assume A is assigned the first turn.
 - The AI managing A inputs "USER."
 - The AI managing B inputs "OPPONENT."
 - A displays a coordinate guess on the console (e.g., A9).
 - The AI managing B inputs the guess (A9) in their console.
 - B processes the information, determines if it constitutes a HIT or a MISS, updates the grid accordingly, and displays the outcome on their console (assuming it was a MISS).
 - The AI managing A inputs the result, "MISS," into their console.
 - A processes the information, updates the grid, and displays the outcome.
 - It is now B's turn. B displays a coordinate guess on their console (e.g., J1).
 - The AI managing A inputs the guess (J1) in their console.
 - A processes the information, determines if it constitutes a HIT or a MISS, updates the grid, and displays the outcome on their console (assuming it was a HIT, targeting the "AIRCRAFT CARRIER").
 - The AI managing B inputs the result, "HIT, AIRCRAFT CARRIER," into their console.
 - B processes the information, updates the grid, and displays the outcome.
 - Repeat the previous steps as the game progresses.

This simulation records the number of hits, misses, total shots, and remaining ships for both the user and the opponent. In the GUI window, the user's ships are showcased on the left, while the opponent's grid is displayed on the right. Each round, the ships are randomly generated, ensuring an engaging and unpredictable experience. 

# Battleship Guessing Algorithm
The AI's guessing algorithm in this simulation adopts a straightforward approach. At the start of each round, it randomly selects a point on the grid and begins guessing at every other spot, moving horizontally. Once it completes a row, it shifts down to the next row. Should it reach the bottom of the grid, it resumes at the top, continuing the horizontal pattern until all spots have been attempted.

# Ships
 - AIRCRAFT CARRIER: 5
 - BATTLESHIP: 4
 - CRUISER: 3
 - SUBMARINE: 3
 - DESTROYER: 2

# Editor
This project has been coded using the IDLE Integrated Development Environment.

# Download
 - Click on the green download button labelled “Code”.
 - Enter the dropdown menu and select “Download ZIP”.
 - Once download is complete, extract the files from the ZIP file.

# Dependencies
To run this simulation, ensure that you have the following dependencies:

 - [Python 3](https://www.python.org/downloads/) (3.6+)
 - [PyGame](https://www.pygame.org/wiki/GettingStarted)
