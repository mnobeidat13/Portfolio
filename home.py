from flet import *
import flet as ft
import settings

def get_home_page():

    page = settings.page
    device = settings.device
    view_padding = settings.view_padding
    view_horizontal_alignment = settings.view_horizontal_alignment
    navigation_bar = settings.navigation_bar

    color = '#3E665F'
    divider = VerticalDivider(color='#3E665F', width=100, thickness=2)

    title_size = 26
    title_weight = 'w800'

    subtitle_size = 22
    subtitle_weight = 'w600'

    text_size = 20
    text_weight = 'w400'

    text1 = Text('This is what I can do for you', size=30, weight='w600', color='#3E665F')

    text2 = Text('Dash-Boarding', size=title_size, weight=title_weight, color=color)
    text3 = Text('You need to see your data?', size=subtitle_size, weight=subtitle_weight)
    text4 = Text('I can help you with that. I can build a dashboard that summerizes your data and it can be made interactive or ran as stand alone web app using Plotly Dash',
                    size=text_size, weight=text_weight)

    text5 = Text('Data Analysis', size=title_size, weight=title_weight, color=color)
    text6 = Text('You need to understand your data?', size=subtitle_size, weight=subtitle_weight)
    text7 = Text('I can clean, transform and model your data to get valuable insights and help you make data driven decisions',
                    size=text_size, weight=text_weight)

    text8 = Text('Machine Learning', size=title_size, weight=title_weight, color=color)
    text9 = Text('You need to forecast demand or predict customer churn?', size=subtitle_size, weight=subtitle_weight)
    text10 = Text('Whether you have images, documents or a table, I can use it to build a predictive model that predicts your target. But remember, machine learning is not a magic wand, a good model needs good data',
                    size=text_size, weight=text_weight)

    def get_card(image_url, t1, t2, t3):

        row = Row([Image(src=image_url,height=90, width=90), t1])
        column = Column([row, t2, t3], spacing=5, expand=True)
        card = Container(content=column, padding=ft.padding.symmetric(vertical=20))

        return card

    card1 = get_card("https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/dasboard.jpeg", text2, text3, text4)
    card2 = get_card("https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/db.jpeg", text5, text6, text7)
    card3 = get_card("https://raw.githubusercontent.com/mnobeidat13/flet-resources/main/ml.jpeg", text8, text9, text10)

    column = Column([text1, card1, card2, card3], spacing=10, horizontal_alignment='start', expand=True, scroll='hidden')

    if device in ['android', 'ios']:
        view = View("/home1", [column, navigation_bar], padding=view_padding, horizontal_alignment=view_horizontal_alignment)
    elif device in ['windows', 'macos', 'linux']:
        view = View("/home1", [Row([navigation_bar, divider, column], expand=True)], padding=view_padding, horizontal_alignment=view_horizontal_alignment)

    view.controls.append(settings.back_button)
    return view