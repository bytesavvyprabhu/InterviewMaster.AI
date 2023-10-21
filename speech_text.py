import speech_recognition as sr

r = sr.Recognizer()

def audio_text(file_path):
    try:
        with sr.AudioFile(file_path) as source:
            audio_data = r.record(source)  # Record audio data from the file
            text = r.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        print("Speech not recognized.")
        return ""

    
a =audio_text('F:\\PycharmProjects\\To Do Project\\Interview_master\\myrecording.wav')
print(a)