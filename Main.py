import telepot
import json
from ConverterAudio import ConvertAudioOGGtoWAV
from ConverteAudioTotext import AudioToText
#from Executor_AI import Execut
from ExecutorIA import GeminiBot
#from pyttsx import Falar
from Gttsx import FalarGtts
from PDFCreate import ContractGenerate

bot = telepot.Bot("API_KEY_TELEGRAN")

#Envia a mensagem regada a partor do Gemini
def SendMessage(chatID, message):
    bot.sendMessage(chatID, message)

#Recebe a mensagem do telegran
def ReceiveMessage(msg):
    #Se mensagem de texto
    if('text' in msg):

        if("gerar contrato" in msg['text'].lower() or "criar contrato" in msg['text'].lower() or "crie um contrato" in msg['text'].lower() or "gere um contrato" in msg['text'].lower()):
            print("Em Telegran: ",msg['text'])
            resposta = GeminiBot(msg['text'])
            ContractGenerate(str(msg['chat']['id']),resposta)
            bot.sendDocument(msg['chat']['id'],open('Contrato.pdf', 'rb'))
            SendMessage(msg['chat']['id'], resposta)
        
        else:
            print("Em Telegran: ",msg['text'])
            resposta = GeminiBot(msg['text'])
            #ContractGenerate(str(msg['chat']['id']),resposta)
            #bot.sendDocument(msg['chat']['id'],open('Contrato.pdf', 'rb'))
            SendMessage(msg['chat']['id'], resposta)


    #Se mensagem de audio
    if('voice' in msg):        
        # ID do arquivo de voz
        file_id = msg['voice']['file_id']
        # Caminho de destino do arquivo
        destination = 'voz.ogg'
        # Faz o download do arquivo
        bot.download_file(file_id, destination)
        print("Arquivo de audio recebido, necessario conversão para interpretação",file_id)
        ConvertAudioOGGtoWAV()
       
        resposta = GeminiBot(AudioToText())

        FalarGtts(resposta)
        bot.sendAudio(msg['chat']['id'], open('audio.mp3', 'rb'))

        SendMessage(msg['chat']['id'],resposta)

bot.message_loop(ReceiveMessage)

while True:
    pass
