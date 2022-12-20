from flet import *
import flet as ft
import settings
import pickle
import pandas as pd
import numpy as np


def get_car_price_page():

    page = settings.page
    device = settings.device
    view_padding = settings.view_padding
    view_horizontal_alignment = settings.view_horizontal_alignment
    navigation_bar = settings.navigation_bar

    f = open('car_inference.pickle', 'rb')
    dict_ = pickle.load(f)

    brands = dict_['brands']
    sub_brands = dict_['sub_brands']
    sub_brand_weights = dict_['sub_brand_weights']
    colors = dict_['colors']
    specs = dict_['specs']
    y_scaler = dict_['y_scaler']
    pipe = dict_['pipe']

    def inference(brand, car_model, car_specs, year, milage, n_cylinder, color):
        model_weight = sub_brand_weights[f'{brand}_{car_model}']

        brand = pd.Categorical([brand], categories = brands)
        brand = pd.get_dummies(brand).values.flatten().tolist()

        car_specs = pd.Categorical([car_specs], categories = specs)
        car_specs = pd.get_dummies(car_specs).values.flatten().tolist()

        color = pd.Categorical([color], categories = colors)
        color = pd.get_dummies(color).values.flatten().tolist()

        test = [year, milage, n_cylinder, model_weight] + brand + car_specs + color
        test = np.array(test).flatten().reshape(1, -1)
        price = int(y_scaler.inverse_transform(pipe.predict(test).reshape(-1, 1)))

        return price

    def brand_on_change(e):
        brand_value = brand.value
        sub_brand.value = sorted(sub_brands[brand_value])[0]
        sub_brand.options = [ft.dropdown.Option(i) for i in sorted(sub_brands[brand_value])]
        sub_brand.disabled = False
        sub_brand.update()

    brand = Dropdown(label="Brand",hint_text="Choose Brand",options=[ft.dropdown.Option(i) for i in sorted(brands)], autofocus=True, on_change=brand_on_change)
    brand.value = 'BMW'
    sub_brand = Dropdown(label="Model",hint_text="Choose Model",options=[ft.dropdown.Option(i) for i in sorted(dict_['sub_brands']['BMW'])], autofocus=True)
    sub_brand.value = '320'

    car_specs = Dropdown(label="Specs",hint_text="Choose Specs",options=[ft.dropdown.Option(i) for i in sorted(specs)], autofocus=True)
    car_specs.value='GCC'

    year = TextField(label='Model Year', bgcolor=ft.colors.WHITE)
    year.value = 2011

    milage = TextField(label='Milage in KM')
    milage.value = 120000

    n_cylinder = TextField(label='Number of Cylinders')
    n_cylinder.value = 6

    color = Dropdown(label="Color",hint_text="Choose Color",options=[ft.dropdown.Option(i) for i in sorted(colors)], autofocus=True)
    color.value = 'White'

    label = Text(size=30, font_family="RobotoSlab", weight="w100", text_align='center')
    price_estimation = Text(size=30, font_family="RobotoSlab", weight="w100", text_align='center', width=200)

    def on_click(e):
        try:
            price = inference(brand.value, sub_brand.value, car_specs.value, year.value, milage.value, n_cylinder.value, color.value)
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

    title = Card(content=Container(content=Text("Used Car Price Estimation", size=30, font_family="Consolas"), padding=10))
    header = Text('Choose your car specs', size=24)

    col1 = Column([header, Column([brand, sub_brand, car_specs, year, milage, n_cylinder, color, button], scroll='hidden')], spacing=30)

    col2 = Column([Row([label], alignment='center'), Row([price_estimation], alignment='center')])#, horizontal_alignment='center')

    card = Card(content=Container(content=Row([col1, col2], wrap=True, width=500, ), padding=60))

    md1 = """
[**Link to Project on github**](https://github.com/mnobeidat13/Used-Car-Price-Estimation)
============
"""
    description = Column([title, Text('This is an implementation of a Random Forest model that estimates the price of a used car based on its specs.\nFollow the link for code and documentation',
                         width=300, size=22),
                         Markdown(md1, on_tap_link=lambda e: page.launch_url(e.data)),
                         ], spacing=20)


    column_content = Row([description, card], wrap=True, spacing=50)
    column = ft.Column([column_content], horizontal_alignment='center', expand=True, spacing=50, scroll='hidden')
    # view = View('/house_price', [Row([description, card], wrap=True, spacing=100)], vertical_alignment='start', horizontal_alignment='center', padding=20)

    divider = VerticalDivider(color='#3E665F', width=50, thickness=2)

    if device in ['android', 'ios']:
        view = View("/car_price", [Row([column], expand=True), navigation_bar], padding=view_padding, horizontal_alignment=view_horizontal_alignment)
    elif device in ['windows', 'macos', 'linux']:
        view = View("/car_price", [Row([navigation_bar, divider,column], expand=True)], padding=view_padding, horizontal_alignment=view_horizontal_alignment)

    view.controls.append(settings.back_button)

    return view