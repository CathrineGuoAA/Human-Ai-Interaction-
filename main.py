import streamlit as st
import streamlit_survey as ss

st.header('📃 Welcome to feedback questionnaire')
survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(8, on_submit=lambda: st.success("Your responses have been recorded. Thank you!"))

with pages:
    if pages.current == 0:
        st.subheader("Introduction")
        st.write("there should be some content/consent form?")
    
    if pages.current == 1:
        # Initialize session states if not already present
        if 'show_Q1_1' not in st.session_state:
            st.session_state.show_Q1_1 = False
        if 'show_Q1_2' not in st.session_state:
            st.session_state.show_Q1_2 = False
        if 'show_Q1_3' not in st.session_state:
            st.session_state.show_Q1_3 = False

        # Define a callback function to handle changes in Q1
        def on_q1_change():
            # Reset states whenever Q1 changes
            st.session_state.show_Q1_1 = False
            st.session_state.show_Q1_2 = False
            st.session_state.show_Q1_3 = False
            
        # Check the response range of Q1 and update session states accordingly
            if st.session_state.Q1 in ["1", "2", "3"]:
                st.session_state.show_Q1_1 = True
            elif st.session_state.Q1 in ["4", "5", "6","7"]:
                st.session_state.show_Q1_2 = True
            elif st.session_state.Q1 in ["8", "9", "10"]:
                st.session_state.show_Q1_3 = True
            

        # First question with a callback to update state based on the answer
        st.write("How satisfied are you with this survey?")
        Q1 = survey.select_slider(
            "Overall Satisfaction",
            options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            label_visibility="collapsed",
            key="Q1",
            on_change=on_q1_change
        )

        # Check which follow-up question should be shown
        if st.session_state.show_Q1_1:
            st.write("AI Assistant 💭 Follow-up Question Q1-1: Why is your satisfaction low?")
            Q1_1 = survey.text_input("Please specify for Q1-1:", key="Q1-1")

        if st.session_state.show_Q1_2:
            st.write("AI Assistant 💭 Follow-up Question Q1_2: Why is your satisfaction moderate?")
            Q1_2 = survey.text_input("Please specify for Q1_2:", key="Q1_2")

        if st.session_state.show_Q1_3:
            st.write("AI Assistant 💭 Follow-up Question Q1_3: Why is your satisfaction moderate?")
            Q1_3 = survey.text_input("Please specify for Q1_3:", key="Q1_3")
    
    elif pages.current == 2:

    # Check which page is currently active
        if pages.current == 2:
            # Question 2
            Q2 = survey.select_slider(
                "Likert scale:",
                options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
                key="Q2"
            )

            # Conditionally display follow-up questions
            if Q2 == "Strongly Disagree" or Q2 == "Disagree":
                Q2_1 = survey.text_input("Follow-up for Disagree: Please specify your reasons:", key="Q2_1")
            elif Q2 == "Neutral":
                Q2_2 = survey.text_input("Follow-up for Neutral: Please elaborate on your neutrality:", key="Q2_2")
            elif Q2 == "Agree" or Q2 == "Strongly Agree":
                Q2_3 = survey.text_input("Follow-up for Agree: Why do you agree?", key="Q2_3")