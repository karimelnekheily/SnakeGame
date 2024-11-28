import curses
import random

# initialize the curses library to create our screen
screen = curses.initscr()
# hide curser
curses.curs_set(0)
# get max screen height and width
screen_height, screen_width = screen.getmaxyx()

# create a new window
window = curses.newwin(screen_height, screen_width, 0, 0)
# allow window to receive input from keyboard
window.keypad(True)
# set the delay for updating the screen
window.timeout(400)
# set the x,y coordinates of the initial position of snake's head
snk_x = screen_width // 4
snk_y = screen_height // 2
# define the initial position of the snake body
snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]
# create the food in the middle of window
food = [screen_height // 2, screen_width // 2]
# add the food by using PI character from curses module
window.addch(food[0], food[1], curses.ACS_PI)
# set initial movement direction to right
key = curses.KEY_RIGHT
# create game loop that loops forever until player loses or quits the game\
try:

    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key
        if snake[0][0] in [0, screen_height] or snake[0][1] in [
            0, screen_width
        ] or snake[0] in snake[1:]:
            curses.endwin()
            quit()

        new_head = [snake[0][0], snake[0][1]]
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        snake.insert(0, new_head)

        if snake[0] == food:
            food = None
            while food is None:
                new_food = [
                    random.randint(1, screen_height - 1),
                    random.randint(1, screen_width - 1)
                ]
                food = new_food if new_food not in snake else None
            window.addch(food[0], food[1], curses.ACS_PI)

        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
finally:
    curses.endwin()