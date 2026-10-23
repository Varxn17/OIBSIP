import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import urllib.parse
import sys

# ==========================================
# 1. INITIALIZE TEXT-TO-SPEECH ENGINE
# ==========================================
engine = pyttsx3.init()

# Optional: Customize voice speed and voice type
engine.setProperty('rate', 175)     # Speed of speech (words per minute)
engine.setProperty('volume', 1.0)   # Volume (0.0 to 1.0)

# Uncomment the lines below if you want to switch between male/female voices:
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # 0 is usually male, 1 is usually female


def speak(text):
    """Converts text to speech and prints it to the console."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


# ==========================================
# 2. CAPTURE VOICE INPUT & ERROR HANDLING
# ==========================================
def listen_command():
    """
    Listens to microphone input and returns the recognized text in lowercase.
    Includes graceful error handling if speech is not understood.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        # Adjust for ambient background noise for 0.5 seconds
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        try:
            # Listen for audio input (times out if no speech starts within 5s)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("Recognizing...")
            
            # Use Google's free speech recognition API
            command = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: '{command}'")
            return command.lower()

        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please speak when you are ready.")
            return None
        except sr.UnknownValueError:
            # Graceful error handling when voice is not understood
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return None
        except sr.RequestError:
            speak("Sorry, my speech recognition service is currently unavailable. Please check your internet connection.")
            return None


# ==========================================
# 3. PROCESS COMMANDS & PERFORM ACTIONS
# ==========================================
def process_command(command):
    """Evaluates the spoken command and triggers the appropriate response."""
    
    # 1. Respond to "Hello" with a predefined greeting
    if "hello" in command or "hi" in command or "hey" in command:
        speak("Hello there! How can I help you today?")

    # 2. Tell the current time on request
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    # 3. Tell the current date on request
    elif "date" in command or "day" in command or "today" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}.")

    # 4. Perform a web search on a user-specified topic
    elif "search" in command or "google" in command:
        # Extract query if the user said "search for <topic>" or "search <topic>"
        query = command
        for prefix in ["search for", "google for", "search", "google"]:
            if prefix in query:
                query = query.split(prefix, 1)[1].strip()
                break

        # If the user only said "search", ask them what topic they want
        if not query:
            speak("What topic would you like me to search for?")
            query = listen_command()

        if query:
            speak(f"Searching the web for {query}.")
            encoded_query = urllib.parse.quote_plus(query)
            url = f"https://www.google.com/search?q={encoded_query}"
            webbrowser.open(url)

    # 5. Exit / Stop the assistant
    elif any(word in command for word in ["exit", "quit", "stop", "goodbye", "bye"]):
        speak("Goodbye! Have a great day.")
        sys.exit(0)

    # Fallback if command is recognized as words, but doesn't match a feature
    else:
        speak("I heard you, but I don't know how to handle that command yet. Please try asking for the time, date, or a web search.")


# ==========================================
# 4. MAIN LOOP
# ==========================================
def main():
    speak("Voice Assistant initialized. Say 'Hello' to start, or say 'Exit' to quit.")
    
    while True:
        try:
            command = listen_command()
            if command:
                process_command(command)
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break


if __name__ == "__main__":
    main()
    