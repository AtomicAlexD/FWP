import __builtins__

def smart_move():
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


def plant_trees():
    if get_pos_x() != 0 or get_pos_y() != 0:
        quick_print("Starting at (0, 0)")
    
    while True:
        quick_print("I am at "+str(get_pos_x)+", "+str(get_pos_y())+")")
        if can_harvest():
            harvest()
        if get_pos_x() %2 == 0 and get_pos_y() %2 == 0:
            quick_print("Plant a god dam tree")
            plant(Entities.Tree)
        elif get_pos_x() %2 != 0 and get_pos_y() %2 != 0:
            quick_print("Plant a god dam tree")
            plant(Entities.Tree)
        smart_move()

plant_trees()
