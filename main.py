import streamlit as st
import os
from openai import OpenAI
import streamlit_survey as ss
from Pages import questions  # Importing the questions from the questions file
from streamlit_extras.switch_page_button import switch_page
# from oocsi_source import OOCSI

# optional; defaults to `os.environ['OPENAI_API_KEY']`
openai.api_key = 'sk-proj-ljbeeer2OFS55YaPQPSRT3BlbkFJGRrPlF5gchcjYfaNqfbN'

            

# Initialize survey
st.sidebar.title("Contact Info")
st.sidebar.write("Email: s.guo3@tue.nl")
st.title('Feedback Questionnaire')
st.markdown('😀 Welcome to our test')



# Consent form
OSF = st.radio

st.subheader("✍️ Consent")
agree = st.radio(
    '4️⃣ I consent to my answers being used for quotes in the research publications – without including my name.',
    ('do', 'do not'), index=1)

consent_for_osf = "yes" if OSF == 'do' else 'no'
agree = st.radio(
        '5️⃣ I consent to my real name being mentioned in the quotes as described under 4',
        ('do', 'do not'), index=1)

consent_for_osf = "yes" if OSF == 'do' else 'no'


if 'name' not in st.session_state:
        st.session_state['name'] = ''

if not st.session_state.name:
        nameID = st.text_input("Please enter/paste here your name")
        if nameID.strip():
            st.session_state.name = nameID
        else:
            st.write("Input cannot be empty. Please try again.")

# Display final output if both inputs are provided
if agree == "do":
        st.write('Thank you! Please continue to the next page to start the experiment')

        if st.button("Next page"):
            switch_page("q1")
else:
        if st.button("Next page"):
            switch_page('https://www.pinterest.com/')
