from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.video import Video
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import pyautogui
import sys
sys.path.append('modules')
import set_skin
import show_presplash
import key_press_events
import mainloop
import actions_with_objects
import play_music

screen_width, screen_height = pyautogui.size()
Window.size = (screen_width, screen_height)
Window.borderless = False



class seabattleApp(App):
    def build(self):
        self.move_bg_x = 0
        self.move_bg_y = 0


        Clock.schedule_interval(self.update_pos_mainloop, 0.01)

        Window.bind(on_key_down=self.on_key_down)
        Window.bind(on_key_up=self.on_key_up)
        self.main_layout = FloatLayout()
        self.nothing_image = Image(source='images/background/additional/nothing.png',
                                    size_hint=(.2, .7),
                                    pos_hint={'x': .35, 'y': .2},
                                    allow_stretch = True,
                                    keep_ratio = False)
        self.main_character = Image(source='images/characters/ghost.png',
                                    size_hint=(None, None),
                                    size=(Window.width/5, Window.height/2),
                                    pos=(Window.width/2.5, 0),
                                    allow_stretch = True,
                                    keep_ratio = False)
        self.monya_presplash_video = Video(source='videos/monya_presplash.mp4',
                                          state='pause',
                                          volume=0,
                                          allow_stretch=True,
                                          keep_ratio=False,
                                          size_hint=(1, 1),
                                          pos_hint={'x': 0, 'y': 0})
        self.story_vid_1 = Video(source='videos/story/story_vid_1.mp4',
                                          state='pause',
                                          volume=1,
                                          allow_stretch=True,
                                          keep_ratio=False,
                                          size_hint=(1, 1),
                                          pos_hint={'x': 0, 'y': 0})
        self.monya_presplash_video.bind(eos=self.on_monya_presplash_video_end)
        self.story_vid_1.bind(eos=self.on_story_vid_1_end)




        #========= choose skin screen =======
        self.choose_skin_screen = FloatLayout()
        self.choose_skin_screen_boxlayout = BoxLayout(orientation='vertical',
                                                      spacing=10,
                                                      size_hint=(1, .5),
                                                      pos_hint={'x': 0, 'y': 0})
        self.choose_skin_screen_scrollview = ScrollView(size_hint=(.15, .6),
                                                        pos_hint={'x': .8, 'y': .12})
        self.choose_skin_screen_background = Image(source='images/background/choose_skin/skin_page_bg.png',
                                                    size_hint=(1, 1),
                                                    pos_hint={'x': 0, 'y': 0},
                                                    allow_stretch = True,
                                                    keep_ratio = False)
        self.choose_skin_screen_choose_skin_text = Image(source='images/background/choose_skin/text_on_coose_skin.png',
                                                    size_hint=(.3, .1),
                                                    pos_hint={'x': .7, 'y': .9},
                                                    allow_stretch = True,
                                                    keep_ratio = False)
        self.choose_skin_screen_choose_skin_text_3 = Image(source='images/background/choose_skin/text_on_coose_skin_3.png',
                                                    size_hint=(.2, .1),
                                                    pos_hint={'x': .05, 'y': .8},
                                                    allow_stretch = True,
                                                    keep_ratio = False)
        self.choose_skin_screen_description = Image(source='images/characters/d1.png',
                                                    size_hint=(.18, .25),
                                                    pos_hint={'x': .07, 'y': .52},
                                                    allow_stretch = True,
                                                    keep_ratio = False)
        self.choose_skin_screen_confirm_button = Button(background_normal='images/background/choose_skin/text_on_coose_skin_2.png',
                                                        size_hint=(.3, .1),
                                                        pos_hint={'x': 2, 'y': .01},
                                                        disabled = 1,
                                                        on_release = self.go_to_in_home_screen)
        self.choose_skin_screen.add_widget(self.choose_skin_screen_background)
        self.choose_skin_screen.add_widget(self.choose_skin_screen_scrollview)
        self.choose_skin_screen.add_widget(self.choose_skin_screen_choose_skin_text)
        self.choose_skin_screen.add_widget(self.choose_skin_screen_confirm_button)
        self.choose_skin_screen.add_widget(self.choose_skin_screen_choose_skin_text_3)
        self.choose_skin_screen.add_widget(self.choose_skin_screen_description)
        self.choose_skin_screen_scrollview.add_widget(self.choose_skin_screen_boxlayout)
        self.choose_skin_screen.add_widget(self.main_character)
        for card_id in ['sigma', 'rekardo', 'kitty', 'gim', 'gun']:
            self.choose_skin_screen_card_button = Button(text=card_id,
                                                    background_normal='images/background/choose_skin/card.png',
                                                    color = (0, 0, 1, 1),
                                                    font_size = 20,
                                                    size_hint=(1, 1),
                                                    on_release = self.choose_skin)
            self.choose_skin_screen_boxlayout.add_widget(self.choose_skin_screen_card_button)
        #====================================

        # ============ login screen ==========
        self.login_screen = FloatLayout()
        self.login_screen_email_textinput = TextInput(hint_text ='email...',
                                                    font_size = 30,
                                                    size_hint=(.4, .1),
                                                    pos_hint={'x': .3, 'y': .6},
                                                    background_color=(1, .7, .6, 1),
                                                    foreground_color=(0, 0, 0, 1),
                                                    cursor_color=(0, 0, 0, 1),
                                                    multiline=False)
        self.login_screen_password_textinput = TextInput(hint_text ='password...',
                                                    font_size = 30,
                                                    size_hint=(.4, .1),
                                                    pos_hint={'x': .3, 'y': .45},
                                                    background_color=(1, .7, .6, 1),
                                                    foreground_color=(0, 0, 0, 1),
                                                    cursor_color=(0, 0, 0, 1),
                                                    multiline=False)
        self.login_screen_register_button = Button(text = "don't have an account ? register here >",
                                                    font_size=15,
                                                    size_hint=(.3, .05),
                                                    pos_hint={'x': .4, 'y': .38},
                                                    on_release = self.go_to_register_screen)
        self.login_screen_continue_button = Button(text = "continue >",
                                                    font_size=30,
                                                    size_hint=(.2, .1),
                                                    pos_hint={'x': .8, 'y': .01},
                                                    on_release = self.on_monya_presplash_video_start)
        self.login_screen.add_widget(self.login_screen_email_textinput)
        self.login_screen.add_widget(self.login_screen_password_textinput)
        self.login_screen.add_widget(self.login_screen_register_button)
        self.login_screen.add_widget(self.login_screen_continue_button)
        # ====================================

        # ============ register screen ==========
        self.register_screen = FloatLayout()
        self.register_screen_email_textinput = TextInput(hint_text ='email...',
                                                    font_size = 30,
                                                    size_hint=(.4, .1),
                                                    pos_hint={'x': .3, 'y': .6},
                                                    background_color=(1, .7, .6, 1),
                                                    foreground_color=(0, 0, 0, 1),
                                                    cursor_color=(0, 0, 0, 1),
                                                    multiline=False)
        self.register_screen_password_textinput = TextInput(hint_text ='password...',
                                                    font_size = 30,
                                                    size_hint=(.4, .1),
                                                    pos_hint={'x': .3, 'y': .45},
                                                    background_color=(1, .7, .6, 1),
                                                    foreground_color=(0, 0, 0, 1),
                                                    cursor_color=(0, 0, 0, 1),
                                                    multiline=False)
        self.register_screen_password_confirm_textinput = TextInput(hint_text ='confirm password...',
                                                    font_size = 30,
                                                    size_hint=(.4, .1),
                                                    pos_hint={'x': .3, 'y': .3},
                                                    background_color=(1, .7, .6, 1),
                                                    foreground_color=(0, 0, 0, 1),
                                                    cursor_color=(0, 0, 0, 1),
                                                    multiline=False)
        self.register_screen_continue_button = Button(text = "continue >",
                                                    font_size=30,
                                                    size_hint=(.2, .1),
                                                    pos_hint={'x': .8, 'y': .01},
                                                    on_release = self.go_to_login_screen)
        self.register_screen.add_widget(self.register_screen_email_textinput)
        self.register_screen.add_widget(self.register_screen_password_textinput)
        self.register_screen.add_widget(self.register_screen_password_confirm_textinput)
        self.register_screen.add_widget(self.register_screen_continue_button)
        # ====================================

        # ======== in home screen ===========
        self.in_house_screen = FloatLayout()
        self.in_house_screen_interior_laout = FloatLayout(size_hint=(None, None),
                                                          size = (Window.width*4, Window.height),
                                                          pos = (-(Window.width/1.5), 0))
        self.in_house_screen_outside_the_window_img = Image(source='images/background/home/outside_the_window.png',
                                            size_hint=(1, 1),
                                            pos_hint={'x': 0, 'y': 0},
                                            allow_stretch = True,
                                            keep_ratio = False)
        self.in_house_screen_house_background_img = Image(source='images/background/home/home_inside.png',
                                            size_hint=(1, 1),
                                            pos_hint={'x': 0, 'y': 0},
                                            allow_stretch = True,
                                            keep_ratio = False)
        self.in_house_screen_door_img = Image(source='images/background/home/home_inside_door.png',
                                            size_hint=(.07, .65),
                                            pos_hint={'x': .11, 'y': .18},
                                            allow_stretch = True,
                                            keep_ratio = False)
        self.in_house_screen_vinyl_img = Image(source='images/background/home/vinyl.png',
                                            size_hint=(.05, .35),
                                            pos_hint={'x': .72, 'y': .15},
                                            allow_stretch = True,
                                            keep_ratio = False)
        self.in_house_screen_heater_img = Image(source='images/background/home/heater.png',
                                            size_hint=(.1, .88),
                                            pos_hint={'x': .45, 'y': .12},
                                            allow_stretch = True,
                                            keep_ratio = False)
        self.in_house_screen_bed_img = Image(source='images/background/home/bed.png',
                                            size_hint=(.1, .2),
                                            pos_hint={'x': .78, 'y': .15},
                                            allow_stretch = True,
                                            keep_ratio = False)
        self.in_house_screen_chest_img = Image(source='images/background/home/сhest.png',
                                            size_hint=(.02, .2),
                                            pos_hint={'x': .9, 'y': .15},
                                            allow_stretch = True,
                                            keep_ratio = False)
        self.in_house_screen_chair_img = Image(source='images/background/home/chair.png',
                                               size_hint=(.04, .4),
                                               pos_hint={'x': .6, 'y': .08},
                                               allow_stretch=True,
                                               keep_ratio=False)
        self.in_house_screen_exit_house_button = Button(text = 'exit',
                                                    font_size=15,
                                                    size_hint=(.05, .04),
                                                    pos_hint={'x': .12, 'y': .75},
                                                    on_release = self.exit_house)
        self.in_house_screen_play_vinyl_button = Button(text = 'play music',
                                                    font_size=15,
                                                    size_hint=(.05, .04),
                                                    pos_hint={'x': self.in_house_screen_vinyl_img.pos_hint['x'], 'y': .65},
                                                    on_release = self.play_vinyl)
        self.in_house_screen_stop_vinyl_button = Button(text = 'stop music',
                                                    font_size=15,
                                                    size_hint=(.05, .04),
                                                    pos_hint={'x': self.in_house_screen_vinyl_img.pos_hint['x'], 'y': .6},
                                                    disabled = 1,
                                                    on_release = self.stop_vinyl)
        self.in_house_screen_interior_laout.add_widget(self.in_house_screen_outside_the_window_img)
        self.in_house_screen_interior_laout.add_widget(self.in_house_screen_house_background_img)
        self.in_house_screen_interior_laout.add_widget(self.in_house_screen_door_img)
        self.in_house_screen_interior_laout.add_widget(self.in_house_screen_vinyl_img)
        self.in_house_screen_interior_laout.add_widget(self.in_house_screen_heater_img)
        self.in_house_screen_interior_laout.add_widget(self.in_house_screen_bed_img)
        self.in_house_screen_interior_laout.add_widget(self.in_house_screen_chest_img)
        self.in_house_screen_interior_laout.add_widget(self.in_house_screen_chair_img)
        #self.in_house_screen_interior_laout.add_widget(self.in_house_screen_exit_house_button)
        self.in_house_screen.add_widget(self.in_house_screen_interior_laout)
        # ====================================



        # ======== taverna screen ============
        self.taverna_screen = FloatLayout()
        self.taverna_screen_interior_layout = FloatLayout(size_hint=(None, None),
                                                          size = (Window.width*4, Window.height),
                                                          pos = (-(Window.width/1.5), 0))
        self.taverna_screen_interior_img = Image(source='images/background/taverna/interior.png',
                                                 size_hint=(1, 1),
                                                 pos_hint={'x': 0, 'y': 0},
                                                 allow_stretch = True,
                                                 keep_ratio = False)
        self.taverna_screen_outside_the_window_img = Image(source='images/background/taverna/outside_the_window.png',
                                                 size_hint=(1, 1),
                                                 pos_hint={'x': 0, 'y': 0},
                                                 allow_stretch = True,
                                                 keep_ratio = False)
        self.taverna_screen_posters_img = Image(source='images/background/taverna/posters.png',
                                                 size_hint=(1, 1),
                                                 pos_hint={'x': 0, 'y': 0},
                                                 allow_stretch = True,
                                                 keep_ratio = False)
        self.taverna_screen_door_img = Image(source='images/background/taverna/door.png',
                                             size_hint=(.1, .65),
                                             pos_hint={'x': .35, 'y': .12},
                                             allow_stretch = True,
                                             keep_ratio = False)
        self.taverna_screen_piano_img = Image(source='images/background/taverna/piano.png',
                                             size_hint=(.08, .45),
                                             pos_hint={'x': .05, 'y': .12},
                                             allow_stretch = True,
                                             keep_ratio = False)
        self.taverna_screen_table_img = Image(source='images/background/taverna/table.png',
                                             size_hint=(.05, .3),
                                             pos_hint={'x': .2, 'y': .12},
                                             allow_stretch = True,
                                             keep_ratio = False)
        self.taverna_screen_chair_img = Image(source='images/background/taverna/chair.png',
                                             size_hint=(.02, .12),
                                             pos_hint={'x': .25, 'y': .12},
                                             allow_stretch = True,
                                             keep_ratio = False)
        self.taverna_screen_silver_bar_stol_img = Image(source='images/background/taverna/silver_bar_stol.png',
                                             size_hint=(.08, .4),
                                             pos_hint={'x': .82, 'y': .1},
                                             allow_stretch = True,
                                             keep_ratio = False)
        self.taverna_screen_bochkas_img = Image(source='images/background/taverna/bochkas.png',
                                             size_hint=(.05, .12),
                                             pos_hint={'x': .82, 'y': .75},
                                             allow_stretch = True,
                                             keep_ratio = False)
        self.taverna_screen_basement_door_img = Image(source='images/background/taverna/basement_door.png',
                                             size_hint=(.06, .75),
                                             pos_hint={'x': .92, 'y': .12},
                                             allow_stretch = True,
                                             keep_ratio = False)
        self.taverna_screen_exit_taverna_button = Button(text ='exit_taverna',
                                                         font_size=15,
                                                         size_hint=(.05, .04),
                                                         pos_hint={'x': float(self.taverna_screen_door_img.pos_hint['x']), 'y': .5},
                                                         on_release = self.exit_taverna)
        self.taverna_screen_interior_layout.add_widget(self.taverna_screen_outside_the_window_img)
        self.taverna_screen_interior_layout.add_widget(self.taverna_screen_interior_img)
        self.taverna_screen_interior_layout.add_widget(self.taverna_screen_posters_img)
        self.taverna_screen_interior_layout.add_widget(self.taverna_screen_door_img)
        self.taverna_screen_interior_layout.add_widget(self.taverna_screen_piano_img)
        self.taverna_screen_interior_layout.add_widget(self.taverna_screen_table_img)
        self.taverna_screen_interior_layout.add_widget(self.taverna_screen_chair_img)
        self.taverna_screen_interior_layout.add_widget(self.taverna_screen_silver_bar_stol_img)
        self.taverna_screen_interior_layout.add_widget(self.taverna_screen_bochkas_img)
        self.taverna_screen_interior_layout.add_widget(self.taverna_screen_basement_door_img)
        self.taverna_screen_interior_layout.add_widget(self.taverna_screen_exit_taverna_button)
        self.taverna_screen.add_widget(self.taverna_screen_interior_layout)
        # ====================================



        # ======== main map screen ===========
        self.main_map_screen = FloatLayout()
        self.main_map_screen_map_layout =  FloatLayout(size_hint=(None, None),
                                              size = (Window.width*10, Window.height*10),
                                              pos = (-(Window.width*1.5), -(Window.height*1)))
        self.main_map_screen_map_background_img = Image(source='images/background/maps/main_map.png',
                                            size_hint=(1, 1),
                                            pos_hint={'x': 0, 'y': 0},
                                            allow_stretch = True,
                                            keep_ratio = False)
        self.main_map_screen_home_img = Image(source='images/background/houses/home.png',
                                               size_hint=(.1, .15),
                                               pos_hint={'x': .1, 'y': .12},
                                               allow_stretch=True,
                                               keep_ratio=False)
        self.main_map_screen_taverna_img = Image(source='images/background/houses/taverna.png',
                                                 size_hint=(.1, .15),
                                                 pos_hint={'x': .1, 'y': .7},
                                                 allow_stretch=True,
                                                 keep_ratio=False)
        self.main_map_screen_enter_home_btn = Button(text = 'enter_house',
                                                    font_size=15,
                                                    size_hint=(.01, .01),
                                                    pos_hint={'x': self.main_map_screen_home_img.pos_hint['x']+0.09, 'y': self.main_map_screen_home_img.pos_hint['y']+0.05},
                                                    on_release = self.enter_home)
        self.main_map_screen_enter_taverna_btn = Button(text ='enter_taverna',
                                                        font_size=15,
                                                        size_hint=(.01, .01),
                                                        pos_hint={'x': self.main_map_screen_taverna_img.pos_hint['x'] + 0.09, 'y': self.main_map_screen_taverna_img.pos_hint['y'] + 0.05},
                                                        on_release = self.enter_taverna)
        self.main_map_screen_map_layout.add_widget(self.main_map_screen_map_background_img)
        self.main_map_screen_map_layout.add_widget(self.main_map_screen_home_img)
        self.main_map_screen_map_layout.add_widget(self.main_map_screen_taverna_img)
        #self.main_map_screen_map_layout.add_widget(self.main_map_screen_enter_home_btn)

        self.main_map_screen.add_widget(self.main_map_screen_map_layout)

        # ====================================

        self.list_with_objects = [
            self.in_house_screen_door_img,
            self.in_house_screen_vinyl_img
        ]
        self.list_with_buttons_to_place = [
            self.in_house_screen_exit_house_button,
            self.in_house_screen_play_vinyl_button,
            self.in_house_screen_stop_vinyl_button
        ]
        

        self.list_with_objects_3d = [
            self.main_map_screen_home_img,
            self.main_map_screen_taverna_img
        ]
        self.list_with_buttons_to_place_3d = [
            self.main_map_screen_enter_home_btn,
            self.main_map_screen_enter_taverna_btn
        ]









        self.current_map_name = 'none'
        self.current_map = self.in_house_screen_interior_laout


        self.main_layout.add_widget(self.choose_skin_screen)
        #self.main_layout.add_widget(self.taverna_screen)
        #self.main_layout.add_widget(self.login_screen)
        #self.main_layout.add_widget(self.register_screen)
        #self.main_layout.add_widget(self.in_house_screen)
        return self.main_layout





    def choose_skin(self, instance):
        set_skin.set(self.main_character,
                     instance.text,
                     self.choose_skin_screen_description,
                     self.choose_skin_screen_confirm_button)
    def go_to_register_screen(self, instance):
        self.main_layout.remove_widget(self.login_screen)
        self.main_layout.add_widget(self.register_screen)
    def go_to_login_screen(self, instance):
        self.main_layout.remove_widget(self.register_screen)
        self.main_layout.add_widget(self.login_screen)
    def on_monya_presplash_video_start(self, instance):
        show_presplash.show(self.main_layout, self.login_screen, self.monya_presplash_video)
    def on_monya_presplash_video_end(self, instance, value):
        show_presplash.stop(self.main_layout, self.nothing_image, self.monya_presplash_video)
        self.main_layout.remove_widget(self.nothing_image)
        show_presplash.show(self.main_layout, self.monya_presplash_video, self.story_vid_1)
    def on_story_vid_1_end(self, instance, value):
        show_presplash.stop(self.main_layout, self.choose_skin_screen, self.story_vid_1)
    def go_to_in_home_screen(self, instance):
        self.main_layout.remove_widget(self.choose_skin_screen)
        self.main_layout.add_widget(self.in_house_screen)
        self.choose_skin_screen.remove_widget(self.main_character)
        self.in_house_screen.add_widget(self.main_character)
        self.current_map_name = 'home'
    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        self.move_bg_x = key_press_events.move(text)[0]
        self.move_bg_y = key_press_events.move(text)[1]
    def on_key_up(self, key, scancode, codepoint):
        self.move_bg_x = key_press_events.stop_moving()[0]
        self.move_bg_y = key_press_events.stop_moving()[1]
    def exit_house(self, instance):
        self.main_layout.remove_widget(self.in_house_screen)
        self.main_layout.add_widget(self.main_map_screen)
        self.in_house_screen.remove_widget(self.main_character)
        self.main_map_screen.add_widget(self.main_character)
        self.current_map = self.main_map_screen_map_layout
        self.current_map_name = 'main_map'
        self.main_character.pos = (Window.width/2, Window.height/3)
        self.stop_vinyl(1)
    def play_vinyl(self, instance):
        self.in_house_screen_play_vinyl_button.disabled = 1
        self.in_house_screen_stop_vinyl_button.disabled = 0
        play_music.music_play('sound/music_for_vinyl/povodir.ogg')
    def stop_vinyl(self, instance):
        self.in_house_screen_play_vinyl_button.disabled = 0
        self.in_house_screen_stop_vinyl_button.disabled = 1
        play_music.music_stop()
    def enter_home(self, instance):
        self.main_layout.remove_widget(self.main_map_screen)
        self.main_layout.add_widget(self.in_house_screen)
        self.main_map_screen.remove_widget(self.main_character)
        self.in_house_screen.add_widget(self.main_character)
        self.current_map = self.in_house_screen_interior_laout
        self.main_character.pos =(Window.width/2, 0)
        self.current_map_name = 'home'
        self.list_with_objects = [
            self.in_house_screen_door_img,
            self.in_house_screen_vinyl_img
        ]
        self.list_with_buttons_to_place = [
            self.in_house_screen_exit_house_button,
            self.in_house_screen_play_vinyl_button,
            self.in_house_screen_stop_vinyl_button
        ]
    def enter_taverna(self, instance):
        self.main_layout.remove_widget(self.main_map_screen)
        self.main_layout.add_widget(self.taverna_screen)
        self.main_map_screen.remove_widget(self.main_character)
        self.taverna_screen.add_widget(self.main_character)
        self.current_map = self.taverna_screen_interior_layout
        self.main_character.pos =(Window.width/2, 0)
        self.current_map_name = 'taverna'
        self.list_with_objects = [
            self.taverna_screen_door_img
        ]
        self.list_with_buttons_to_place = [
            self.taverna_screen_exit_taverna_button
        ]
    def exit_taverna(self, instance):
        self.main_layout.remove_widget(self.taverna_screen)
        self.main_layout.add_widget(self.main_map_screen)
        self.taverna_screen.remove_widget(self.main_character)
        self.main_map_screen.add_widget(self.main_character)
        self.current_map = self.main_map_screen_map_layout
        self.current_map_name = 'main_map'
        self.main_character.pos = (Window.width/2, Window.height/3)
















    def update_pos_mainloop(self, instance):
        mainloop.update_pos(self.current_map_name, self.current_map, self.main_character, self.move_bg_x, self.move_bg_y, Window.width, Window.height)
        actions_with_objects.update(self.current_map_name, self.current_map, self.main_character, self.list_with_buttons_to_place, self.list_with_objects, self.list_with_buttons_to_place_3d, self.list_with_objects_3d)



seabattleApp().run()


























