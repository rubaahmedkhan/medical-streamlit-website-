import streamlit as st

st.title("Contact Us")
st.markdown("""
You can reach us via the following methods:
- Phone: (123) 456-7890
- Email: dr.hania@example.com
""")

# Creating a form for user input
with st.form(key='contact_form'):
    # Name input
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    
    # Submit button inside the form
    submit_button = st.form_submit_button("Send Message")
    
    # Handling form submission
    if submit_button:
        if name and email and message:
            st.success("Your message has been sent successfully!")
            # Optionally, you can display or save the form data here
        else:
            st.error("Please fill in all fields.")
