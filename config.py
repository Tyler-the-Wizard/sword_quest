def init():
    global camera_pos, L, R, U, D, Jump, sprites, actors, player

    camera_pos = (100, 0)

    # Related to movement; set in event_handler and read in game
    L = False
    R = False
    U = False
    D = False
    Jump = False

    # Global arrays for drawing objects to the screen
    sprites = []
    actors = []

    # Several important game objects
    player = False