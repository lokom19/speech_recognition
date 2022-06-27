import speech_recognition as sr
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print('Скажи что-нибудь: ')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Ты сказал : {}".format(text))
        except:
            print("Извини, не понимаю")
            continue