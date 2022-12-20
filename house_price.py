from flet import *
import flet as ft
import settings
import pickle
import pandas as pd
import numpy as np




def get_house_price_page():
    page = settings.page
    device = settings.device
    view_padding = settings.view_padding
    view_horizontal_alignment = settings.view_horizontal_alignment
    navigation_bar = settings.navigation_bar

    f = open('house_inference.pickle', 'rb')
    dict_ = pickle.load(f)

    def inference(beds, baths, area, location):
        location = pd.Categorical([location], categories = dict_['regions'])
        location_dummy = pd.get_dummies(location).values.flatten().tolist()

        test = np.array([beds, baths, area] + location_dummy).reshape(1, -1)
        pipe = dict_['pipe']
        price = int(dict_['y_scaler'].inverse_transform(pipe.predict(test).reshape(-1, 1)))

        return price

    beds = TextField(label='Bedrooms', bgcolor=ft.colors.WHITE)
    baths = TextField(label='Baths')
    area = TextField(label='Area in SQR.M')
    location = Dropdown(label="Location",
                        hint_text="Choose Location",
                        options=[
                            ft.dropdown.Option(i) for i in sorted(dict_['regions'])
                        ], autofocus=True)

    beds.value = 2
    baths.value = 2
    area.value = 200
    location.value = 'Dubai Harbour'

    label = Text(size=30, font_family="RobotoSlab", weight="w100", text_align='center')
    price_estimation = Text(size=30, font_family="RobotoSlab", weight="w100", text_align='center', width=200)

    def on_click(e):
        try:
            price = inference(int(beds.value), int(baths.value), int(area.value), location.value)
            price_len = len(str(price)) - 2

            high = math.ceil(price / 10**price_len) * 10**price_len
            low = math.floor(price / 10**price_len) * 10**price_len

            label.value = 'Estimated Price'
            price_estimation.value = f'{low:,} - {high:,} AED'
            price_estimation.update()
            label.update()
        except Exception as e:
            print(e)
            pass

    button = Row([ElevatedButton(content=Column([Text('Go', size=24, text_align='center')], width=100, height=50, alignment='center', horizontal_alignment='center'), on_click=on_click)], alignment='center')

    title = Card(content=Container(content=Text("Residential Unit Price Estimation", size=30, font_family="Consolas"), padding=10))
    header = Text('Enter the number of bedrooms, bathrooms and area and choose your location', size=24)

    col1 = Column([header, baths, beds, area, location, button], spacing=30)

    col2 = Column([Row([label], alignment='center'), Row([price_estimation], alignment='center')])#, horizontal_alignment='center')

    card = Card(content=Container(content=Row([col1, col2], wrap=True, width=500, ), padding=60))

    md1 = """
[**Map**](https://mnobeidat.netlify.app)
============
"""
    md2 = """
[**Link to project on Github**](https://github.com/mnobeidat13/Residential-Units-Price-Prediction)
============
"""
    description = Column([title, Text('This is an implementation of a Random Forest model that estimates the price of a residential unit in 75 different locations in Dubai give the number of bedrooms and bathrroms it has, its area and location.\nClick on the link below to launch the map',
                         width=300, size=22),
                         Markdown(md1, on_tap_link=lambda e: global_page.launch_url(e.data)),
                         Markdown(md2, on_tap_link=lambda e: global_page.launch_url(e.data)),
                         Image(src='https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/houses%20thumbnail.png', width=300, height=300)
                         ], spacing=20)


    column_content = Row([description, card], wrap=True, spacing=50)
    column = ft.Column([column_content], scroll='hidden', horizontal_alignment='center', expand=True, spacing=50)
    # view = View('/house_price', [Row([description, card], wrap=True, spacing=100)], vertical_alignment='start', horizontal_alignment='center', padding=20)

    divider = VerticalDivider(color='#3E665F', width=10, thickness=2)

    if device in ['android', 'ios']:
        view = View("/house_price", [Row([column], expand=True), navigation_bar], padding=view_padding, horizontal_alignment=view_horizontal_alignment)
    elif device in ['windows', 'macos', 'linux']:
        view = View("/house_price", [Row([navigation_bar, divider, column], expand=True)], padding=view_padding, horizontal_alignment=view_horizontal_alignment)

    view.controls.append(settings.back_button)

    return view
