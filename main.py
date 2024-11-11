import pygame
import serial

# Configuração da porta serial (substitua 'COM3' pela correta)
arduino = serial.Serial('COM3', 9600)  # Para Windows
# arduino = serial.Serial('/dev/ttyUSB0', 9600)  # Para Linux/Mac

# Inicializa o mixer de áudio
pygame.mixer.init()

# Dicionário para mapear os comandos aos áudios
audios = {
    "AUDIO_1": "audios/audio1.mp3",
    "AUDIO_2": "audios/audio2.mp3",
    "AUDIO_3": "audios/audio3.mp3",
    "AUDIO_4": "audios/audio4.mp3",
    "AUDIO_5": "audios/audio5.mp3",
    "AUDIO_6": "audios/audio6.mp3",
    "AUDIO_7": "audios/audio7.mp3",
    "AUDIO_8": "audios/audio8.mp3",
}

def tocar_audio(caminho_audio):
    # Carrega o áudio
    pygame.mixer.music.load(caminho_audio)
    # Reproduz o áudio
    pygame.mixer.music.play()
    # Aguarda até o áudio terminar
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Loop principal para leitura da porta serial
while True:
    if arduino.in_waiting > 0:
        comando = arduino.readline().decode('utf-8').strip()
        print(f"Comando recebido: {comando}")

        # Verifica se o comando corresponde a um áudio
        if comando in audios:
            caminho_audio = audios[comando]
            print(f"Tocando: {caminho_audio}")
            tocar_audio(caminho_audio)
        else:
            print(f"Comando desconhecido: {comando}")
