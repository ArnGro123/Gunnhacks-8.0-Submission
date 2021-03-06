from tkinter import *
import speech_recognition
import pyttsx3
import openai

def bind_func():

    root = Tk()
    root.title('Key Bind Button')
    root.geometry("200x200")

    def button_animation(x,y,fcolor,bcolor,cmd,text):

        def on_entry(e):
            test_button['background']=bcolor
            test_button['foreground']=fcolor

        def out_entry(e):
            test_button['background']=fcolor
            test_button['foreground']=bcolor

        test_button = Button(root,width=200,height=200,text=text,
                            fg=bcolor,
                            bg=fcolor,
                            border=0,
                            activeforeground=fcolor,
                            activebackground=bcolor,
                            command=cmd
                            )

        test_button.bind('<Enter>', on_entry)
        test_button.bind('<Leave>', out_entry)
        test_button.place(x=x,y=y)

    button_animation(0,0,"#141414","light blue",run,"RUN")

    root.mainloop()

def run():
    def speech_text():

        global question

        print("Ask a Question:")

        recognizer = speech_recognition.Recognizer()

        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                question = text
                
        except speech_recognition.UnknownValueError():
            recognizer = speech_recognition.Recognizer()
            

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


    def text_to_speech(response):

        converter = pyttsx3.init()

        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

        converter.setProperty("voice", voice_id)
        converter.setProperty("rate", 150)
        converter.setProperty("volume", 0.7)

        converter.say(response)

        converter.runAndWait()


    speech_text()
    print("Question:", question)

    response = chat_bot(question)
    print("Response:", response)
        
    text_to_speech(response)

bind_func()