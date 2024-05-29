# Pages/q2.py

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def main():
    st.title("Question 2")
    
    st.subheader("The educational setup (e.g. structure, content, teaching/learning methods, level, and coherence) worked well and was suitable for this course/project. 5 Scale: Disagree to agree")
    rating = st.slider("Rate the statement", 1, 5, key="Q2")

    if rating <= 2:
        follow_up = "What aspects of the setup do you think were not suitable?"
    elif rating == 3:
        follow_up = "Is there any particular aspect of the setup you found lacking?"
    else:
        follow_up = "What aspects of the course/project did you find most effective?"
    
    st.write(follow_up)
    response = st.text_input("Your answer", key="Q2_follow_up")
    
    if st.button("Next"):
        # Save the responses
        st.session_state['Q2_rating'] = rating
        st.session_state['Q2_response'] = response
        switch_page("q3")  # Switch to the next question page

if __name__ == "__main__":
    main()
