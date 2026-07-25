SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

ALIEN_1_WIDTH = 32
ALIEN_1_HEIGHT = 16
ALIEN_2_WIDTH = 32
ALIEN_2_HEIGHT = 16
GUN_WIDTH = 32
GUN_HEIGHT = 32
SAUCER_HEIGHTH = 16
SAUCER_WIDTH = 16
ALIEN_MOVE_LIMIT = 30
ALIEN_MOVE_DISTANCE = 5


GUN_LEFT_LIMIT = -(SCREEN_WIDTH / 2) + 30
GUN_RIGHT_LIMIT = (SCREEN_WIDTH / 2) - 30
GUN_VER_LIMIT = -2 + 20
GUN_MOVE_DISTANCE = 20
GUN_COLLISION_DISTANCE = 20
GUN_INITIAL_POSITION = (0, -250)

BULLET_BOTTOM_LIMIT = -(SCREEN_HEIGHT / 2) + 30
BULLET_TOP_LIMIT = (SCREEN_HEIGHT / 2) - 30
BULLET_MOVE_DISTANCE = 20
BULLET_COLLISION_DISTANCE = 30
BULLET_MOVE_SPEED = 100  # mseconds

ALIEN_FIRE_TICK = 20  # fire every 20 ticks

BUTTON_START_POS = (GUN_LEFT_LIMIT - 10, GUN_VER_LIMIT - 10)
BUTTON_FONT_SIZE = 12
BUTTON_FONT = ("Arial", BUTTON_FONT_SIZE, "bold")

TILE_ROWS = 4
TILE_COLUMNS = 8
TILE_SEP_X = 45
TILE_SEP_Y = 30
TILE_PADX = 60
TILE_PADY = 30
TILE_LEFT_LIMIT = -(SCREEN_WIDTH / 2) + TILE_PADX
TILE_RIGHT_LIMIT = (SCREEN_WIDTH / 2) - TILE_PADX
TILE_TOP_LIMIT = (SCREEN_HEIGHT / 2) - TILE_PADY
TILE_BOTTOM_LIMIT = -(SCREEN_HEIGHT / 2) + TILE_PADY


def calculate_dimensions(level_count=0):
    base_rows = TILE_ROWS
    base_cols = TILE_COLUMNS
    new_rows = base_rows + level_count
    new_cols = base_cols + (2 * level_count)
    new_width = SCREEN_WIDTH + (ALIEN_1_WIDTH * 2)
    new_height = SCREEN_HEIGHT + (ALIEN_1_HEIGHT * level_count)
    return new_width, new_height, new_rows, new_cols


def recalculate_limits(width, height, rows, cols):
    new_padx = 60
    new_pady = 30
    new_left_limit = -(width / 2) + new_padx
    new_right_limit = (width / 2) - new_padx
    new_top_limit = (height / 2) - new_pady
    new_bottom_limit = -(height / 2) + new_pady
    return new_left_limit, new_right_limit, new_top_limit, new_bottom_limit


def update_config_for_level(level_count=0):
    global SCREEN_WIDTH, SCREEN_HEIGHT, TILE_ROWS, TILE_COLUMNS, TILE_LEFT_LIMIT, TILE_RIGHT_LIMIT, TILE_TOP_LIMIT, TILE_BOTTOM_LIMIT, GUN_LEFT_LIMIT, GUN_RIGHT_LIMIT, BULLET_BOTTOM_LIMIT, BULLET_TOP_LIMIT, BUTTON_START_POS
    new_width, new_height, new_rows, new_cols = calculate_dimensions(level_count)
    SCREEN_WIDTH = new_width
    SCREEN_HEIGHT = new_height
    TILE_ROWS = new_rows
    TILE_COLUMNS = new_cols
    TILE_LEFT_LIMIT = -(new_width / 2) + TILE_PADX
    TILE_RIGHT_LIMIT = (new_width / 2) - TILE_PADX
    TILE_TOP_LIMIT = (new_height / 2) - TILE_PADY
    TILE_BOTTOM_LIMIT = -(new_height / 2) + TILE_PADY
    GUN_LEFT_LIMIT = -(new_width / 2) + 30
    GUN_RIGHT_LIMIT = (new_width / 2) - 30
    BULLET_BOTTOM_LIMIT = -(new_height / 2) + 30
    BULLET_TOP_LIMIT = (new_height / 2) - 30
    BUTTON_START_POS = (GUN_LEFT_LIMIT - 10, GUN_VER_LIMIT - 10)


def print_config():
    print(f"SCREEN_WIDTH: {SCREEN_WIDTH}")
    print(f"SCREEN_HEIGHT: {SCREEN_HEIGHT}")
    print("------------------------")
    print(f"GUN_LEFT_LIMIT: {GUN_LEFT_LIMIT}")
    print(f"GUN_RIGHT_LIMIT: {GUN_RIGHT_LIMIT}")
    print(f"GUN_MOVE_DISTANCE: {GUN_MOVE_DISTANCE}")
    print(f"GUN_COLLISION_DISTANCE: {GUN_COLLISION_DISTANCE}")
    print("------------------------")
    print(f"BULLET_MOVE_DISTANCE: {BULLET_MOVE_DISTANCE}")
    print(f"BULLET_MOVE_SPEED: {BULLET_MOVE_SPEED}")
    print(f"BULLET_COLLISION_DISTANCE: {BULLET_COLLISION_DISTANCE}")
    print("------------------------")
    print(f"ALIEN TILE_ROWS: {TILE_ROWS}")
    print(f"ALIEN TILE_COLUMNS: {TILE_COLUMNS}")
    print(f"ALIEN TILE_LEFT_LIMIT: {TILE_LEFT_LIMIT}")
    print(f"ALIEN TILE_TOP_LIMIT: {TILE_TOP_LIMIT}")
    print(f"TILE_RIGHT_LIMIT: {TILE_RIGHT_LIMIT}")
    print(f"TILE_BOTTOM_LIMIT: {TILE_BOTTOM_LIMIT}")
