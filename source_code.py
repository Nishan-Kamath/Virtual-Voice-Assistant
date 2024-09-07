import speech_recognition as sr
import pyttsx4
import pywhatkit
import datetime
import wikipedia
import pyjokes
import openai
import subprocess
import platform
import json
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# OpenAI API Key
openai.api_key = 'your api key'

# Initialize text-to-speech engine
engine = pyttsx4.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

# Define global messages for OpenAI
messages = [{"role": "system", "content": "You are an intelligent assistant."}]

def talk(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listen for a voice command and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"User: {command}")
        return command
    except sr.UnknownValueError:
        talk("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        talk("Sorry, I'm having trouble connecting to the internet.")
        return None

def get_weather(location):
    """Fetch weather information for a given location."""
    api_key = 'your_weather_api_key'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f'The weather in {location} is currently {weather} with a temperature of {temp}°C.'
    else:
        return "Sorry, I couldn't get the weather information."

def set_reminder(reminder_text):
    """Set a reminder."""
    with open('reminders.txt', 'a') as f:
        f.write(f'{datetime.datetime.now()}: {reminder_text}\n')
    talk(f'Reminder set: {reminder_text}')

def send_email(subject, body, to_email):
    """Send an email."""
    from_email = 'your_email@gmail.com'
    from_password = 'your_email_password'
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, from_password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            talk("Email sent successfully.")
    except Exception as e:
        talk(f"Sorry, I couldn't send the email. Error: {e}")

def run_jarvis():
    command = listen_command()
    if not command:
        return

    if 'jarvis' in command:
        command = command.replace('jarvis', '').strip()

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {current_time}')
        print(f'Current time is {current_time}')

    elif 'search about' in command:
        person = command.replace('search about', '').strip()
        try:
            info = wikipedia.summary(person, sentences=3)
            talk(info)
            print(f'Jarvis: {info}')
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn't find any information on that.")
            print("Jarvis: Sorry, I couldn't find any information on that.")

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(f'Jarvis: {joke}')

    elif 'weather' in command:
        location = command.replace('weather', '').strip()
        weather_info = get_weather(location)
        talk(weather_info)
        print(f'Jarvis: {weather_info}')

    elif 'reminder' in command:
        reminder_text = command.replace('reminder', '').strip()
        set_reminder(reminder_text)

    elif 'email' in command:
        email_info = command.replace('email', '').strip()
        try:
            subject, body, to_email = email_info.split(', ', 2)
            send_email(subject, body, to_email)
        except ValueError:
            talk("Please provide the email details in the format: subject, body, recipient email.")

    elif 'open' in command:
        folder_name = command.split('open', 1)[1].strip()
        if platform.system() == 'Windows':
            subprocess.Popen(['explorer', folder_name], shell=True)
        elif platform.system() == 'Darwin':  # macOS
            subprocess.Popen(['open', folder_name])
        else:  # Unix/Linux
            subprocess.Popen(['xdg-open', folder_name])
        talk(f'Opening {folder_name}')
        print(f'Opening {folder_name}')

    elif 'exit' in command:
        talk('Exiting')
        exit()

    else:
        messages.append({"role": "user", "content": command})
        try:
            chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
            reply = chat.choices[0].message['content']
            talk(reply)
            print(f'Jarvis: {reply}')
        except Exception as e:
            talk("Sorry, something went wrong.")
            print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        run_jarvis()
