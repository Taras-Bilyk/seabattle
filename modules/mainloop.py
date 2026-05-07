import sys
sys.path.append('.')
import key_press_events

side = 'none'
side_v = 'none'
side_bg = 'none'
side_bg_v = 'none'

def update_pos(map_name, current_layout, character, x, y, window_width, window_height):
    if map_name != 'none':
        size_of_aside_barriers = window_width / 5
        size_of_aside_barriers_y = window_height / 15
        if (character.pos[0] >= size_of_aside_barriers and character.pos[0]+character.size[0] <= window_width-size_of_aside_barriers) and (character.pos[1] >= size_of_aside_barriers_y and character.pos[1]+character.size[1] <= window_height-size_of_aside_barriers_y):    #move logic for character
            if map_name == 'main_map':
                character.pos = (character.pos[0] - x, character.pos[1] - y)
            else:
                character.pos = (character.pos[0] - x, character.pos[1])
            global side
            global side_v
            side = 'none'
            side_v = 'none'
        else:
            side = 'none'
            side_v = 'none'
            if character.pos[0] <= size_of_aside_barriers:
                side = 'left'
            if character.pos[0]+character.size[0]>=window_width-size_of_aside_barriers:
                side = 'right'
            if map_name == 'main_map':
                if character.pos[1] <= size_of_aside_barriers_y:
                    side_v = 'bottom'
                if character.pos[1]+character.size[1]>=window_height-size_of_aside_barriers_y:
                    side_v = 'top'
            if side != 'right' and key_press_events.key_pressed == 'd':
                character.pos = (character.pos[0] + abs(x), character.pos[1])
            elif side != 'left' and key_press_events.key_pressed == 'a':
                character.pos = (character.pos[0] - abs(x), character.pos[1])
            if map_name == 'main_map':
                if side_v != 'top' and key_press_events.key_pressed == 'w':
                    character.pos = (character.pos[0], character.pos[1] + abs(y))
                elif side_v != 'bottom' and key_press_events.key_pressed == 's':
                    character.pos = (character.pos[0], character.pos[1] - abs(y))
            if side != 'none' or side_v != 'none':
                if (current_layout.pos[0] <= 0 and current_layout.pos[0] + current_layout.size[0] >= window_width) and (current_layout.pos[1] <= 0 and current_layout.pos[1] + current_layout.size[1] >= window_height):  # move logic for background
                    if map_name == 'main_map':
                        if side != 'none' and side_v != 'none' and (key_press_events.key_pressed == 'a' or key_press_events.key_pressed == 'd'):
                            current_layout.pos = (current_layout.pos[0] + x, current_layout.pos[1])
                        elif side != 'none' and (key_press_events.key_pressed == 'a' or key_press_events.key_pressed == 'd'):
                            current_layout.pos = (current_layout.pos[0] + x, current_layout.pos[1])
                        else:
                            current_layout.pos = (current_layout.pos[0], current_layout.pos[1])
                        if side_v != 'none' and (key_press_events.key_pressed == 'w' or key_press_events.key_pressed == 's'):
                            current_layout.pos = (current_layout.pos[0], current_layout.pos[1] + y)
                    else:
                        current_layout.pos = (current_layout.pos[0] + x, character.pos[1])
                    global side_bg
                    global side_bg_v
                    side_bg = 'none'
                    side_bg_v = 'none'
                else:
                    side_bg = 'none'
                    side_bg_v = 'none'
                    if current_layout.pos[0] >= 0:
                        side_bg = 'left'
                    if current_layout.pos[0] + current_layout.size[0] <= window_width:
                        side_bg = 'right'
                    if map_name == 'main_map':
                        if current_layout.pos[1] >= 0:
                            side_bg_v = 'bottom'
                        if current_layout.pos[1] + current_layout.size[1] <= window_height:
                            side_bg_v = 'top'
                    if side_bg != 'right' and key_press_events.key_pressed == 'd':
                        current_layout.pos = (current_layout.pos[0] - abs(x), current_layout.pos[1])
                    elif side_bg != 'left' and key_press_events.key_pressed == 'a':
                        current_layout.pos = (current_layout.pos[0] + abs(x), current_layout.pos[1])
                    if map_name == 'main_map':
                        if side_bg_v == 'bottom' and key_press_events.key_pressed == 'w':
                            current_layout.pos = (current_layout.pos[0], current_layout.pos[1] - abs(y))
                        elif side_bg_v == 'top' and key_press_events.key_pressed == 's':
                            current_layout.pos = (current_layout.pos[0], current_layout.pos[1] + abs(y))







    #=====================================================







