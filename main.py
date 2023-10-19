import streamlit as st
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Streamlit app layout
st.title("Speech-to-Text App")

# Define the question
question = st.text_area("Question:", "What is your question?")

# Create an expander for the microphone and stop button
with st.expander("Speech Input"):
    mic_button = st.button("Start Recording")
    stop_button = st.button("Stop Recording")

# Initialize a list to store speech-to-text results
results = st.sidebar.beta_container()
speech_results = []

# Analyze button to process the speech
if st.button("Analyze"):
    if mic_button:
        st.warning("Please stop recording before analyzing.")
    else:
        try:
            with sr.Microphone() as source:
                st.info("Recording... Speak now.")
                audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            speech_results.append(text)
            results.write(f"Speech-to-Text Result: {text}")
        except sr.UnknownValueError:
            st.warning("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")

# Display the speech-to-text results
with results:
    st.title("Speech-to-Text Results")
    for idx, result in enumerate(speech_results):
        st.write(f"Result {idx + 1}: {result}")
