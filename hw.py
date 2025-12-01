import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import colorama
from colorama import Fore,Style

def speak(text,language="en"):
    engine=pyttsx3.init()
    engine.setProperty('rate',150)
    voices=engine.getProperty('voices')

    if language == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.BLUE +"Please speak now in English..." + Style.RESET_ALL)
        audio=recognizer.listen(source)

    try:
        print(Fore.GREEN +"Recognising speech..." + Style.RESET_ALL)
        text=recognizer.recognize_google(audio,language="en-US")
        print(Fore.BLUE + f"You said:{text}"+ Style.RESET_ALL)
        return text
    except sr.UnknownValueError:
        print(Fore.RED +"Could not understand the audio."+ Style.RESET_ALL)
    except sr.RequestError as e:
        print(f"API Error:{e}")
    return ""

def translate_text(text,target_language="es"):
    translator=Translator()
    translation=translator.translate(text,dest=target_language)
    print(Fore.GREEN +f"Translated text:{translation.text}"+ Style.RESET_ALL)
    return translation.text

def display_language_options():
    print(Fore.BLUE +"Available translation languages:"+ Style.RESET_ALL)
    print(Fore.YELLOW +"1.Hindi (hi)"+ Style.RESET_ALL)
    print(Fore.YELLOW +"2.Tamil (ta)"+ Style.RESET_ALL)
    print(Fore.YELLOW +"3.Telugu (te)"+ Style.RESET_ALL)
    print(Fore.YELLOW +"4.Bengali (bn)"+ Style.RESET_ALL)
    print(Fore.YELLOW +"5.Marathi (mr)"+ Style.RESET_ALL)
    print(Fore.YELLOW +"6.Gujarati (gu)"+ Style.RESET_ALL)
    print(Fore.YELLOW +"7.Malayalam (ml)"+ Style.RESET_ALL)
    print(Fore.YELLOW +"8.Punjabi (pa)"+ Style.RESET_ALL)

    choice=input(Fore.BLUE +"Please select the target language number (1-8):"+ Style.RESET_ALL)
    language_dict={
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa"
    }

    return language_dict.get(choice,"es")

def main():
    target_language=display_language_options()
    original_text=speech_to_text()

    if original_text:
        translated_text=translate_text(original_text,target_language=target_language)
        speak(translated_text,language="en")
        print(Fore.YELLOW +"Translation spoken out!"+Style.RESET_ALL)

if __name__ == "__main__":
    main()