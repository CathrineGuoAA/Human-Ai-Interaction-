# Pages/q1.py

import os

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import openai

# optional; defaults to `os.environ['OPENAI_API_KEY']`
openai.api_key = '...'


# Save init prompt in the bot_prompt.
if len(st.session_state.bot_prompt) == 0:
    pr: list = prompt.split('\n')
    pr = [p for p in pr if len(p)]  # remove empty string
    st.session_state.bot_prompt = pr
    # print(f'init: {st.session_state.bot_prompt}')

def main():
    st.title("Question 1")
    
    st.subheader("On a scale of 1 to 10, how would you rate this course/project?")
    rating = st.slider("Rate the statement", 1, 10, key="Q1")

    if rating <= 4:
        follow_up = "What aspects of the course/project do you think need improvement?"
    elif 5 <= rating <= 7:
        follow_up = "Is there anything specific you think could be improved?"
    else:
        follow_up = "What aspects of the course/project did you find most effective?"
    
    st.write(follow_up)
    response = st.text_input("Your answer", key="Q1_follow_up")
    
    if response:
        generated_question = generate_follow_up_question(response)
        st.write("GPT Assistant 💭: " + generated_question)
        extra_response = st.text_input("Your answer to GPT's follow-up question", key="Q1_extra_follow_up")

if 'bot_prompt' not in st.session_state:
    st.session_state.bot_prompt = []

if user_input:
    # Add the user input to the bot_prompt before sending the prompt.
    st.session_state.bot_prompt.append(f'You: {user_input}')

    # Convert a list of prompts to a string for the GPT bot.
    input_prompt: str = '\n'.join(st.session_state.bot_prompt)
    # print(f'bot prompt input list:\n{st.session_state.bot_prompt}')
    # print(f'bot prompt input string:\n{input_prompt}')

    output = chatbot_response(input_prompt)
    # print(prompt)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

    # Add bot response for next prompt.
    st.session_state.bot_prompt.append(f'Friend: {output}')
    
    if st.button("Next"):
        # Save the responses
        st.session_state['Q1_rating'] = rating
        st.session_state['Q1_response'] = response
        if response:
            st.session_state['Q1_extra_response'] = extra_response
        switch_page("q2")  # Switch to the next question page

if __name__ == "__main__":
    main()
