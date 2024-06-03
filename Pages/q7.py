# Pages/q2.py

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
            "page_name": "q7",
            "duration_seconds": page_duration.total_seconds(),
            "participant_ID": st.session_state.name
        })



def main():
    st.title("Question 7")
    
    st.subheader("The educational setup (e.g. structure, content, teaching/learning methods, level, and coherence) worked well and was suitable for this course/project. 5 Scale: Disagree to agree")
    rating = st.slider("Rate the statement", 1, 5, key="Q7")

    if rating <= 2:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: In what ways do you feel the effort required did not correspond with the credits?"
    elif rating == 3:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: Were there any specific aspects where you felt the effort didn't match the credits? Can you provide examples of any particular assignments, activities, or discussions that you found especially needs more time and efforts?"
    else:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: What aspects of the course/project made you feel that you applied more effort than the corresponded number of credits?"
    
    st.write(follow_up)
    response = st.text_input("Your answer", key="Q7_follow_up")
    
    if st.button("Next"):
        # Save the responses
        st.session_state['Q7_rating'] = rating
        st.session_state['Q7_response'] = response
        st.session_state['Q7_followup'] = follow_up

        if response:
            st.session_state.oocsi.send('HAI_survey', {
                    'participant_ID': st.session_state.name,
                    'rating': st.session_state['Q7_rating'],
                    'response': st.session_state['Q7_response'],
                    'followup': st.session_state['Q7_followup'],
                    "page_name": "q7"
                    })
        switch_page("q8")  # Switch to the next question page



if __name__ == "__main__":
    main()
