import soundfile as sf

#Função para converter o codec de audio de OGG para WAV
def ConvertAudioOGGtoWAV():
    # Carregue o arquivo OGG
    ogg_data, samplerate = sf.read("voz.ogg")

    # Converta o OGG para WAV
    wav_data = sf.write("voz.wav", ogg_data, samplerate=samplerate, format="WAV")


