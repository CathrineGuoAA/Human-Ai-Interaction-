# Pages/q1.py

import os
import streamlit as st
import datetime
from datetime import datetime
from streamlit_extras.switch_page_button import switch_page
from oocsi_source import OOCSI
import time

# Initialize OOCSI
if 'oocsi' not in st.session_state:
    st.session_state.oocsi = OOCSI('', 'oocsi.id.tue.nl')


# Record page start time function
def record_page_start_time():
    st.session_state['page_start_time'] = datetime.now()

# Record page duration and send data via OOCSI
def record_page_duration_and_send():
    if 'page_start_time' in st.session_state:
        page_duration = datetime.now() - st.session_state['page_start_time']
        st.session_state.oocsi.send('HUMAN AI INTERACTION', {
            "page_name": "q1",
            "duration_seconds": page_duration.total_seconds(),
            "participant_ID": st.session_state.name
        })


def main():
    st.title("Question 1")
    
    st.subheader("On a scale of 1 to 10, how would you rate this course/project?")
    rating = st.slider("Rate the statement", 1, 10, key="Q1")

    if rating <= 4:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = " 🤖💬: What aspects of the course/project do you think need improvement?"
    elif 5 <= rating <= 7:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: Is there anything specific you think could be improved?"
    else:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: What aspects of the course/project did you find most effective?"
    
    st.write(follow_up)
    response = st.text_input("Your answer", key="Q1_follow_up")
    
    if st.button("Next"):
        # Save the responses
        st.session_state['Q1_rating'] = rating
        st.session_state['Q1_response'] = response
        st.session_state['Q1_followup'] = follow_up
    
        if response:
            st.session_state.oocsi.send ('HAI_survey', {
                    'participant_ID': st.session_state.name,
                    'q1rating': st.session_state['Q1_rating'],
                    'q1response': st.session_state['Q1_response'],
                    'q1followup': st.session_state['Q1_followup'],
                    "page_name": "q1"
                    })
        switch_page("q2")  # Switch to the next question page



if __name__ == "__main__":
    main()
