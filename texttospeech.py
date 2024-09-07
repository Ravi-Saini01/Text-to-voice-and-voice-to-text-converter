import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import speech_recognition as sr
import os


def text_to_speech():
    text = text_input.get("1.0", tk.END)
    language = 'en'  
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3") 


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data, language='en-IN') 
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, text)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Speech recognition could not understand audio")
        except sr.RequestError:
            messagebox.showerror("Error", "Could not request results from Google Speech Recognition")


root = tk.Tk()
root.title("Text-to-Speech and Speech-to-Text Converter")


text_input = tk.Text(root, height=10, width=50)
text_input.pack()

text_to_speech_button = tk.Button(root, text="Text to Speech", command=text_to_speech)
text_to_speech_button.pack()

speech_to_text_button = tk.Button(root, text="Speech to Text", command=speech_to_text)
speech_to_text_button.pack()

text_output = tk.Text(root, height=10, width=50)
text_output.pack()


root.mainloop()
