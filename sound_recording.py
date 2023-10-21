import pyaudio
import wave
import keyboard
from exce import EnterPressedException
import streamlit as st
from speech_text import audio_text


def record_audio_to_wav():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100,
                        input=True, frames_per_buffer=1024)

    frames = []
    try:
        while True:
            data = stream.read(1024)
            frames.append(data)
            #if keyboard.is_pressed('enter'):
            if st.button("Stop Recording"):
                break
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()
        sound_file = wave.open("myrecording.wav","wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(frames))
        sound_file.close()
    text = audio_text('F:\\PycharmProjects\\To Do Project\\Interview_master\\myrecording.wav')
    return text
print("start")
record_audio_to_wav()
print("stop")