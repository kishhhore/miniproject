from pynput import keyboard
import pyttsx3
import speech_recognition as sr
from ai21 import AI21Client

client = AI21Client(api_key="4eT4o4XUrYxW3mJAoNkriN8ybuDpHZXK")
key_buffer = []
tts_engine = pyttsx3.init()

class Action:
    def _init_(self):
        self.is_listening = False

    def start_listening(self):
        self.is_listening = True
        self.keylogger()
        self.speak("Hello, how can I help you?")
        recognized_text = self.listen_to_speech()
        if recognized_text:
            self.speak(f"You said: {recognized_text}")
            response = self.generate_response(recognized_text)
            self.speak(response)
        self.is_listening = False

    def keylogger(self):
        if self.is_listening:
            def on_press(key):
                global key_buffer
                try:
                    char = key.char
                except AttributeError:
                    if key == keyboard.Key.space:
                        char = ' '
                    elif key == keyboard.Key.enter:
                        char = '\n'
                    elif key == keyboard.Key.tab:
                        char = '\t'
                    elif key == keyboard.Key.backspace:
                        char = '<BACKSPACE>'
                    else:
                        char = ''

                if char:
                    key_buffer.append(char)
                    if len(key_buffer) > 10:
                        key_buffer.pop(0)

                    if ''.join(key_buffer) == ' ' * 10:
                        listener.stop()

            def on_release(key):
                pass

            with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
                listener.join()

    def generate_response(self, prompt):
        response = client.completion.create(
            model="j2-ultra",
            prompt=prompt,
            num_results=1,
            max_tokens=200,
            temperature=0.1,
        )
        generated_text = response.completions[0].data.text
        return generated_text

    def speak(self, text):
        tts_engine.say(text)
        tts_engine.runAndWait()

    def listen_to_speech(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            self.speak("Listening...")
            audio = recognizer.listen(source)
            try:
                print("Recognizing...")
                self.speak("Recognizing..")
                text = recognizer.recognize_google(audio)
                print(f"Recognized text: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                return ""
            except sr.RequestError:
                print("Could not request results; check your network connection.")
                return ""

if _name_ == "_main_":                 
    while True:
        action = Action()
        action.start_listening()
