from pynput import keyboard
import pyttsx3
import speech_recognition as sr
from time import sleep
from ai21 import AI21Client

client = AI21Client(api_key="4eT4o4XUrYxW3mJAoNkriN8ybuDpHZXK")
key_buffer = []
tts_engine = pyttsx3.init()

def generate_response(prompt):
    response = client.completion.create(
        model="j2-ultra",
        prompt=prompt,
        num_results=1,
        max_tokens=200,
        temperature=0.1,
    )
    generated_text = response.completions[0].data.text
    return generated_text

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

# Main function to integrate all components
def main():
    text_to_speak = "Hello, how can I help you?"
    speak(text_to_speak)

    print("Please say something...")
    recognized_text = listen()
    if recognized_text:
        print(f"You said: {recognized_text}")
        speak(f"You said: {recognized_text}")
        
        response = generate_response(recognized_text)
        print(f"AI21 Response: {response}")
        speak(response)

def keylogger():
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
                main()

    def on_release(key):
        pass

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    keylogger()
