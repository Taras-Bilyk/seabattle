from kivy.core.audio import SoundLoader

def music_play(file):
    global music_m
    music_m = SoundLoader.load(file)
    music_m.volume = 1
    music_m.loop = True
    music_m.play()

def music_stop():
    try:
        music_m.stop()
    except Exception:
        pass




