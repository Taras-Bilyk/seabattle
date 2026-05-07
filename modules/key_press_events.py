
step = 10
key_pressed = 'none'
def move(key):
    x = 0
    y = 0
    if key == 'a':
        x = step
        global key_pressed
        key_pressed = 'a'
    if key == 'd':
        x = -step
        key_pressed = 'd'


    if key == 'w':
        y = -step
        key_pressed = 'w'
    if key == 's':
        y = step
        key_pressed = 's'



    data = [x, y]
    return data
def stop_moving():
    x = 0
    y = 0
    data = [x, y]
    return data
