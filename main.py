import os
import speech_recognition
from dotenv import load_dotenv
import telegram
from chat_dict import CHAT_DICT
from image_dict import IMG_DICT

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = ''

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def send_message(bot, message, CHAT_ID):
    try:
        bot.send_message(CHAT_ID, message)
    except Exception:
        return 'OOOpsss...Ошибка отправки'

def send_photo(bot, photo, CHAT_ID):
    try:
        bot.send_photo(CHAT_ID, photo)
    except Exception:
        return 'UUUUHHHHH.... Неудача'

def listen_comand():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.1)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'OOOpss....Я тебя не понял'


def main():
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    query = listen_comand()
    print(query)
    
    if query in CHAT_DICT.keys():
        CHAT_ID = CHAT_DICT.get(query)
    print(CHAT_ID)
    message = listen_comand()
    print(message)
    send_message(bot, message, CHAT_ID)
    choise_photo = listen_comand()
    if choise_photo in IMG_DICT.keys():
        name_photo = IMG_DICT.get(choise_photo)
        print(name_photo)
        photo = open(f'{name_photo}', 'rb')
        send_photo(bot, photo, CHAT_ID)
    else:
        return 'OOOOPPPPSSS.....'




if __name__ == '__main__': 

    main() 
