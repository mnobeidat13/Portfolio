import flet as ft
from flet import *
import settings
from resume import *
from car_price import *
from house_price import *
from projects import *
from contacts import *
from home import *
from navigation_bar import *
from item_recommendations import *
from customer_recommendations import *
from captioning import *
from product_tagging import *
from stock import *
from recommender import *
from landing_page import *

def main(page: Page):

    device = page.platform

    settings.init(page, device, None, None, None, None)

    page.title = "M. Obeidat"
    page.theme_mode = 'light'
    theme_color = '#3E665F'
    theme = ft.theme.Theme(color_scheme_seed=theme_color, visual_density='comfortable')
    page.theme = theme
    page.padding = 0

    navigation_bar = get_navigation_bar()
    recommender_navigation_bar = get_recommender_navigation_bar()

    def back(e):
        try:
            route = settings.route_history[-2].route
            settings.route_history = settings.route_history[:-2]
            print(route)
            page.go(route)
        except Exception as e:
            print('You are back home')

    back_button = ft.FloatingActionButton(content=ft.Row([ft.Icon(ft.icons.ARROW_BACK)], alignment="center", spacing=5),
                                            bgcolor=theme_color,shape=ft.RoundedRectangleBorder(radius=5),width=50, mini=True, on_click=back)

    settings.init(page, device, navigation_bar, recommender_navigation_bar, [], back_button)

    def route_change(route):
        page.views.clear()


        page.views.append(get_landing_page())

        if page.route == "/home1":
            page.views.append(get_home_page())

        if page.route == "/resume":
            page.views.append(get_resume_page())

        if page.route == "/projects":
            page.views.append(get_projects_page())

        if page.route == "/contacts":
            page.views.append(get_contacts_page())

        if page.route == "/house_price":
            page.views.append(get_house_price_page())

        if page.route == "/car_price":
            page.views.append(get_car_price_page())

        if page.route == "/recommender":
            page.views.append(get_recommender_page())

        if page.route == "/item_recommendation":
            page.views.append(get_item_recommendations_view())

        if page.route == "/customer_recommendation":
            page.views.append(get_customer_recommendations_view())

        if page.route == "/product_tagging":
            page.views.append(get_item_tagging_view())

        if page.route == "/captioning":

            page.views.append(get_captioning_view())

        if page.route == "/stock_market":
            page.views.append(get_stock_market_page())

        page.update()
        settings.route_history.append(route)

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_resize = lambda e: print(page.width)
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main, web_renderer="html")#, view=ft.WEB_BROWSER)