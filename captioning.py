from funcs import *
from flet import *
import flet as ft
import numpy as np
import settings

### Read data

df = pd.read_csv('https://raw.githubusercontent.com/mnobeidat13/HandM-update/main/caption_desc_embeds.csv', dtype={'id':str}).drop('Unnamed: 0', axis=1)


def get_captioning_view():

    ## get image from github
    def get_item_image(image):
        return f'https://raw.githubusercontent.com/mnobeidat13/HandM-update/main/results/images/{image}.jpeg'



    def get_item(e):

        item = df.sample(1)
        item_id = item.id.iloc[0][1:]
        desc = item.desc.iloc[0]
        desc = ' '.join(desc.split(' ')[:10])
        caption = item.caption.iloc[0].capitalize()

        card = Card(content=Container(content=Column([
                                                    Text(f'True Label: {desc}', weight='w400'),
                                                    Text(f'Predicted Label: {caption}', weight='w500'),
                                                    Image(src=get_item_image(item_id), border_radius=ft.border_radius.all(40), height=300, width=300),
                                                    ],horizontal_alignment='center'), padding=10, width=400, height=430))
        content_container.content = card
        content_container.update()


    new_button = Row([ElevatedButton("Get An Item", on_click=get_item)], alignment='center')

    header = Row([Text('An Implementaion of A Transformer Model Which Generates Verbal Description of An Item', weight='w500', width=350)], alignment='center', vertical_alignment='center')

    content_container = Container()

    view = View('/product_tagging', vertical_alignment='center',  horizontal_alignment='center')
    view.controls.append(header)
    view.controls.append(new_button)
    view.controls.append(Divider(thickness=2))
    view.controls.append(content_container)
    recommender_navigation_bar = settings.recommender_navigation_bar
    view.controls.append(recommender_navigation_bar)
    view.controls.append(settings.back_button)
    return view
