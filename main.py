import streamlit as st
import streamlit_survey as ss

# Define main questions and sub-questions
questions = {
    1: {
        "main": "On a scale of 1 to 10, how would you rate this course/project?",
        "follow_ups": [
            "What aspects of the course/project do you think need improvement?",
            "Is there anything specific you think could be improved?",
            "What aspects of the course/project did you find most effective?"
        ]
    },
    2: {
        "main": "The educational setup (e.g. structure, content, teaching/learning methods, level, and coherence) worked well and was suitable for this course/project. 5 Scale: Disagree to agree",
        "follow_ups": [
            "What aspects of the setup do you think were not suitable?",
            "Is there any particular aspect of the setup you found lacking? Or Are there any aspects of the course's/project's structure, teamwork dynamics, or deliverables that you believe could be improved?",
            "What aspects of the course/project did you find most effective?"
        ]
    },
    3: {
        "main": "The course/project was well organized. 5 Scale: Disagree to agree",
        "follow_ups": [
            "In what ways do you think the setup/organization could be improved?",
            "Were there any specific aspects of the setup/organization that you found lacking?",
            "What aspects of the setup/organization did you find most effective?"
        ]
    },
    4: {
        "main": "The course material was clear and motivated me to study for this course/project. 5 Scale: Disagree to agree",
        "follow_ups": [
            "What aspects of the material do you think were unclear or demotivating? Can you suggest any additional materials needed or emerging trends that could be included in future iterations of the course?",
            "Were there any specific parts of the material that you found unclear? Can you provide examples of any particular materials that you found especially engaging?",
            "What aspects of the material did you find most clear and motivating?"
        ]
    },
    5: {
        "main": "The assessment of this course/project was appropriate. 5 Scale: Disagree to agree",
        "follow_ups": [
            "What aspects of the assessment do you think were inappropriate?",
            "Were there any specific aspects of the assessment that you found unclear or irrelevant?",
            "What aspects of the assessment did you find most appropriate?"
        ]
    },
    6: {
        "main": "Overall, how would you describe the level of difficulty in this course/project? 5 Scale: Very easy to very difficult",
        "follow_ups": [
            "In what ways do you think the difficulty level could be increased?",
            "Were there any specific areas where you found the difficulty level challenging or appropriate?",
            "What aspects of the course/project challenged you a lot or you find really difficult?"
        ]
    },
    7: {
        "main": "Did the effort you applied correspond with the number of credits? 5 Scale: Much less to much more effort",
        "follow_ups": [
            "In what ways do you feel the effort required did not correspond with the credits?",
            "Were there any specific aspects where you felt the effort didn't match the credits? Can you provide examples of any particular assignments, activities, or discussions that you found especially needs more time and efforts?",
            "What aspects of the course/project made you feel that you applied more effort than the corresponded number of credits?"
        ]
    },
    8: {
        "main": "What percentage of the teaching sessions did you attend? 5 Scale: Percentage ten steps",
        "follow_ups": [
            "What factors influenced your attendance?",
            "Were there any particular sessions you found more beneficial than others?",
            "What aspects of the teaching sessions did you find most helpful?"
        ]
    },
}

# Initialize survey
st.sidebar.title("Contact Info")
st.sidebar.write("Email: s.guo3@tue.nl")
st.title('Feedback Questionnaire')
st.markdown('😀 Welcome to our test')
survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(len(questions) + 1, on_submit=lambda: st.success("Your responses have been recorded. Thank you!"))

# Update state function
def update_state():
    question_num = pages.current
    response_key = f"Q{question_num}"
    response = st.session_state.get(response_key, "0")
    
    for j in range(1, 4):
        st.session_state[f'show_Q{question_num}_{j}'] = False

    response_int = int(response)

    if question_num == 1:  # Special logic for the 10-point scale
        if response_int <= 4:
            st.session_state[f'show_Q{question_num}_1'] = True
        elif 5 <= response_int <= 7:
            st.session_state[f'show_Q{question_num}_2'] = True
        elif response_int >= 8:
            st.session_state[f'show_Q{question_num}_3'] = True
    else:  # Logic for the 5-point scale
        if response_int <= 2:
            st.session_state[f'show_Q{question_num}_1'] = True
        elif response_int == 3:
            st.session_state[f'show_Q{question_num}_2'] = True
        elif response_int >= 4:
            st.session_state[f'show_Q{question_num}_3'] = True

# Main survey loop
with pages:
    for i in range(1, len(questions) + 1):
        if pages.current == i:
            q_info = questions[i]
            st.subheader(f"Question {i}: {q_info['main']}")
            options_range = 10 if i == 1 else 5  # 10-point scale for the first question, 5-point for the rest
            options = [str(num) for num in range(1, options_range + 1)]

            survey.select_slider(
                "Rate the statement",
                options = options,
                label_visibility = "collapsed",
                key = f"Q{i}",
                on_change = update_state
            )

            for j, follow_up in enumerate(q_info['follow_ups'], 1):
                if st.session_state.get(f'show_Q{i}_{j}', False):
                    st.write(f"AI Assistant 💭: {follow_up}")
                    user_input = survey.text_input("Please specify:", key=f"Q{i}_{j}")
                    print('*****************')
                    print(user_input)
                    if st.button(f"Submit Answer {i}_{j}"):
                        st.session_state[f"Q{i}_{j}_submitted"] = user_input  # 保存用户输入
                        #st.session_state.oocsi.send  #?
                        #st.session_state[f"Q{i}_{j}"] = ""  # 清空文本输入框
                        st.rerun()  # 重新运行脚本以清空文本输入框

if pages.current == len(questions) + 1:
    st.subheader("Completion")
    st.write("Thank you for completing the survey!")
# streamlit run main.py