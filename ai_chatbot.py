import speech_recognition
import pyttsx3
import openai

def speech_text():

    global question

    recognizer = speech_recognition.Recognizer()

    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(text)
            question = text
            
    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()
        
speech_text()
print("Question:",question)

def chat_bot(stext):

    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=stext,
            temperature=0.1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )
    
    return response.choices[0].text

response = chat_bot(question)
print(response)

def text_to_speech(response):

    converter = pyttsx3.init()

    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

    converter.setProperty("voice", voice_id)
    converter.setProperty("rate", 150)
    converter.setProperty("volume", 0.7)

    converter.say(response)

    converter.runAndWait()

    voices = converter.getProperty('voices')

text_to_speech(response)