# Alexa Virtual Assistant Bot

## Overview
The **Alexa Virtual Assistant Bot** is a Python-based AI voice assistant that listens to user commands, responds via voice output, and integrates ChatGPT for intelligent conversational capabilities. It utilizes:
- **SpeechRecognition** for capturing user input via voice.
- **pyttsx3** for text-to-speech conversion.
- **gTTS (Google Text-to-Speech)** as an alternative voice engine.
- **OpenAI's ChatGPT API** for AI-powered responses.

## Features
- Recognizes speech and converts it into text.
- Responds using a voice assistant.
- Integrates ChatGPT API for intelligent responses.
- Can perform basic operations like opening applications, searching the web, and answering general knowledge questions.

## Installation
Ensure you have Python installed, then install the required dependencies:

```bash
pip install speechrecognition pyttsx3 gtts openai
```

## Setup
### 1. Get OpenAI API Key
To use ChatGPT, obtain an API key from OpenAI:  
[OpenAI API](https://openai.com/api/)

### 2. Configure API Key in Code
Replace `your-api-key-here` with your actual API key in the script:

```python
import openai
openai.api_key = "your-api-key-here"
```

## Usage
Run the Python script to activate the virtual assistant:

```bash
python alexa_assistant.py
```

Then, speak into your microphone, and the assistant will respond using ChatGPT and voice synthesis.

## Example Interaction
**User:** "What is the capital of France?"
**Assistant:** "The capital of France is Paris."

## Contributing
Feel free to fork this repository, create a branch, and submit a pull request with improvements!

## License
This project is licensed under the MIT License.

## Repository
Check out the full project on GitHub:  
[Alexa Virtual Assistant Bot](https://github.com/SayandipSaha666/Alexa-Virtual-Assistant-Bot)

