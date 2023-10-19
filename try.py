import streamlit as st
from speech_to_text import speech_to_tex
from speech import start_recording,stop_recording
from chat_gpt import prompting
from bard import get_response
t = None
st.title("Speech-to-Text App")
st.write('''In below box please mention your coding language and year of exeperince 
         space seprated and your desire company name''')
question = st.text_area("Interview:")
print('This is your question',question)
prompt_input = question.split(" ")
coding_lang = prompt_input[0]
exp = prompt_input[1] if len(prompt_input) > 1 else None
company_name = prompt_input[2] if len(prompt_input) > 2 else None
ask_question_button = st.button("Ask Question")
# Generating question from ChatGpt 
prompt_question = f'''
I am preparing for job switch as a software engineer. I will provide you my 
coding language, eperience and, comapny name which is in double quote.
Please ask the leval of question related with my coding language and experience.
"{coding_lang}"
"{exp}"
"{company_name}"
Please ask your question using / delimited formate.
 '''
question_by_chatGPT ="What /is /Python" #prompting(prompt_question)
#question_by_chatGPT = get_response(prompt_question)
list_question_by_chatGPT = question_by_chatGPT.split('/')
#st.write(question_by_chatGPT)
print('This is your prompt_input',prompt_input)

#recording = False
if ask_question_button:
    #i = 0 
    #while i <= len(list_question_by_chatGPT):
    st.write(question_by_chatGPT)
    mic_button = st.button("Start Recording")
    
    if mic_button:
        start_recording()
            #recording = True
        stop_button = st.button("Stop Recording")
        if stop_button:
            # Stop recording logic
            t = stop_recording()
            print(t)
            st.write(t)
            #recording = False
    prompt_ans = '''
        I will provide you answer of some questions. Please check my answer is 
        this correct or not. both question and answer are in double quote. 
        and please try to provide your answer by provide percentage of accuracy of
        my answer. if my answer accuracy percentage is less than 80% then please provide
        the answer by own.
        please try to use less words. your answer should be small and on the point.
        here is the question "{list_question_by_chatGPT[i]}".
        and here is my answer "{t}"
        '''
        #ans = prompting(prompt_ans)
        #ans = get_response(prompt_ans)
        #st.write(prompt_ans)

#i += 1