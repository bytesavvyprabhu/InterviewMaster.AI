import streamlit as st
from chat_gpt import prompting
from sound_recording import record_audio_to_wav
from promptin import question_prompt, ans_prompt
import threading

question_by_chatGPT = None

# Streamlit app layout.
st.title("Welcome at InterviewMaster.AI")

# Getting Programing language, year of experience and desire company name.
st.write('''Please enter your coding language, years of experience, and desired company (space-separated) below:''')

question = st.text_area("Interview:")

prompt_input = question.split(",")

coding_lang = prompt_input[0] if len(prompt_input) > 0 else None

exp = prompt_input[1] if len(prompt_input) > 1 else None

company_name = prompt_input[2] if len(prompt_input) > 2 else None

# Button for asking a question
ask_question_button = st.button("Ask Question")

if ask_question_button:
    # Generate a question from ChatGPT based on user input
    prompt_question = question_prompt(coding_lang, exp, company_name)
    question_by_chatGPT = prompting(prompt_question)
    question_in_list = prompt_question.split(';')
    for i in question_in_list:
        # Display the generated question
        st.write(i)
        if st.button("Start"):
            text = record_audio_to_wav()
            st.write(text)
            result_thread = threading.Thread(target=ans_prompt, args=(i,text,))
            result_thread.start()  
