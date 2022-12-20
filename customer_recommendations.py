from funcs import *
from flet import *
import flet as ft
import numpy as np
import settings

### Read data
articles_df = pd.read_csv('https://raw.githubusercontent.com/mnobeidat13/HandM-Recommender-System/main/articles.csv')

titles = ['Similar items based on image embeddings',
            'Similar items based on text embeddings',
            'Similar items based discriptive features',
            'Similar items based on embeddings from TensorFlow Recommendrs model',
            'Similar items based on a combination of all embeddings']
subtitles = ['Image embeddings are calculated using VGG16 CNN from Keras',
                'Text description embeddings are calculated using "universal-sentence-encoder" from TensorFlow Hub',
                'Features embeddings are calculated by one-hot encoding the descriptive features provided by H&M',
                'TFRS model performes a collaborative filtering based ranking using a neural network',
                'A concatenation of all embeddings above is used to find similar items']

customers_rcmnds = pd.read_csv('https://raw.githubusercontent.com/mnobeidat13/HandM-Recommender-System/main/results/customers_rcmnds.csv')

df = customers_rcmnds[['customer', 'history']].drop_duplicates()
df = df[df['history'].map(eval).map(len) >= 8]

customers_rcmnds = customers_rcmnds[customers_rcmnds.customer.isin(df.customer)]
customers = customers_rcmnds.customer.unique()

def get_customer_recommendations_view():


    def get_random_customer():
        customer = np.random.choice(customers)
        customer_data = customers_rcmnds[customers_rcmnds.customer == customer]
        customer_history = np.array(eval(customer_data.history.iloc[0]))

        image_rcmnds, text_rcmnds, feature_rcmnds, tfrs_rcmnds, combined_rcmnds = get_rcmnds(customer_data)
        detail_descs  = get_rcmnds_desc(articles_df, image_rcmnds, text_rcmnds, feature_rcmnds, tfrs_rcmnds, combined_rcmnds)

        rcmnds = (image_rcmnds, text_rcmnds, feature_rcmnds, tfrs_rcmnds, combined_rcmnds)

        return customer, customer_data, customer_history, detail_descs, rcmnds


    ## get image from github
    def get_item_image(image):
        return f'https://raw.githubusercontent.com/mnobeidat13/HandM-Recommender-System/main/results/images/{image}.jpeg'

    ## build rcmnds card
    def get_rcmnds_card(rcmnds, title, subtitle, avatar=True):


            grid_view = ft.GridView(expand=1, runs_count=5,max_extent=150,child_aspect_ratio=1.0,spacing=5,run_spacing=5, width=400)
            for image in rcmnds[1:7]:
                if avatar:
                    a1 = CircleAvatar(foreground_image_url=get_item_image(image), radius=30, content=Text(image),)
                    grid_view.controls.append(Container(content=a1, on_click=show_bottom_sheet))
                else:
                    image = ft.Image(src=get_item_image(image), border_radius=ft.border_radius.all(20), width=90, height=150)
                    grid_view.controls.append(Container(content=image, on_click=show_bottom_sheet))

            card = Card(content=Container(content=Column([grid_view, ft.ListTile(title=ft.Text(title),subtitle=ft.Text(subtitle))], horizontal_alignment='center'),
                                padding=10, width=400, height=370), width=400)
            return card

    def show_bottom_sheet(e):
        item = e.__dict__['control'].content.foreground_image_url.split('/')[-1][:-5]
        item_name = articles_df[articles_df.article_id == float(item)].prod_name.values[0]
        item_desc = articles_df[articles_df.article_id == float(item)].detail_desc.iloc[0]

        bs_container.content = ft.Row([Column([ft.Image(get_item_image(item), width=150, height=250, border_radius=ft.border_radius.all(40))], alignment='start'),
                            Column([Text(item_name, weight='bold', size=24, width=250), Text(item_desc, width=250, weight='w400', size=18)], alignment='start')], height=300)

        bs.open = True
        bs.update()




    bs_container = ft.Container(padding=1, margin=20)
    bs = ft.BottomSheet(bs_container)
    lv = ft.ListView(expand=1, spacing=10, padding=20)

    def update_list_view(e):
        lv.controls = []
        customer, customer_data, customer_history, detail_descs, rcmnds = get_random_customer()
        for group, title, subtitle in zip(rcmnds, titles, subtitles):
            card = get_rcmnds_card(group, title, subtitle)
            lv.controls.append(card)

        header_row_controls = [Image(src=get_item_image(i), border_radius=ft.border_radius.all(10), width=100, height=130) for i in  np.unique(customer_history)[:10]]
        header.controls = header_row_controls

        header.update()
        view.update()


    new_button = Row([ElevatedButton('Get Random Customer', on_click=update_list_view)],alignment='center')
    header = Row(alignment='center', vertical_alignment='center', spacing=5, scroll='hidden')

    view = View('/customer_recommendation', vertical_alignment='center',  horizontal_alignment='center')
    view.controls.append(new_button)
    view.controls.append(Row([Text('A Sample of the Customer Purchase History', weight='w400')], alignment='center', vertical_alignment='center'))
    view.controls.append(Divider(thickness=2))
    view.controls.append(header)
    view.controls.append(Divider(thickness=2))
    view.controls.append(lv)
    view.controls.append(bs)
    recommender_navigation_bar = settings.recommender_navigation_bar
    view.controls.append(recommender_navigation_bar)
    view.controls.append(settings.back_button)

    return view
