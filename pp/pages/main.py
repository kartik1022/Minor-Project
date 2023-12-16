import streamlit as st
st.set_page_config(
    page_title="My Page Title",
    initial_sidebar_state="auto",
    menu_items=None
)

from streamlit_option_menu import option_menu
import Home, cp, aboutus, contactus

class MultiApp():

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self): # Add 'self' parameter here
        with st.sidebar:
            app = option_menu(
                menu_title='Menu',
                options=['Home', 'Recommender', 'About Us', 'Contact Us'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }
            )

        if app == "Home":
            Home.app()
        elif app == "Recommender":
            cp.app()
        elif app == "About Us":
            aboutus.app()
        elif app == 'Contact Us':
            contactus.app()

# Create an instance of the MultiApp class
multi_app = MultiApp()

# Add apps to the multi-app instance
multi_app.add_app("Home", Home.app)
multi_app.add_app("Recommender", cp.app)
multi_app.add_app("About Us", aboutus.app)
multi_app.add_app("Contact Us", contactus.app)

# Run the multi-app
multi_app.run()