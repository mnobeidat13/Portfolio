from flet import *
import flet as ft
import settings

def get_landing_page():

    page = settings.page
    device = settings.device
    view_padding = settings.view_padding
    view_horizontal_alignment = settings.view_horizontal_alignment
    navigation_bar = settings.navigation_bar

    ## Mobile

    if device in ['android', 'ios']:
        container = Container(image_src='https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/landing.gif',
                         width=settings.page.width, height=settings.page.height, image_fit='fitWidth', bgcolor='#0D0D0D')

        container.alignment = ft.alignment.Alignment(0, 0.5)

        home_button = ElevatedButton(color='white', on_click=lambda e: page.go('/home1'), bgcolor='#3E665F', elevation=10)
        text = Text('Enter', size=24, font_family='Consolas',  color='white')
        icon = ft.Icon(name=ft.icons.LOGIN, color="white")
        row = Row([text, icon], width=90, spacing=5)
        home_button.content = row

        container.content = home_button

        view = View("/", [container], padding=view_padding, horizontal_alignment=view_horizontal_alignment)

    ## Desktop

    elif device in ['windows', 'macos', 'linux']:

        container = Container(image_src='https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/desktoplow.png',
                         width=settings.page.width, height=settings.page.height, image_fit='fitHeight', bgcolor='#0D0D0D')

        container.image_src = 'https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/LandingDesktop5.gif'

        container.alignment = ft.alignment.Alignment(-0.6, 0.7)

        home_button = ElevatedButton(color='white', on_click=lambda e: page.go('/home1'), bgcolor='#3E665F', elevation=10)
        text = Text('Enter', size=20, font_family='Consolas',  color='white')
        icon = ft.Icon(name=ft.icons.LOGIN, color="white")
        row = Row([text, icon], width=80, spacing=5)
        home_button.content = row

        container.content = home_button

        view = View("/", [Row([container], expand=True)], padding=50, horizontal_alignment=view_horizontal_alignment)

    view.padding = 0
    return view