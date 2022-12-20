import settings
from flet import *
import flet as ft

def get_navigation_bar():

    page = settings.page
    device = settings.device
    view_padding = settings.view_padding
    view_horizontal_alignment = settings.view_horizontal_alignment
    navigation_bar = settings.navigation_bar

    dist_text_size = 18

    a1 = CircleAvatar(foreground_image_url="https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/graycut.jpg", radius=60, content=Text("Picture"),)

    if device in ['android', 'ios']:
        navigation_bar = ft.NavigationBar(destinations=[ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                                                        ft.NavigationDestination(icon=ft.icons.DOCUMENT_SCANNER, label="Resume"),
                                                        ft.NavigationDestination(icon=ft.icons.WORK_ROUNDED, label="Projects"),
                                                        ft.NavigationDestination(icon=ft.icons.CONTACTS, label="Contact")])
        destinations = {0:'/home1', 1:'/resume', 2:'/projects', 3:'/contacts'}

        navigation_bar.on_change = lambda e: page.go(destinations[navigation_bar.selected_index])

    elif device in ['windows', 'macos', 'linux']:
        navigation_bar = Row([Container(content=Column([
                        a1,
                        Text('M. Obeidat', size=24, weight='bold'),
                        TextButton(content=Text('Home', size=dist_text_size, weight='w500'),  on_click=lambda e: page.go('/home1')),
                        TextButton(content=Text('Resume', size=dist_text_size, weight='w500'), on_click=lambda e: page.go('/resume')),
                        TextButton(content=Text('Projects', size=dist_text_size, weight='w500'),  on_click=lambda e: page.go('/projects')),
                        TextButton(content=Text('Contacts', size=dist_text_size, weight='w500'),  on_click=lambda e: page.go('/contacts')),], scroll=False,
                        alignment="center", horizontal_alignment='center', spacing=50, width=170),
                        bgcolor="#E6F1EE",
                        border_radius=ft.border_radius.all(20))], spacing=30)

    return navigation_bar

def get_recommender_navigation_bar():

    page = settings.page
    device = settings.device

    navigation_bar = ft.NavigationBar(destinations=[    ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG, label="Item"),
                                                        ft.NavigationDestination(icon=ft.icons.PERSON, label="Customer"),
                                                        ft.NavigationDestination(icon=ft.icons.CHECK, label="Tagging"),
                                                        ft.NavigationDestination(icon=ft.icons.ARTICLE, label="Captioning"),
                                                        ft.NavigationDestination(icon=ft.icons.HOME, label="Home")])
    destinations = {0:'/item_recommendation', 1:'/customer_recommendation', 2:'/product_tagging', 3:'/captioning', 4:'/home1'}

    navigation_bar.on_change = lambda e: page.go(destinations[navigation_bar.selected_index])

    return navigation_bar