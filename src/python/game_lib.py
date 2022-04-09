import turtle
import game_map
import random
import math

# The map is stored as a list of lists structure
game_map_data = []

# These variables store the size (number of rows and columns) of the game map
game_map_total_rows = 0
game_map_total_cols = 0

# These variables store the current location (row and column) of the robot
robot_row = 0
robot_col = 0

# This variable is True when the game finishes, i.e. the robot reaches the exit
# or False otherwise
is_finished = False

# This variable is True when the robot cannot see the rest of the map, or False otherwise
robot_view = False

# This variable stores the decision making function and timing
timing = 100
current_task_handler = None

task_handlers = {"task4":None}

currentTask = None

total_number_of_energy_cells = 5
current_energy_cells = 0
min_cell_distance = 4
auto_cells_generation = True

#
# The following 8 functions are available to help make the robot's decision
#

# This function returns True if a wall is on the left of the robot
# or False otherwise
def leftIsWall():
    return game_map_data[robot_row][robot_col-1] == "B"


# This function returns True if a wall is on the right of the robot
# or False otherwise
def rightIsWall():
    return game_map_data[robot_row][robot_col+1] == "B"


# This function returns True if a wall is above the robot
# or False otherwise
def upIsWall():
    return game_map_data[robot_row-1][robot_col] == "B"


# This function returns True if a wall is below the robot
# or False otherwise
def downIsWall():
    return game_map_data[robot_row+1][robot_col] == "B"

# This function returns True if an exit is on the left of the robot
# or False otherwise
def leftIsExit():
    return game_map_data[robot_row][robot_col-1] == "E"


# This function returns True if an exit is on the right of the robot
# or False otherwise
def rightIsExit():
    return game_map_data[robot_row][robot_col+1] == "E"


# This function returns True if an exit is above the robot
# or False otherwise
def upIsExit():
    return game_map_data[robot_row-1][robot_col] == "E"


# This function returns True if an exit is below the robot
# or False otherwise
def downIsExit():
    return game_map_data[robot_row+1][robot_col] == "E"

def getTotalNumberOfEnergyCells():
    return total_number_of_energy_cells

def getNumberOfCollectedEnergyCells():
    return current_energy_cells

# This function lets you choose the game map to start the game from
def chooseGameMap(task, map_number):
    global currentTask
    global game_map_data
    global game_map_total_rows, game_map_total_cols
    global robot_row, robot_col
    global total_number_of_energy_cells
    
    currentTask = task

    # Get the 'raw' game map containing a big string
    if task != "custom":
        raw_game_map_data = game_map.getGameMap(task, map_number)[0]
        
    else:
        raw_game_map_data, currentTask = game_map.getGameMap(task, map_number)
    

    # Change the raw map of string into a list of lists
    game_map_data = raw_game_map_data.split("\n")
    for row in range(len(game_map_data)):
        game_map_data[row] = list(game_map_data[row])

    # Set the size of the map
    game_map_total_rows = len(game_map_data)
    game_map_total_cols = len(game_map_data[0])

    # Generate different position of energy_cells
    if currentTask =="task6":
        if auto_cells_generation:
            energy_cells = []
            for i in range(total_number_of_energy_cells):
                random_row, random_col = 0, 0
                this_position_not_ok = True
                while game_map_data[random_row][random_col]!=" " or this_position_not_ok:
                    random_row = random.randint(0, game_map_total_rows-1)
                    random_col = random.randint(0, game_map_total_cols-1)
                    this_position_not_ok = False
                    for energy_cell in energy_cells:
                        if math.sqrt(pow(random_row-energy_cell[0],2)+pow(random_col-energy_cell[1],2))<min_cell_distance:
                            this_position_not_ok=True
                energy_cells.append([random_row,random_col])
                game_map_data[random_row][random_col]="G"
        else:
            total_number_of_energy_cells = 0
            for row in game_map_data:
                total_number_of_energy_cells += row.count("G")

    # Search for the initial position of the robot
    for row in range(game_map_total_rows):
        for col in range(game_map_total_cols):
            if game_map_data[row][col] == "P":
                robot_row = row
                robot_col = col


# This function returns True if the robot can move to the target location
# or False otherwise
def isMoveable(target_row, target_col):
    # The robot moves out of the game map area
    if target_row < 0 or target_row >= game_map_total_rows or \
       target_col < 0 or target_col >= game_map_total_cols:
        print("The robot is out of bounds!")
        return False

    # A wall is there
    if game_map_data[target_row][target_col] == "B":
        print("The robot hits the wall!")
        return False

    return True


# This function tries to move the robot to a new location
def move(target_row, target_col):
    global robot_row, robot_col, current_energy_cells

    if isMoveable(target_row, target_col):
        # Change the current block to 'history'
        game_map_data[robot_row][robot_col] = "H"

        # Move the robot to the new location
        robot_row = target_row
        robot_col = target_col

        # Detect if the next block is energy cell
        if game_map_data[robot_row][robot_col] == "G":
            current_energy_cells += 1

        # Change the block to P if the robot is not at the exit
        if game_map_data[robot_row][robot_col] != "E":
            game_map_data[robot_row][robot_col] = "P"


# This function tries to move the robot to the left
def moveLeft():
    if not startToMove:
        return
    move(robot_row, robot_col - 1)
    robot_turtle.shape("/Users/chanyuhin/PycharmProjects/Allen/venv/Maze-Game/src/resource/gif/robot_left.gif")
        

# This function tries to move the robot to the right
def moveRight():
    if not startToMove:
        return
    move(robot_row, robot_col + 1)
    robot_turtle.shape("/Users/chanyuhin/PycharmProjects/Allen/venv/Maze-Game/src/resource/gif/robot_right.gif")


# This function tries to move the robot up one row
def moveUp():
    if not startToMove:
        return
    move(robot_row - 1, robot_col)
    robot_turtle.shape("/Users/chanyuhin/PycharmProjects/Allen/venv/Maze-Game/src/resource/gif/robot_up.gif")


# This function tries to move the robot down one row
def moveDown():
    if not startToMove:
        return
    move(robot_row + 1, robot_col)
    robot_turtle.shape("/Users/chanyuhin/PycharmProjects/Allen/venv/Maze-Game/src/resource/gif/robot_down.gif")


# This function moves the robot based on the given decision
# The decision can be one of "LEFT", "RIGHT", "UP" and "DOWN"
def moveRobot(decision):
    global is_finished, current_energy_cells

    # Show the decision
    print(decision)

    # Move the robot based on the decision
    if decision == "LEFT":
        moveLeft()
    elif decision == "RIGHT":
        moveRight()
    elif decision == "UP":
        moveUp()
    elif decision == "DOWN":
        moveDown()
    elif decision == "NONE":
        pass
    else:
        print("ERROR IN COMMAND, cannot understand the command.")
        return

    if game_map_data[robot_row][robot_col] == "E":
        is_finished = True

    if currentTask=="task6":
        if current_energy_cells!=1:
            print("Current energy cells", current_energy_cells)
        else:
            print("Current energy cell", current_energy_cells)
    # Update the game map
    drawGameMap()
    
    # Show the game over message when the game finishes
    if is_finished:
        showGameOver()


# This function is used for drawing a block (wall or empty space) in the map
def drawBlock(row, col, pencolor, fillcolor):
    # Go to the starting position
    drawing_turtle.goto(col - 0.5, row - 0.5)

    # Set up the color
    drawing_turtle.color(pencolor, fillcolor)

    # Draw the block
    drawing_turtle.down()
    drawing_turtle.begin_fill()
    for _ in range(4):
        drawing_turtle.forward(1)
        drawing_turtle.left(90)
    drawing_turtle.end_fill()
    drawing_turtle.up()


# This function draws the game map inside the turtle window
def drawGameMap():
    # Disable the tracer
    turtle.tracer(False)

    # Clear the current content
    drawing_turtle.clear()

    # Draw the game blocks
    for row in range(len(game_map_data)):
        for col in range(len(game_map_data[0])):
            # If the robot cannot view the rest of the map
            if robot_view and \
               abs(robot_row - row) + abs(robot_col - col) > 1:
                drawBlock(row, col, "", "black")
                continue

            # If it is a block...
            if game_map_data[row][col] == "B":
                drawBlock(row, col, "", "blue")

            # If it is the exit...
            elif game_map_data[row][col] == "E":
                drawBlock(row, col, "", "red")

            elif game_map_data[row][col] == "G":
                drawBlock(row, col, "", "green")

            # If it is the movement history...
            elif game_map_data[row][col] == "H":
                drawBlock(row, col, "", "grey80")

    # Draw the robot last
    for row in range(len(game_map_data)):
        for col in range(len(game_map_data[0])):
            # If it is the robot...
            if game_map_data[row][col] == "P":
                drawBlock(row, col, "brown", "")

                robot_turtle.up()
                robot_turtle.goto(col, row)

    # Update the turtle window
    turtle.tracer(True)


# This function shows the game over message inside the turtle window
# when the game is over
def showGameOver():
    # Disable the tracer
    turtle.tracer(False)

    # Draw the game over text
    drawing_turtle.goto((game_map_total_cols-0.5)/2, (game_map_total_rows-0.5)/2)
    drawing_turtle.color("red")

    if currentTask != "task6":
        drawing_turtle.write("You finished the game!!!", \
                         align="center", font=("Comic Sans", 24, "bold"))
    else:
        if current_energy_cells == total_number_of_energy_cells:
            drawing_turtle.write("You finished the game!!!", \
                         align="center", font=("Comic Sans", 24, "bold"))
        else:
            drawing_turtle.write("You found the exit", \
                         align="center", font=("Comic Sans", 24, "bold"))
            drawing_turtle.left(90)
            drawing_turtle.forward(1.2)
            drawing_turtle.write("but you have not found all energy cells...", \
                         align="center", font=("Comic Sans", 18, "bold"))

    # Update the turtle window
    turtle.tracer(True)


# This function is used by the key event to toggle the robot view
def toggleRobotView():
    global robot_view
    robot_view = not robot_view

startToMove = False

# The function sets the decision making functions
def setDecisionFuncForTask0(func):
    global task_handlers
    task_handlers["task0"] = func
    
def setDecisionFuncForTask4(func):
    global task_handlers
    task_handlers["task4"] = func
    
def setDecisionFuncForTask6(func):
    global task_handlers
    task_handlers["task6"] = func

# This is the main game loop
def gameLoop():
    global robot_col, robot_row, startToMove, total_number_of_energy_cells, current_energy_cells, currentTask
    # Give up if no function is given
    if current_task_handler == None:
        return

    startToMove = False
    before_col, before_row = robot_col, robot_row
    before_total_number_of_energy_cells, before_current_energy_cells = total_number_of_energy_cells, current_energy_cells
    before_currentTask = currentTask
    
    # Get the decision of the robot
    decision = current_task_handler()

    robot_col, robot_row = before_col, before_row
    total_number_of_energy_cells, current_energy_cells = before_total_number_of_energy_cells, before_current_energy_cells
    currentTask = before_currentTask
    # Make the robot move based on the decision
    startToMove = True
    moveRobot(decision)

    # Repeat the game loop
    if not is_finished:
        turtle.ontimer(gameLoop, timing)


# This function sets up the entire robot game using the selected game map
# and then starts the game
def startGame():
    global robot_turtle, drawing_turtle
    global current_task_handler

    # Set up the turtle window
    turtle.setup(500, 500)
    turtle.title("Robot Maze Game")

    # Set up the coordinate system of the window to be the same as the map
    turtle.setworldcoordinates(-1, game_map_total_rows + 0.5, game_map_total_cols + 0.5, -1)

    # Add the robot images as turtle shapes
    turtle.addshape("/Users/chanyuhin/PycharmProjects/Allen/venv/Maze-Game/src/resource/gif/robot_up.gif")
    turtle.addshape("/Users/chanyuhin/PycharmProjects/Allen/venv/Maze-Game/src/resource/gif/robot_down.gif")
    turtle.addshape("/Users/chanyuhin/PycharmProjects/Allen/venv/Maze-Game/src/resource/gif/robot_left.gif")
    turtle.addshape("/Users/chanyuhin/PycharmProjects/Allen/venv/Maze-Game/src/resource/gif/robot_right.gif")

    # Create a robot turtle
    robot_turtle = turtle.Turtle()
    robot_turtle.up()
    robot_turtle.shape("/Users/chanyuhin/PycharmProjects/Allen/venv/Maze-Game/src/resource/gif/robot_up.gif")

    # Create a turtle for drawing the game graphics such as the map
    drawing_turtle = turtle.Turtle()
    drawing_turtle.up()
    drawing_turtle.hideturtle()

    # Set up the key event for the 'r' key
    turtle.onkeypress(toggleRobotView,'r')
    turtle.listen()

    # Update the game map
    drawGameMap()

    # Select corresponding task handler
    if  currentTask == "task4":
        current_task_handler = task_handlers["task4"]
                
    else:
        current_task_handler = task_handlers["task6"]

    # Start the game loop
    turtle.ontimer(gameLoop, timing)
    
    turtle.done()
