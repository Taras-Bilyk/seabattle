def show(main_layout, active_layout, video):
    main_layout.remove_widget(active_layout)
    main_layout.add_widget(video)
    video.state='play'
def stop(main_layout, active_layout, video):
    video.state = 'pause'
    main_layout.remove_widget(video)
    main_layout.add_widget(active_layout)




