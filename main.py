import __builtins__

while True:
    move(East)
    for i in range(get_world_size()):
        harvest()
        move(North)