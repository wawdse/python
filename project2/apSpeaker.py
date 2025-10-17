import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from scrapping import weather, exchange, stock
import time

#문자를 소리로 출력(gtts)
def speak(text):
    print('[인공지능]' + text)
    tts = gTTS(text=text, lang='ko')
    file_name = 'data/voice.mp3'
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

#음성을 문자로 출력
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[홍길동]' + text)
        answer(text, stop)
    except sr.UnknownValueError:
        print('인식실패')
    except sr.RequestError:
        print('요청실패')

#문자를 입력 받아 인공지능이 대답
def answer(text, stop):
    answer_text = ''
    if '종료' in text:
        answer_text = '다음에 또 만나요.' 
        speak(answer_text)
        stop(wait_for_stop=False)
        os._exit(0)
    elif '주식' in text:
        index = text.find('주식')
        query = text[:index + 2]
        price = stock(query)
        answer_text = f'{query}의 가격은 {price}원 입니다.'
    elif '환율' in text:
        rate = exchange()
        answer_text='1달러 환율은 ' + rate + '원 입니다.'
    elif '날씨' in text:
        index = text.find('날씨')
        query = text[:index + 2]
        temp = weather(query)
        answer_text = f'{query}의 기온은 {temp}입니다.'
    elif '안녕' in text:
        answer_text='안녕하세요! 반갑습니다.'
    else:
        answer_text='다시 한번 말씀해 주시겠어요?'

    speak(answer_text)

speak('무엇을 도와드릴까요?')
mic = sr.Microphone()
stop = sr.Recognizer().listen_in_background(mic, listen)

while True:
    time.sleep(0.5)