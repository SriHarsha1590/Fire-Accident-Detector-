import pygame

def play_alert_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('alarm.mp3')  
    pygame.mixer.music.play()

if __name__ == "__main__":
    print("Fire detected! Playing sound alert...")
    play_alert_sound()
