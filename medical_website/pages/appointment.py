import streamlit as st
from datetime import datetime

st.title("Book Your Appointment")

# Create an appointment form
with st.form(key='appointment_form'):
    # Patient's name and email
    name: str = st.text_input("Full Name")
    email: str = st.text_input("Email Address")
    
    # Choose a date for the appointment
    appointment_date = st.date_input("Select Appointment Date", min_value=datetime.today())

    # Choose time slot for the appointment
    time_slot = st.selectbox("Choose Appointment Time", ["9:00 AM", "11:00 AM", "2:00 PM", "4:00 PM"])
    
    # Submit button
    submit_button = st.form_submit_button(label="Book Appointment")
    
    if submit_button:
        st.success(f"Your appointment has been booked for {appointment_date} at {time_slot}.")
        st.markdown(f"**Patient Info:** {name}, {email}")
