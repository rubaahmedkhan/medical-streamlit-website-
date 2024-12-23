import streamlit as st
from PIL import Image

# Define the navigation menu (sidebar)
PAGES = {
    "Home": "home.py",
    "About": "about.py",
    "Services": "services.py",
    "Contact": "contact.py",
    "Gallery": "gallery.py",
    "Book Appointment": "appointment.py",
    "Dash Board":"dashboard.py"
}

# Sidebar radio for page selection
page = st.sidebar.radio("Select a page", list(PAGES.keys()))

# Load the page dynamically
if page == "Home":
    import pages.home
elif page == "About":
    import pages.about
elif page == "Services":
    import pages.services
elif page == "Contact":
    import pages.contact
elif page == "Gallery":
    import pages.gallery
elif page == "Book Appointment":
    import pages.appointment
elif page == "Dash Board":
    import pages.dashboard    
