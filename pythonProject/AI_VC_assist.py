import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen and recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, I encountered an error."

# Main loop
while True:
    user_input = listen().lower()

    if "hello" in user_input:
        speak("Hello! How can I propose you?")

    elif "who are you" in user_input:
        speak("I am your boyfriend.")

    elif "I don't have boyfriends" in user_input:
        speak("Then I will be your boyfriend.")

    elif "Sorry its a wrong number" in user_input:
        speak("I will die without you.")

    elif "I don't know who you are, don't call me again" in user_input:
        speak("I will be waiting in-front of your college...Welcome to my heart")
        break


