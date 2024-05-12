import random
from gtts import gTTS
import os
import platform
import playsound


#pip install playsound==1.2.2
platformThis = platform.system()


def FalarGtts(texto):
    try:
        
        #em text, informe o texto a ser dito. Evite usar acentuacao.
        #AudioDoTexto = gTTS(texto, lang='pt')  #pt eh o codigo de idioma correspondente ao Portugues. 
        #Aqui pode ser utilizado qualquer um dos codigos de idioma citados anteriormente neste post.
        if(platformThis == "Linux"):
            AudioDoTexto = gTTS(texto, lang='pt-br')
            AudioDoTexto.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
        if(platformThis == "Windows"):
            try:
                AudioDoTexto = gTTS(texto, lang='pt-br')
                AudioDoTexto.save("audio.mp3")
                #Toca o audio direto no programa
                #playsound.playsound('audio.mp3', True)
                #os.remove("audio.mp3")
                
            except:
                numero = random.randint(0,1000000000000)
                tts = gTTS (texto, lang='pt-br')
                tts.save('tmp/audio'+ str(numero) +'.mp3')
                print ('Tallud:\n    ' +texto)
                playsound.playsound('tmp/audio'+ str(numero) +'.mp3')   #windows
                os.remove('tmp/audio'+ str(numero) +'.mp3')
  
        
    except Exception as ex:
        print(ex)
    pass

        
