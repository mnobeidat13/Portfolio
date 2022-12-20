from funcs import *
from flet import *
import flet as ft
import numpy as np
import settings

### Read data
df = pd.read_csv('https://raw.githubusercontent.com/mnobeidat13/HandM-update/main/product_tagging.csv', usecols=['article_id',	'label',	'prediction'])

def get_item_tagging_view():

    ## get image from github
    def get_item_image(image):
        return f'https://raw.githubusercontent.com/mnobeidat13/HandM-update/main/results/images/{image}.jpeg'


    def get_item(e):
        item = df.sample(1)
        if item.label.iloc[0] == item.prediction.iloc[0]:
            color = ft.colors.GREEN
        else:
            color = ft.colors.RED

        card = Card(content=Container(content=Column([
                                                    Text(f'True Label: {item.label.iloc[0]}', weight='w500'),
                                                    Text(f'Predicted Label: {item.prediction.iloc[0]}', color=color, weight='w500'),
                                                    Image(src=get_item_image(item.article_id.iloc[0]), border_radius=ft.border_radius.all(40), height=300, width=300),
                                                    ],horizontal_alignment='center'), padding=10, width=400, height=400))
        content_container.content = card
        content_container.update()


    new_button = Row([ElevatedButton("Get An Item", on_click=get_item)], alignment='center')

    header = Row([Text('An Implementaion of A CNN Model Which Tags Items', weight='w600')], alignment='center', vertical_alignment='center')

    content_container = Container()

    view = View('/product_tagging', vertical_alignment='center',  horizontal_alignment='center')
    view.controls.append(header)
    view.controls.append(new_button)
    view.controls.append(Divider(thickness=2))
    view.controls.append(content_container)
    view.controls.append(settings.recommender_navigation_bar)
    view.controls.append(settings.back_button)
    return view
