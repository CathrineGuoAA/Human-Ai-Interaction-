# Pages/q8.py

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
    st.title("Question 8")
    rating = st.slider("What percentage of the teaching sessions did you attend?", 0, 100, step=10)

    if rating < 50:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: What factors influenced your attendance?"
    elif 50 <= rating <= 75:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: Were there any particular sessions you found more beneficial than others?"
    else:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: What aspects of the teaching sessions did you find most helpful?"

    st.write(follow_up)
    response = st.text_input("Your answer", key="Q8_follow_up")

        
    if st.button("Next"):
        # Save the responses
        st.session_state['Q8_rating'] = rating
        st.session_state['Q8_response'] = response
        st.session_state['Q8_followup'] = follow_up

        if response:
            st.session_state.oocsi.send('HAI_survey', {
                    'participant_ID': st.session_state.name,
                    'rating': st.session_state['Q8_rating'],
                    'response': st.session_state['Q8_response'],
                    'followup': st.session_state['Q8_followup'],
                    "page_name": "q8"
                    })
        switch_page("thankyou")  # Switch to the next question page



if __name__ == "__main__":
    main()
