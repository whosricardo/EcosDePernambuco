import pygame
import serial
import os

# Configuração da porta serial
arduino = serial.Serial('/dev/cu.usbmodem1301', 9600)  # Ajuste para sua plataforma

# Inicializa o mixer de áudio
pygame.mixer.init()

# Idioma atual (0 = Português, 1 = Inglês, 2 = Espanhol)
idioma_atual = 0

# Dicionário para mapear os comandos aos áudios
audios = {
    0: {  # Português
        "AUDIO_1": "audios/pt_audio1.mp3",
        "AUDIO_2": "audios/pt_audio2.mp3",
        "AUDIO_3": "audios/pt_audio3.mp3",
        "AUDIO_4": "audios/pt_audio4.mp3",
        "AUDIO_5": "audios/pt_audio5.mp3",
        "AUDIO_6": "audios/pt_audio6.mp3",
        "AUDIO_7": "audios/pt_audio7.mp3",
        "AUDIO_8": "audios/pt_audio8.mp3",

    },
    1: {  # Inglês
        "AUDIO_1": "audios/en_audio1.mp3",
        "AUDIO_2": "audios/en_audio2.mp3",
        "AUDIO_3": "audios/en_audio3.mp3",
        "AUDIO_4": "audios/en_audio4.mp3",
        "AUDIO_5": "audios/en_audio5.mp3",
        "AUDIO_6": "audios/en_audio6.mp3",
        "AUDIO_7": "audios/en_audio7.mp3",
        "AUDIO_8": "audios/en_audio8.mp3",
    },
    2: {  # Espanhol
        "AUDIO_1": "audios/es_audio1.mp3",
        "AUDIO_2": "audios/es_audio2.mp3",
        "AUDIO_3": "audios/es_audio3.mp3",
        "AUDIO_4": "audios/es_audio4.mp3",
        "AUDIO_5": "audios/es_audio5.mp3",
        "AUDIO_6": "audios/es_audio6.mp3",
        "AUDIO_7": "audios/es_audio7.mp3",
        "AUDIO_8": "audios/es_audio8.mp3",
    },
}

def tocar_audio(caminho_audio):
    if not os.path.exists(caminho_audio):
        print(f"Erro: Arquivo {caminho_audio} não encontrado.")
        return
    
    # Para o áudio atual antes de tocar o novo
    if pygame.mixer.music.get_busy():
        print("Parando áudio atual...")
        pygame.mixer.music.stop()
    
    # Carrega e toca o novo áudio
    pygame.mixer.music.load(caminho_audio)
    pygame.mixer.music.play()
    print(f"Tocando: {caminho_audio}")

# Loop principal para leitura da porta serial
while True:
    if arduino.in_waiting > 0:
        comando = arduino.readline().decode('utf-8').strip()
        print(f"Comando recebido: {comando}")

        # Processa comando de idioma
        if comando.startswith("LANG_"):
            try:
                idioma_atual = int(comando.split("_")[1])
                print(f"Idioma alterado para: {['Português', 'Inglês', 'Espanhol'][idioma_atual]}")
            except (ValueError, IndexError):
                print("Comando de idioma inválido recebido.")

        # Processa comando de áudio
        elif comando.startswith("AUDIO_"):
            if comando in audios[idioma_atual]:
                tocar_audio(audios[idioma_atual][comando])
            else:
                print(f"Áudio não encontrado para o comando: {comando}")

        # Comando desconhecido
        else:
            print(f"Comando desconhecido: {comando}")
