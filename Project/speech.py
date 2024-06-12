import pyttsx3
import speech_recognition as sr

tts_engine = pyttsx3.init()

# Function to speak a given text
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen to voice input and convert it to text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""

# Example usage
if True:
    text_to_speak = "Hello, how can I help you?"
    speak(text_to_speak)

    print("Please say something...")
    recognized_text = listen()
    if recognized_text:
        print(f"You said: {recognized_text}")
        speak(f"You said: {recognized_text}")
