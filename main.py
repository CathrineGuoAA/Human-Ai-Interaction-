import streamlit as st
import os
from Pages import questions  # Importing the questions from the questions file
from streamlit_extras.switch_page_button import switch_page
from oocsi_source import OOCSI
import datetime
from datetime import datetime
import Pages


# Initialize OOCSI
if 'oocsi' not in st.session_state:
    st.session_state.oocsi = OOCSI('', 'oocsi.id.tue.nl')


# Record start time for each page
def record_page_start_time():
    global page_start_time
    page_start_time = datetime.now()

# Record page duration and send data via OOCSI
def record_page_duration_and_send():
    current_page_title = st.session_state.current_page_title
    if page_start_time:
        page_end_time = datetime.now()
        page_duration = page_end_time - page_start_time
        st.write(f"Time spent on {current_page_title}: {page_duration}")

        # Send data to Data Foundry via OOCSI
        data = {
            "page_name": current_page_title,
            "duration_seconds": page_duration.total_seconds(),
            'participant_ID': st.session_state.participantID
        }
        st.session_state.oocsi.send('HAI_consent', data)


# Initialize survey
st.sidebar.title("Contact Info")
st.sidebar.write("Email: s.guo3@tue.nl")
st.title('Feedback Questionnaire')
st.markdown('😀 Welcome to our test')



st.markdown('''
    1️⃣ I have enough information about the research project from the separate information sheet. I have read it, and I have had the chance to ask questions, which have been answered to my satisfaction.
                    
    2️⃣ I take part in this research project voluntarily. There is no explicit or implicit pressure for me to take part in this research project, and I understand I can stop my participation at any moment without explaining why. I do not have to answer any question I do not want to answer.
                    
    3️⃣ I know my personal data will be collected and used for the research, as explained to me in the information sheet.

    ''')

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


if st.session_state.name:
    st.write(f"Hello, {st.session_state.name}!")

    if agree == "do":
        st.write('Thank you! Please continue to the next page to start the experiment')
        if st.button("Next page"):
            st.session_state.oocsi.send('HAI_CONSENT', {
                'participant_ID': st.session_state.name,
                'consent': 'yes',
                'consentForOSF': consent_for_osf
            })
            switch_page("q1")
    else:
        if st.button("Next page"):
            switch_page('https://www.pinterest.com/')
