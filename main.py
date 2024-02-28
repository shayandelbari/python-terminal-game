import curses, random, time

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(False)
stdscr.nodelay(True)

obs = '.'
player = 'x'

maxl = curses.LINES - 1
maxc = curses.COLS - 1

world = []

# player_l = player_c = 0

def init():
    global player_c, player_l
    for i in range(maxl):
        world.append([])
        for j in range(maxc):
            world[i].append(' ' if random.random() > 0.03 else obs)
    player_l = random.randint(0, maxl)
    player_c = random.randint(0, maxc)

def draw():
    for i in range(maxl):
        for j in range(maxc):
            stdscr.addch(i, j, world[i][j])
    stdscr.addch(player_l, player_c, player)
    stdscr.refresh()

def move(c):
    global player_l, player_c
    if c == 'w':
        player_l -= 1
    elif c == 's':
        player_l += 1
    elif c == 'a':
        player_c -= 1
    elif c == 'd':
        player_c += 1

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
    draw()

curses.endwin()
