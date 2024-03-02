import curses, random, time

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(False)
stdscr.nodelay(True)

obs = '.'
player = 'x'
food_ch = '*'
food_num = 10
score = 0

maxl = curses.LINES - 1
maxc = curses.COLS - 1

world = []
food = []

# making sure player cannot go outside the screen
def in_range(a, min, max):
    if a > max:
        return max
    if a < min:
        return min
    else:
        return a

# getting two random values that doesn't overlap
def random_place():
    i = random.randint(0, maxl)
    j = random.randint(0, maxc)
    while world[i][j] != ' ':
        i = random.randint(0, maxl)
        j = random.randint(0, maxc)
    return i, j

def init():
    global player_c, player_l
    for i in range(maxl + 1):
        world.append([])
        for j in range(maxc + 1):
            world[i].append(' ' if random.random() > 0.03 else obs)

    for i in range(food_num):
        foodl, foodc = random_place()
        fooda = random.randint(1000, 10000)
        food.append((foodl, foodc, fooda))
    
    player_l, player_c = random_place()

def draw():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i, j, world[i][j]) 
    
    for f in food:
        fl, fc, fa = f
        stdscr.addch(fl, fc, food_ch)

    stdscr.addch(player_l, player_c, player)
    stdscr.addstr(1, 1, f"Score: {score}")
    
    stdscr.refresh()

# moving function
def move(c):
    global player_l, player_c
    if c == 'w' and world[player_l - 1][player_c] != obs:
        player_l -= 1
    elif c == 's' and world[player_l + 1][player_c] != obs:
        player_l += 1
    elif c == 'a' and world[player_l][player_c - 1] != obs:
        player_c -= 1
    elif c == 'd' and world[player_l][player_c + 1] != obs:
        player_c += 1

    player_l = in_range(player_l, 0, maxl - 1)
    player_c = in_range(player_c, 0, maxc - 1)

# eating food and keeping score
def check_food():
    global score
    for i in range(len(food)):
        fc, fl, fa = food[i]
        if player_l == fc and player_c == fl:
            score += 10
            new_fl, new_fc = random_place()
            new_fa = random.randint(1000, 10000)
            food[i] = (new_fl, new_fc, new_fa)

init()

playing = True

# main loop
while playing:
    try:
        c = stdscr.getkey()
    except:
        c = ''

    if c in 'awsd':
        move(c)
    elif c.lower() == 'q':
        playing = False
    
    check_food()
    draw()

curses.endwin()
