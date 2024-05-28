import streamlit as st

from streamlit_chat import message

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.responses.append(user_input)

def on_btn_click():
    del st.session_state['questions']
    del st.session_state['responses']

st.session_state.setdefault('questions', [])

st.title("Survey QA Bot")
questions_list = ['question 1', 'question 2', 'question 3']

if 'responses' not in st.session_state.keys():
    st.session_state.questions.extend(questions_list)
    st.session_state.responses = []

chat_placeholder = st.empty()
st.button("Clear message", on_click=on_btn_click)

message(st.session_state.questions[0]) 

with st.container():
    for response, question in zip(st.session_state.responses, st.session_state.questions[1:]):
        message(response, is_user = True)
        message(question)


with st.container():
    st.text_input("User Response:", on_change=on_input_change, key="user_input")