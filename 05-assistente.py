from random import randint
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import sys
import so_funcoes
import noticias_funcao

def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

def executa_comandos(acao):
    if "fechar assistente" in acao:
        sys.exit()
    elif "horas" in acao:
        cria_audio("dados/mensagem.mp3", so_funcoes.verifica_hora())
    elif "desligar computador" in acao and "uma hora" in acao:
        so_funcoes.desliga_computador_uma_hora()
    elif "desligar computador" in acao and "meia hora" in acao:
        so_funcoes.desliga_computador_meia_hora()
    elif "cancelar desligamento" in acao:
        so_funcoes.cancela_desligamento()
    elif "notícias" in acao:
        cria_audio("dados/mensagem.mp3", noticias_funcao.ultimas_noticias())
        

def monitora_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Diga alguma coisa: ")
            audio = recon.listen(source)
            try:
                mensagem = recon.recognize_google(audio, language="pt-br")
                mensagem = mensagem.lower()
                print("Você disse: ", mensagem)
                executa_comandos(mensagem)
                break
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
        return mensagem
    
def main():
    cria_audio("dados/welcome.mp3", "Olá, sou lídia. Em que posso te ajudar hoje?")
    while True:
        monitora_audio()
main()