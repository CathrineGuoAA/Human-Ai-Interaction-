# Pages/q9.py

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
            "page_name": "q8",
            "duration_seconds": page_duration.total_seconds(),
            "participant_ID": st.session_state.name
        })


def main():
    st.title("Question 9")
    st.subheader("How would you rate the lecturers' overall effectiveness in presenting the content, engaging students, and being approachable and open to  questions? 5 Scale: Poor to excellent")
    rating = st.slider("Rate the statement", 1, 5, key="Q9")

    if rating <= 2:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: What aspects of the lecturer(s)' presentation style or engagement with students do you think could be improved?"
    elif rating == 3:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: Were there any specific instances where you felt the lecturer(s) could have been more effective in activating and engaging students or more approachable?"
    else:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: Can you recall any instances where the lecturer(s) excelled in activating and engaging students?"
    
    st.write(follow_up)
    response = st.text_input("Your answer", key="Q7_follow_up")
        
    if st.button("Next"):
        # Save the responses
        st.session_state['Q9_rating'] = rating
        st.session_state['Q9_response'] = response
        st.session_state['Q9_followup'] = follow_up

        if response:
            st.session_state.oocsi.send('HAI_survey', {
                    'participant_ID': st.session_state.name,
                    'rating': st.session_state['Q9_rating'],
                    'response': st.session_state['Q9_response'],
                    'followup': st.session_state['Q9_followup'],
                    "page_name": "q9"
                    })
        switch_page("thankyou")  # Switch to the next question page



if __name__ == "__main__":
    main()
