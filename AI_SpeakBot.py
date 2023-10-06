import openai
import speech_recognition as sr
import pyttsx3
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....")
        audio = r.listen(source)
        said = ''
        r.pause_threshold = 1

        try:
            print("Recognizing....")
            said = r.recognize_google(audio , language='eng-in')
            print('You said : ',said)

        except Exception as e :

            print("Exception :" + str(e))

    return said


def speak():

    speak("Activating AI mode and Assigning Jarvis to You. ")

    speak("Your Grace!,its Jarvis here, command me")

    openai.api_key = "your API key"
    model_engine = "text-davinci-002"

    while True:
        prompt = get_audio()
        prompt = prompt.replace("Friday","")

        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )
        message = response["choices"][0]["text"]
        #message = message[message.index("\n") + 1:]
        speak(message)
        # print("Friday: " + message)