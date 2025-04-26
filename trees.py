import __builtins__
from helper import smart_move

def plant_trees():
    # """
    # Plants trees in a grid pattern. The function starts at position (0, 0) and
    # moves across the grid using the `smart_move` function. Trees are planted at
    # positions where both x and y coordinates are either even or odd. If a tree
    # can be harvested, it is harvested before planting a new one.
    # """
    if get_pos_x() != 0 or get_pos_y() != 0:
        quick_print("Starting at (0, 0)")
    
    while True:
        quick_print("I am at "+str(get_pos_x)+", "+str(get_pos_y())+")")
        if can_harvest():
            harvest()
        if get_pos_x() %2 == 0 and get_pos_y() %2 == 0: # x even and y even
            quick_print("Plant a god dam tree")
            plant(Entities.Tree)
        elif get_pos_x() %2 != 0 and get_pos_y() %2 != 0: # x odd and y odd
            quick_print("Plant a god dam tree")
            plant(Entities.Tree)
        else: # get_pos_x() %2 ==0 and get_pos_y() %2 !=0 or get_pos_x() %2 !=0 and get_pos_y() %2 ==0: # x even and y odd or x odd and y even
            if get_ground_type() != Grounds.Grassland:
                quick_print("Tilling grassland -> soil")
                till()
            plant(Entities.Grass)
        smart_move()