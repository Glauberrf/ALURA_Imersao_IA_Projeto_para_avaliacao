import speech_recognition as sr

#Função para converter audio em Texto
def AudioToText():
    r = sr.Recognizer()

    with sr.AudioFile('voz.wav') as source:
        audio = r.record(source)

    text = r.recognize_google(audio, language='pt-BR')
    print(text)
    return text
#AudioToText()