import __builtins__

def smart_move():
    # """
    # Moves the character in a zigzag pattern across the grid.
    # If the x-coordinate is even, the character moves north unless at the top edge,
    # in which case it moves east. If the x-coordinate is odd, the character moves
    # south unless at the bottom edge, in which case it moves east.
    # """
    pos_x = get_pos_x()
    pos_y = get_pos_y()
    max_world_size = get_world_size()-1
    if pos_x == max_world_size and pos_y == max_world_size:
        move(North)
        move(East)
    elif pos_x % 2 == 0:
        if pos_y != max_world_size:
            move(North)
        else:
            move(East)
    elif pos_x % 2 != 0:
        if pos_y != 0:
            move(South)
        else:
            move(East)