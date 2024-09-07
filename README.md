# AI Virtual Assistant 🤖

A versatile AI assistant that provides voice-activated functionality, including playing music, providing weather updates, setting reminders, sending emails, and more!

## Features 🌟

- **Play Music 🎵**: Control music playback on YouTube.
- **Current Time 🕒**: Get the current time.
- **Search Wikipedia 📚**: Retrieve information from Wikipedia.
- **Tell Jokes 😄**: Get random jokes.
- **Weather Updates 🌦️**: Check the weather for any location.
- **Set Reminders ⏰**: Add reminders to a file.
- **Send Emails 📧**: Send emails using SMTP.
- **Open Folders 📂**: Open directories on your system.
- **Interactive Chat 💬**: Engage in a conversation with OpenAI's GPT model.

## Requirements 🛠️

- Python 3.x
- Libraries: `speech_recognition`, `pyttsx4`, `pywhatkit`, `datetime`, `wikipedia`, `pyjokes`, `openai`, `requests`, `smtplib`, `subprocess`

## Setup 🔧

1. **Install Dependencies**: Run the following command to install the necessary libraries:
    ```bash
    pip install speech_recognition pyttsx4 pywhatkit wikipedia pyjokes openai requests
    ```

2. **Set Up API Keys**:
   - Replace `your api key` with your OpenAI API key.
   - Replace `your_weather_api_key` with your OpenWeatherMap API key.
   - Replace email credentials in the `send_email` function.

## Usage 🚀

1. **Run the Assistant**: Execute the script to start the assistant.
    ```bash
    python ai_virtual_assistant.py
    ```

2. **Give Commands**: Use voice commands or type in the command prompt. For example:
   - "play [song name]"
   - "what is the time?"
   - "search about [topic]"
   - "tell me a joke"
   - "weather in [city]"
   - "reminder [your reminder text]"
   - "email [subject, body, recipient email]"
   - "open [folder name]"

## Example Commands 🎤

- **Play Music**: `play Shape of You`
- **Get Time**: `what is the time?`
- **Search**: `search about Python programming`
- **Tell Joke**: `joke`
- **Weather**: `weather in London`
- **Set Reminder**: `reminder Buy groceries`
- **Send Email**: `email Meeting Reminder, Don't forget our meeting at 10 AM, recipient@example.com`
- **Open Folder**: `open Documents`


Happy coding! 🎉

