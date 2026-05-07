def set(character, skin_name, description, confirm_button):
    if skin_name == 'sigma':
        character.source = 'images/characters/sigma.png'
        description.source = 'images/characters/d2.png'
    elif skin_name == 'rekardo':
        character.source = 'images/characters/rekardo.png'
        description.source = 'images/characters/dn.png'
    elif skin_name == 'kitty':
        character.source = 'images/characters/kitty.png'
        description.source = 'images/characters/dn.png'
    elif skin_name == 'gim':
        character.source = 'images/characters/gim.png'
        description.source = 'images/characters/dn.png'
    elif skin_name == 'gun':
        character.source = 'images/characters/gun.png'
        description.source = 'images/characters/dn.png'
    confirm_button.pos_hint = {'x': .7, 'y': .01}
    confirm_button.disabled = 0






