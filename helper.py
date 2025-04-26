import __builtins__


#TODO bug in this where I need to pass in the previous position.
# If the previous position was at the top and I move east I know my next move is south, vice versa from the bottom.
# The bug is that when I increase the size of the world it can cause the drone to skip some columns.
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
    if pos_x % 2 == 0:
        if pos_y != max_world_size:
            move(North)
        else:
            move(East)
    elif pos_x % 2 != 0:
        if pos_y != 0:
            move(South)
        else:
            move(East)