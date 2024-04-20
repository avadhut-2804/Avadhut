import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Can you please repeat?")
        return get_info()
    except sr.RequestError:
        talk("Sorry, I'm unable to access the Google API at the moment.")
        return None


def send_email(receiver, subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Make sure to give app access in your Google account
        server.login('avadhutjagtap2804@gmail.com', 'jzoo fson skec ddgt')
        email = EmailMessage()
        email['From'] = 'avadhutjagtap2804@gmail.com'
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)
        talk('Hey, your email has been sent successfully!')
    except smtplib.SMTPAuthenticationError:
        talk("Oops! Authentication failed. Please check your email credentials.")
    except smtplib.SMTPException as e:
        talk(f"Sorry, something went wrong. Error: {e}")
    finally:
        server.quit()


email_list = {
    'praniket': 'jadhavpraneket@gmail.com',
    'bat': 'aratikhade2005@gmail.com',
    'anushka': 'anushkakadam05@gmail.com',
    'sanket': 'sanketkadam580@gmail.com',
    'irene': 'irene@redvelvet.com',
    'priyanka':'sapkalpriyanaka777@gmail.com'
}


def get_email_info():
    talk('To whom do you want to send the email?')
    name = get_info()
    if name in email_list:
        receiver = email_list[name]
        print(receiver)
        talk('What is the subject of your email?')
        subject = get_info()
        talk('Tell me the content of your email')
        message = get_info()
        send_email(receiver, subject, message)
        talk('Do you want to send more emails?')
        send_more = get_info()
        if 'yes' in send_more:
            get_email_info()
        else:
            talk('Okay, goodbye!')
    else:
        talk("Sorry, I don't know that contact. Please try again.")


get_email_info()