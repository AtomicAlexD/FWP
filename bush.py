import __builtins__

def plant_bush():
    world_size = get_world_size()
    if get_pos_x() != 0 or get_pos_y() != 0:
        quick_print("Starting at (0, 0)")
    quick_print("World size: " + str(world_size))
    while True:
        move(East)
        for i in range(world_size):
            if can_harvest():
                harvest()
            plant(Entities.Bush)
            move(North)
plant_bush()