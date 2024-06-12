from ai21 import AI21Client
import pyttsx3
import speech_recognition as sr
from time import sleep 
# Initialize AI21 client
client = AI21Client(api_key="4eT4o4XUrYxW3mJAoNkriN8ybuDpHZXK")

# Function to generate response using AI21 API
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

# Initialize text-to-speech engine
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
            sleep(1)
            print(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""

# Main function to integrate all components
def exe():
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
def listener():
    recognizer_all = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        audio = recognizer_all.listen(source)
        try:
            # print("Recognizing...")
            text = recognizer_all.recognize_google(audio)
            # print(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            # print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            # print("Could not request results; check your network connection.")
            return ""        
def main():
    while True:
        check = listener()
        if "maths helper" or "max" or "helper" or "help" or "maths" in str(check).tolower():
            exe() 
        check = None  
if __name__ == "__main__":          
    while True:                   
        main()
