from gtts import gTTS
import playsound
import os

# message
message = "Welcome back awkward-student! Time for some burn out."
language = "en"

# gtts object and mp3 conversion
speech = gTTS(text=message, lang=language)
speech.save("welcome.mp3")

playsound.playsound("welcome.mp3")

print("welcome message played")

os.remove("welcome.mp3")
