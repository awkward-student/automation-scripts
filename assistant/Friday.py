# install text to speech:
# pip install pyttsx3;
import pyttsx3

# install speech recog
# pip install speechrecognition
import speech_recognition as sr


# assistanst's speak/talk function:
# MOUTH ++++++++++++++++++++++++++
def speak(text):

    # creating a engine
    engine = pyttsx3.init()

    # getting list of voices to choose from for my assistant:
    voices = engine.getProperty('voices')

    # to get name and id of the available assistant voices in pyttsx3 i'm using for loop over list of voices and printing them: 
    # for v in voices:
        # print(v.id, ": ", v.name)

    # got this two preavailable voices:
    # HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0 :  Microsoft David Desktop - English (United States)
    # HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0 :  Microsoft Zira Desktop - English (United States)

    # going to use female assistant so going with Zira:
    ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

    engine.setProperty('voice', ID)

    # printing text to console:
    print("")

    print(f"--> CHARVI: {text}")

    engine.say(text=text)

    engine.runAndWait()

 
# assistant's speech recognition:
# this will only listen and record audio
# EARS +++++++++++++++++++++++++++++++++
def speechRecognition():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("")

        print("Listening .....")
        
        r.pause_threshold = 1
        
        audio = r.listen(source, 0, 8)

    try:

        print("Recognizing ...")

        query = r.recognize_google(audio, language="en")

        # printing text to console:
        print("")

        print(f"--> USER: {query.lower()}")

        return query.lower()
    
    except:

        return ""


# assistant's brain:
# will start with basic if-else statements for processing
# BRAIN +++++++++++++++++++++++++++++++++++++++++++++++++
def mainExecution(query):

    query = str(query).lower()

    if "hello" in query:
        speak("Hello sir! Good to have you back as always.")
    
    elif "bye" in query:
        speak("Goodbye sir! See you soon.")

# system code below:
    
# testing speaking:
# speak("Hello sir!")


# testing speech recog:
# print(speechRecognition())
        

# testing main execution:
run = True

while run:

    mainExecution(speechRecognition())