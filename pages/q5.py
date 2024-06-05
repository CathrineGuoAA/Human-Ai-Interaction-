# Pages/q5.py

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
            "page_name": "q5",
            "duration_seconds": page_duration.total_seconds(),
            "participant_ID": st.session_state.name
        })



def main():
    st.title("Question 5")
    
    st.subheader("The educational setup (e.g. structure, content, teaching/learning methods, level, and coherence) worked well and was suitable for this course/project. 5 Scale: Disagree to agree")
    rating = st.slider("Rate the statement", 1, 5, key="Q5")

    if rating <= 2:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: What aspects of the assessment do you think were inappropriate?"
    elif rating == 3:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: Were there any specific aspects of the assessment that you found unclear or irrelevant?"
    else:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: What aspects of the assessment did you find most appropriate?"
    
    st.write(follow_up)
    response = st.text_input("Your answer", key="Q5_follow_up")
    
    if st.button("Next"):
        # Save the responses
        st.session_state['Q5_rating'] = rating
        st.session_state['Q5_response'] = response
        st.session_state['Q5_followup'] = follow_up

        if response:
            st.session_state.oocsi.send('HAI_survey', {
                    'participant_ID': st.session_state.name,
                    'rating': st.session_state['Q5_rating'],
                    'response': st.session_state['Q5_response'],
                    'followup': st.session_state['Q5_followup'],
                    "page_name": "q5"
                    })
        switch_page("q6")  # Switch to the next question page



if __name__ == "__main__":
    main()
