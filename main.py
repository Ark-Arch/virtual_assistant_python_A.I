import speech_recognition as virtual_assistant

listener = virtual_assistant.Recognizer()

try:
    #file_handling: helps to open and close the file function.
    with virtual_assistant.Microphone() as source:
        print("what do you help with?...")
        voice_command = listener.listen(source)
        command = listener.recognize_google(voice_command)
        print(command)
except:
    pass
