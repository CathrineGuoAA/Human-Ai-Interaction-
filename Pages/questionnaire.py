import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
from oocsi_source import OOCSI
import datetime
from datetime import datetime
import streamlit_survey as ss

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
            "page_name": "queationnaire",
            "duration_seconds": page_duration.total_seconds(),
            "participant_ID": st.session_state.name
        })


st.session_state.current_page_title = "Final Page"
page_start_time = None
record_page_start_time()

def create_question(left_label, right_label, key):
    st.markdown(
        f"""
        <style>
            .radio-container {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 15px;
            }}
            .radio-label {{
                width: 20%;
            }}
            .radio-buttons {{
                display: flex;
                justify-content: center;
                width: 60%;
            }}
            .radio-buttons label {{
                margin: 0 5px;
            }}
        </style>
        <div class="radio-container">
            <div class="left-label">{left_label}</div>
            <div class="radio-buttons">
                <input type="radio" name="{key}" value="1"> 1
                <input type="radio" name="{key}" value="2"> 2
                <input type="radio" name="{key}" value="3"> 3
                <input type="radio" name="{key}" value="4" checked> 4
                <input type="radio" name="{key}" value="5"> 5
                <input type="radio" name="{key}" value="6"> 6
                <input type="radio" name="{key}" value="7"> 7
            </div>
            <div class="right-label">{right_label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# Only proceed if 'name' and 'topic' are set
    if st.session_state['name'] :
            with st.form("UXQ", clear_on_submit=True):
                st.write("These questions only ask for your opinion about :orange-background[:orange[** when you read the letter**]] ")

                # List of questions
                questions = [
                    ("annoying", "enjoyable"),
                    ("not understandable", "understandable"),
                    ("creative", "dull"),
                    ("easy to learn", "difficult to learn"),
                    ("valuable", "inferior"),
                    ("boring", "exciting"),
                    ("not interesting", "interesting"),
                    ("unpredictable", "predictable"),
                    ("fast", "slow"),
                    ("inventive", "conventional"),
                    ("obstructive", "supportive"),
                    ("good", "bad"),
                    ("complicated", "easy"),
                    ("unlikable", "pleasing"),
                    ("usual", "leading edge"),
                    ("unpleasant", "pleasant")
                ]

        # Create questions and store responses
            responses = {}
            for i, (left, right) in enumerate(questions):
                number = f"question_{i+1}"
                responses[number] = st.radio(
                    f"{left_label} - {right_label}",
                    options=[1, 2, 3, 4, 5, 6, 7],
                    index=3,
                    key=number,
                    horizontal=True
                )


        # Submit button without a key
            submitted = st.form_submit_button("Submit")

            if submitted:
                # Save the responses
                st.session_state['response'] = responses
                st.session_state['Q'] = number
                
                if page_start_time:
                    record_page_duration_and_send()  

                st.session_state.oocsi.send('HAI_UEQ', {
                    'participant_ID': st.session_state['name'],
                    'response': st.session_state['response'],
                    'Q': st.session_state['Q']
                })
                st.write("Thank you for your responses.")
            else:
                st.write("Please enter your name and topic to proceed.")

