import speech_recognition as virtual_assistant
import pyttsx3


listener = virtual_assistant.Recognizer()
voice_box = pyttsx3.init()

try:
    #file_handling: helps to open and close the file function.
    with virtual_assistant.Microphone() as source:
        print("what do you help with?...")
        voice_command = listener.listen(source)
        command = listener.recognize_google(voice_command)
except:
    pass
