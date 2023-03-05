from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from chat_gpt3 import get_response

engine=init()
voices=engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
def spech(text):
    engine.say(text)
    engine.runAndWait()
messages = [
        {"role": "system", "content": "You are a vocal assistant named JOI and you speak english."}
    ]
while True:
    r=Recognizer()
    with Microphone() as source:
        print("ready to listen...")
        audio=r.listen(source)
        print('Processing input...')
        if audio!='' and audio!=None:
            try:
                testo = r.recognize_google(audio, language="en-US").lower()
                messages.append({"role": "user", "content": testo})
                print(testo)
                risposta = get_response(messages=messages)
                print('------------------')
                print(risposta)
                spech(risposta["content"])
            finally:
                s=0
        else:
            testo = ''