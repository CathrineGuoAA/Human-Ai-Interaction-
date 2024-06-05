# Pages/q4.py


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
            "page_name": "q4",
            "duration_seconds": page_duration.total_seconds(),
            "participant_ID": st.session_state.name
        })

def main():
    st.title("Question 4")
    
    st.subheader("The course/project was well organized. 5 Scale: Disagree to agree")
    rating = st.slider("Rate the statement", 1, 5, key="Q4")

    if rating <= 2:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: What aspects of the material do you think were unclear or demotivating? Can you suggest any additional materials needed or emerging trends that could be included in future iterations of the course?"
    elif rating == 3:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬:  Were there any specific parts of the material that you found unclear? Can you provide examples of any particular materials that you found especially engaging?"
    else:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            st.success('Done!')
        time.sleep(1)  # Wait 1 seconds
        follow_up = "🤖💬: What aspects of the material did you find most clear and motivating?"
    
        st.write(follow_up)
    response = st.text_input("Your answer", key="Q4_follow_up")
    
    if st.button("Next"):
        # Save the responses
        st.session_state['Q4_rating'] = rating
        st.session_state['Q4_response'] = response
        st.session_state['Q4_followup'] = follow_up

        if response:
            st.session_state.oocsi.send('HAI_survey', {
                    'participant_ID': st.session_state.name,
                    'rating': st.session_state['Q4_rating'],
                    'response': st.session_state['Q4_response'],
                    'followup': st.session_state['Q4_followup'],
                    "page_name": "q4"
                    })
        switch_page("q5")  # Switch to the next question page
        
if __name__ == "__main__":
    main()
