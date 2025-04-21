import __builtins__

while True:
    move(East)
    for i in range(get_world_size()):
        while i==1:
            if can_harvest():
                harvest()
            move(North)
        while i==2:
            if can_harvest():
                harvest()
            plant(Entities.Bush)
            move(North)
        while i==3:
            if can_harvest():
                harvest()
            till()
            plant(Entities.Carrot)
            move(North)