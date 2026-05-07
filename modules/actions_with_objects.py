def try_to_add(layout_where_to_place, object_to_add):
    try:
        layout_where_to_place.remove_widget(object_to_add)
        layout_where_to_place.add_widget(object_to_add)
    except Exception:
        pass



def update(current_map_name, layout, character, buttons_to_place_list, objects_list, buttons_to_place_list_3d, objects_list_3d):
    is_on_object = 0
    if current_map_name == 'main_map':
        is_on_object_3d = 0
        for object_m_3d in objects_list_3d:
            if (character.pos[0] + character.size[0] / 2 >= object_m_3d.pos[0] and character.pos[0] + character.size[0] / 2 <= object_m_3d.pos[0] + object_m_3d.size[0]) and (character.pos[1] + character.size[1] / 2 >= object_m_3d.pos[1] and character.pos[1] + character.size[1] / 2 <= object_m_3d.pos[1] + object_m_3d.size[1]):
                is_on_object_3d = 1
            for button_m_3d in buttons_to_place_list_3d:
                if is_on_object_3d == 1:
                    layout.remove_widget(button_m_3d)
                    try_to_add(layout, button_m_3d)
                else:
                    layout.remove_widget(button_m_3d)
    else:
        for object_m in objects_list:
            if character.pos[0] + character.size[0] / 2 >= object_m.pos[0] and character.pos[0] + character.size[0] / 2 <= object_m.pos[0] + object_m.size[0]:
                is_on_object = 1
            for button_m in buttons_to_place_list:
                if is_on_object == 1:
                    layout.remove_widget(button_m)
                    try_to_add(layout, button_m)
                else:
                    layout.remove_widget(button_m)





