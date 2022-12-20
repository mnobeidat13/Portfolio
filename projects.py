
from flet import *
import flet as ft
import settings



def create_project_card(title, subtitle, image_link, overview_link=None, project_link=None, card_height=460):

    page = settings.page
    project_card = Container(ft.Card(content=ft.Container(
                            content=ft.Column([
                                ft.Image(src=image_link,width=500, height=300,fit="fitHeight", border_radius=ft.border_radius.all(40)),
                                ft.ListTile(title=ft.Text(title, max_lines=1),subtitle=ft.Text(subtitle, max_lines=3)),
                                ft.Row([TextButton("Overview", on_click=lambda e: page.go(overview_link)), ft.TextButton("Link To Code", on_click=lambda e: page.launch_url(project_link))],
                                alignment="center")]), width=500, padding=10, height=card_height)))
    return project_card

def get_projects_page():
    page = settings.page
    device = settings.device
    view_padding = settings.view_padding
    view_horizontal_alignment = settings.view_horizontal_alignment
    navigation_bar = settings.navigation_bar

    project_cards = []
    project_cards.append(create_project_card(title='H&M Fashion Recommender System',
                                             subtitle="A demo to illustrate a recommender system that uses four different techniques",
                                             image_link="https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/handm%20thumbnail.jpg",
                                             overview_link='/recommender',
                                             project_link='https://github.com/mnobeidat13/HandM-Recommender-System'))

    project_cards.append(create_project_card(title='Used Car Price Estimation',
                                            subtitle="A machine larning model that estimates the sale value of a used car sold in UAE",
                                            image_link="https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/used%20car.jpg",
                                            overview_link='/car_price',
                                            project_link='https://github.com/mnobeidat13/Used-Car-Price-Estimation'))

    project_cards.append(create_project_card(title='Residential Unit Price Estimation',
                                             subtitle="A machine learning model to predict the sale price of residential units in different locations in Dubai",
                                             image_link="https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/dubai%20thumbnail.jpg",
                                             overview_link='/house_price',
                                             project_link='https://github.com/mnobeidat13/Residential-Units-Price-Prediction',
                                             card_height=480))

    project_cards.append(create_project_card(title='Stock Market Prediction',
                                            subtitle="Using machine learning to predict stock prices based on technical and fundamental indicators",
                                            image_link="https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/bull%20bear.jpg",
                                            overview_link='/stock_market',
                                            project_link=None,
                                            card_height=480))

    column_content =  [Row(project_cards[i:i+2], scroll='hidden', spacing=60, wrap=True) for i in range(0, len(project_cards), 2)]
    projects_container = ft.Column(column_content, scroll='hidden', horizontal_alignment='center', expand=True, spacing=50)
    divider = VerticalDivider(color='#3E665F', width=100, thickness=2)

    if device in ['android', 'ios']:
        view = View("/projects", [Row([projects_container], expand=True), navigation_bar], padding=view_padding, horizontal_alignment=view_horizontal_alignment)
    elif device in ['windows', 'macos', 'linux']:
        view = View("/projects", [Row([navigation_bar, divider, projects_container], expand=True)], padding=view_padding, horizontal_alignment=view_horizontal_alignment)

    view.controls.append(settings.back_button)
    return view
