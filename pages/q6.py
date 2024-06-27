# Pages/q6.py

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
            "page_name": "q6",
            "duration_seconds": page_duration.total_seconds(),
            "participant_ID": st.session_state.name
        })



def main():
    st.title("Question 6")
    
    st.subheader(" Overall, how would you describe the level of difficulty in this course/project?. 5 Scale: Disagree to agree")
    rating = st.slider("Rate the statement", 1, 5, key="Q6")

    if rating <= 2:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: In what ways do you think the difficulty level could be increased?"
    elif rating == 3:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: Were there any specific areas where you found the difficulty level challenging or appropriate?"
    else:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: What aspects of the course/project challenged you a lot or you find really difficult ?"
    
    st.write(follow_up)
    response = st.text_input("Your answer", key="Q6_follow_up")
    
    if st.button("Next"):
        # Save the responses
        st.session_state['Q6_rating'] = rating
        st.session_state['Q6_response'] = response
        st.session_state['Q6_followup'] = follow_up

        if response:
            st.session_state.oocsi.send('HAI_survey', {
                    'participant_ID': st.session_state.name,
                    'rating': st.session_state['Q6_rating'],
                    'response': st.session_state['Q6_response'],
                    'followup': st.session_state['Q6_followup'],
                    "page_name": "q6"
                    })
        switch_page("q7")  # Switch to the next question page



if __name__ == "__main__":
    main()
