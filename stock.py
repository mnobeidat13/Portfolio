from flet import *
import flet as ft
import settings

def get_stock_market_page():

    page = settings.page
    device = settings.device
    view_padding = settings.view_padding
    view_horizontal_alignment = settings.view_horizontal_alignment
    navigation_bar = settings.navigation_bar


    # if device in ['android', 'ios']:
    #     view = View("/projects", [ElevatedButton('Home'), navigation_bar], padding=view_padding, horizontal_alignment=view_horizontal_alignment)
    # elif device in ['windows', 'macos', 'linux']:
    #     view = View("/projects", [Row([navigation_bar, ElevatedButton('Home')], expand=True)], padding=view_padding, horizontal_alignment=view_horizontal_alignment)
    view = View('/stock_market', horizontal_alignment='center', vertical_alignment='center')
    view.controls.append(settings.back_button)
    view.controls.append(Text('Still In Lab!', weight='w900', size=34))

    # print(view.controls)
    return view