import __builtins__

def plant_carrots():
    world_size = get_world_size()
    if get_pos_x() != 0 or get_pos_y() != 0:
        clear()
        quick_print("Starting at (0, 0)")
    quick_print("World size: " + str(world_size))
    while True:
        move(East)
        for i in range(get_world_size()):
            if get_ground_type() == Grounds.Grassland:
                quick_print("Tilling grassland -> soil")
                till()
            if can_harvest():
                harvest()
            plant(Entities.Carrot)
            move(North)

plant_carrots()