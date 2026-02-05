from gtts import gTTS
from playsound import playsound

# Testando 
#tts = gTTS("Olá Mundo. Vamos construir nosso assistente", lang="pt-br")
#tts.save("dados/audio.mp3")
#playsound("dados/audio.mp3")

def cria_audio(mensagem):
    tts= gTTS(mensagem, lang="pt-br")
    tts.save("dados/mensagem.mp3")
    playsound("dados/mensagem.mp3")

# Testando função:
cria_audio("Aprendendo a criar um assistente virtual")

#Utilizando input:
frase = input("Digite a frase a ser falada:\n")
cria_audio(frase)

#Utilizando com Arquivo:
arquivo = open("dados/frases.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
cria_audio(conteudo)

#Funcionando perfeitamente, partindo agora para o reconhecimento