from speech_recognition import *
def audio_input():
    """
#return value is the string format of the voice input"""
    try:
        r = Recognizer()
        with Microphone() as source:
            inp = r.listen(source)
        a = r.recognize_google(inp)
        return a

    except UnknownValueError:
        print("please repeat your input")
        return(audio_input())


print(audio_input())
