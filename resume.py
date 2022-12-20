
from flet import *
import flet as ft
import settings




def get_resume_page():

    page = settings.page
    device = settings.device
    view_padding = settings.view_padding
    view_horizontal_alignment = settings.view_horizontal_alignment
    navigation_bar = settings.navigation_bar

    color = '#3E665F'
    section_size = 36
    sub_section_size = 24
    text_size = 20

    section_weight = 'w800'
    title_weight = 'bold'
    text_weight = 'w400'

    ## Experience
    #################################################
    experience_label = Text('Experience', size=section_size, weight=section_weight)

    upwork_title = Text('Freelance Data Scientist, Upwork', size=sub_section_size, weight=title_weight, color=color)
    upwork_text = Text('As a freelancer data scientist, I have worked on one project so far. The objective was to utilize machine learning in algorithmic trading.',
                        size=text_size, weight=text_weight)

    swftbox_title = Text('Data Science Intern, SWFTBOX', size=sub_section_size, weight=title_weight, color=color)
    swftbox_text = Text("As an intern at data-driven delivery start-up, my responsibility was to aid in data preparation andanalysis to understand the demand of each provider and the behavior of each driver in thenetwork to optimize the time and cost of each delivery task and help providers to be ready forupcoming demand.",
                        size=text_size, weight=text_weight)

    teacher_title = Text('Computer Science Teacher, Ministry of Education', size=sub_section_size, weight=title_weight, color=color)
    teacher_text = Text('Delivering a material about basic data manipulation techniques in python, building simple machine learning and deep learning models',
                        size=text_size, weight=text_weight)



    ## Projects
    #################################################

    projects_label = Text('Projects', size=36, weight=section_weight)
    t = Text('Go to projects section to see it in action', color=color)
    hm_title = Text('H&M Fashion Recommender System', size=sub_section_size, weight=title_weight, color=color)
    hm_text = Text('Building a recommender system for H&M using both collaborative filtering and content-based filtering. I built four different sets of customers and items embeddings using items images, items text description, items features and matrix factorization',
                        size=text_size, weight=text_weight)

    swftbox__project_title = Text('Delivery ETA Optimization', size=sub_section_size, weight=title_weight, color=color)
    swftbox_prject_text = Text("Predicting ETA of deliveries and future demand for SWFTBOX which helped optimize and reduce the number of drivers required at each location for every time window during the day by 15-30%",
                        size=text_size, weight=text_weight)

    crypto_bot_title = Text('CryptoBot', size=sub_section_size, weight=title_weight, color=color)
    crypto_bot_text = Text('Building a crypto trading bot using FreqTrade toolbox. The bot performs trades based on trading signals generated commonly used technical indicators',
                        size=text_size, weight=text_weight)

    ## Education
    #################################################
    education_title = Text('Education', size=section_size, weight=section_weight, color=color)
    education_text = Text('Bsc. in Electrical Engineering from Jordan University of Science and Technology with a GPA of 3.03',
                             size=text_size, weight=text_weight)


    ## Courses
    #################################################
    courses_title = Text('Courses', size=section_size, weight=section_weight, color=color)
    corses_text = Text("""• Machine Learning Engineering for Production Specialization
• Recommendation Systems with TensorFlow on GCP
• Machine Learning for Trading Specialization
• Natural Language Processing Specialization""", size=text_size, weight=text_weight)

    ##Skills
    #################################################
    skills_title = Text('Skills', size=section_size, weight=section_weight, color=color)
    skilss_text = Text("""• Data cleaning and preprocessing using pandas.
• Data visualization with Matplotlib and Streamlit.
• Statistical and neural modeling with Sci-kit learn and TensorFlow.
• Time Series Analysis using ARIMA models and Recurrent Neural Networks.
• Deploying and monitoring deep learning models using TensorFlow Extended (TFX).
• Building data processing pipelines.
• Building recommender system using content based filtering and collaborative filtering
• Developing machine learning models on AWS and GCP.
• Data wrangling using MySQL.
• Performing Natural Language Processing using statistical and neural modeling algorithms.
• Performing basic image processing and building Convolutional Neural Networks for image classification.
• Handling large datasets using PySpark
""", size=text_size, weight=text_weight)


    ## PROGRAMING LANGUAGES AND TOOLS
    #################################################
    tools_title = Text('Programming Languages and Tools', size=section_size, weight=section_weight, color=color)
    tools_text = Text("""• Python
• SQL
• Sci-Kit Learn
• PySpark
• TensorFlow Recommenders
• Auquan Toolbox for Quantitative Trading
• Docker
• Java
• Plotly
• Keras
• Kubernetes
• FreqTrade toolbox
• Pandas-TA (technical analysis)
• Plotly Dash
""", size=text_size, weight=text_weight)


    ## Column
    #################################################
    hdivider = Divider(height=50, color='#FAFDFB')
    vdivider = VerticalDivider(color=color, width=100, thickness=2)

    column = Column([experience_label, upwork_title, upwork_text, swftbox_title, swftbox_text, teacher_title, teacher_text, hdivider] +
                    [projects_label, hm_title, t, hm_text, swftbox__project_title, swftbox_prject_text, crypto_bot_title, crypto_bot_text, hdivider]+
                    [education_title, education_text, hdivider]+
                    [courses_title, corses_text, hdivider]+
                    [skills_title, skilss_text, hdivider]+
                    [tools_title, tools_text, hdivider],
                    horizontal_alignment='start', expand=True, scroll='hidden')

    if device in ['android', 'ios']:
        view = View("/resume", [column, navigation_bar], padding=view_padding, horizontal_alignment=view_horizontal_alignment)
    elif device in ['windows', 'macos', 'linux']:
        view = View("/resume", [Row([navigation_bar, vdivider,column], expand=True)], padding=view_padding, horizontal_alignment=view_horizontal_alignment, spacing=100)

    view.controls.append(settings.back_button)

    return view