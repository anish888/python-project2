#importing pyttsx3 library for converting text to speech
import pyttsx3
#here  sapi5 is the speech api
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
#fuction for converting text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
if __name__ == '__main__':
    speak(input('enter your text to speech'))