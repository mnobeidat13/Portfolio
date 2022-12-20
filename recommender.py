from flet import *
import flet as ft
import settings

def get_recommender_page():

    device = settings.device
    view_padding = settings.view_padding
    view_horizontal_alignment = settings.view_horizontal_alignment
    navigation_bar = settings.navigation_bar
    text_width = settings.page.width - 4 * settings.page.padding

    title = Text('H&M Fashion Recommender System', weight='w800', size=28, width=text_width)
    body = Text('This is a demo that show the results of different recommendation models which is part of my work on H&M personalized-fashion-recommendations hosted on Kaggle.com',
                 weight='w400', size=22, width=text_width)


    body2 = Text('Code can be found on my Kaggle profile', weight='w500', size=22, width=text_width)



    competition_button = ElevatedButton(content=Text('Competiton Link', size=20, weight='w400'),
                         on_click=lambda e: settings.page.launch_url('https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations'))
    profile_button = ElevatedButton(content=Text('Kaggle Profile', size=20, weight='w400'),
                         on_click=lambda e: settings.page.launch_url('https://www.kaggle.com/mohammedobeidat/code'))


    button = ElevatedButton(content=Text('See It In Action', size=24, weight='w600'), on_click=lambda e: settings.page.go('/item_recommendation'))

    content_column = Column([title, body, competition_button, body2, profile_button], alignment='center', scroll='hidden', spacing=10, expand=False, wrap=True)

    if device in ['android', 'ios']:
        view = View("/recommender", [content_column, navigation_bar], padding=view_padding, horizontal_alignment=view_horizontal_alignment)
    elif device in ['windows', 'macos', 'linux']:
        view = View("/recommender", [Row([navigation_bar, content_column], expand=True)], padding=view_padding, horizontal_alignment=view_horizontal_alignment)

    view.controls.append(settings.back_button)
    view.controls.append(Divider(thickness=1))
    view.controls.append(button)
    # print(view.controls)
    return view