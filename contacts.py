from flet import *
import flet as ft
import settings



def get_contacts_page():

    page = settings.page
    device = settings.device
    view_padding = settings.view_padding
    view_horizontal_alignment = settings.view_horizontal_alignment
    navigation_bar = settings.navigation_bar

    text_size = 24
    color = 'blue'

    image_width = 50; image_height = 50

    divider = VerticalDivider(color='#3E665F', width=100, thickness=2)

    t1 = Text('You can reach out to me throught email', size=30, weight='w600', color='#3E665F')
    email = Row([Image(src='https://images.vexels.com/media/users/3/140152/isolated/preview/72058b43b2690544e239218583dca020-envelop-round-icon.png', width=image_width, height=image_height),
                 Text('mnobeidat1995@gmail.com', selectable=True, size=20, weight='w500', color=color)], spacing=30)

    t2 = Text('My Profiles', size=30, weight='w600', color='#3E665F')

    linkedin = TextButton(content=Row([Image(src='https://cdn-icons-png.flaticon.com/512/179/179330.png', width=image_width, height=image_height),
                                       Text('LinkedIn', size=text_size, color=color)], spacing=30),
                                       on_click=lambda e: page.launch_url('https://www.linkedin.com/in/mnobeidat/'))

    upwork = TextButton(content=Row([Image(src='https://cdn.iconscout.com/icon/free/png-256/upwork-3629131-3030271.png', width=image_width, height=image_height),
                                       Text('Upwork', size=text_size, color=color)],spacing=30),
                                       on_click=lambda e: page.launch_url('https://www.upwork.com/freelancers/~018dcfde5c2736344d'))

    kaggle = TextButton(content=Row([Image(src='https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png', width=image_width, height=image_height),
                                       Text('Kaggle', size=text_size, color=color)],spacing=30),
                                       on_click=lambda e: page.launch_url('https://www.kaggle.com/mohammedobeidat'))

    github = TextButton(content=Row([Image(src='https://cdn3.iconfinder.com/data/icons/free-social-icons/67/github_circle_black-512.png', width=image_width, height=image_height),
                                       Text('GitHub', size=text_size, color=color)],spacing=30),
                                       on_click=lambda e: page.launch_url('https://github.com/mnobeidat13'))

    column = Column([Column([t1, email]), Column([t2, linkedin, upwork, kaggle, github])],
                     horizontal_alignment='start', spacing=50, alignment='center')

    if device in ['android', 'ios']:
        view = View("/contacts", [column, navigation_bar], padding=view_padding, horizontal_alignment=view_horizontal_alignment)
    elif device in ['windows', 'macos', 'linux']:
        view = View("/contacts", [Row([navigation_bar, divider, column], expand=True)], padding=view_padding, horizontal_alignment=view_horizontal_alignment)

    view.controls.append(settings.back_button)

    return view
