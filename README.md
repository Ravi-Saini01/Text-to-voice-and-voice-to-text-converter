Text-to-Speech and Speech-to-Text Converter
This project is a simple Text-to-Speech (TTS) and Speech-to-Text (STT) converter built using Python's Tkinter for the graphical user interface (GUI), gTTS for speech synthesis, and SpeechRecognition for converting spoken words to text. The user can input text to be converted into speech or record their voice to have it transcribed into text.

Features
Text-to-Speech (TTS): Converts the input text into speech using Google's Text-to-Speech (gTTS) API and plays it back to the user.
Speech-to-Text (STT): Records audio from the microphone and converts it to text using Google's Speech Recognition API (SpeechRecognition).
Requirements
Python 3.x
gTTS
SpeechRecognition
tkinter (usually included with Python)
pyaudio (for capturing audio input)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/text-speech-converter.git
cd text-speech-converter
Install the required dependencies:

bash
Copy code
pip install gTTS SpeechRecognition pyaudio
Run the application:

bash
Copy code
python app.py
Usage
Text to Speech:

Type or paste text into the input box.
Click the "Text to Speech" button to convert the text to audio. The audio file will be saved and played automatically.
Speech to Text:

Click the "Speech to Text" button.
Speak into the microphone, and the spoken words will be transcribed into the output text box.
Error Handling
If the speech input cannot be recognized or there is an issue with the Speech Recognition API, an error message will be shown.

Google Text-to-Speech (gTTS)
SpeechRecognition
Tkinter
