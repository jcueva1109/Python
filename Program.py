from flask import Flask
from flask import request
from flask import Response
import requests

TOKEN = "5533094697:AAGT64X9wimKTC1s36GaZ3TtKJTm2RiItaM"
app = Flask(__name__)

def tel_parse_message(message):
    print("message ---> ",message)
    try: 
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        print("chat_id ---> ",chat_id)
        print("txt ---> ",txt)
        return chat_id,txt
    except:
        print("NO text found -->>")

    try:
        cha_id = message['callback_query']['from']['id']
        i_txt = message['callback_query']['data']
        print("chat_id -->>", cha_id)
        print("i_txt -->>", i_txt)

        return cha_id, i_txt
    except:
        pass

def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {

        'chat_id': chat_id,
        'text': text

    }

    r = requests.post(url,json=payload)
    return r

def tel_send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg",
        'caption': "This is a sample image"
    }

    r = requests.post(url,json=payload)
    return r

def send_logo(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://i.ibb.co/QY8nwpJ/Starnel-Logo.png",
        'caption': "Hola! Gracias por comunicarte con el asistente virtual de Starnel."
    }

    r = requests.post(url,json=payload)
    return r

def tel_send_audio(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'
    payload = {

        'chat_id': chat_id,
        "audio": "http://www.largesound.com/ashborytour/sound/brobob.mp"

    }

    r = requests.post(url, json=payload)
    return r

def tel_send_video(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendVideo'
    payload = {

        'chat_id': chat_id,
        "video": "https://www.appsloveworld.com/wp-content/uploads/2018/10/640.mp4"
    
    }

    r = requests.post(url, json=payload)
    return r

def tel_send_document(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
    payload = {

        'chat_id': chat_id,
        "document": "http://www.africau.edu/images/default/sample.pdf"

    }

    r = requests.post(url, json=payload)
    return r

def tel_send_button(chat_id):
    url=f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload={
        'chat_id': chat_id,
        'text': "What is this?",
                'reply_markup':{ 'keyboard': [[{'text':supa}, {'text':'mario'}]]}
    }

    r = requests.post(url,json=payload)

    return r

def tel_send_inlinebutton(chat_id):
    url=f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload={

        'chat_id': chat_id,
        'text': "¿Dime en que te puedo apoyar?",
        'reply_markup': {

            "inline_keyboard": [[

                {
                    "text":"Quienes somos",
                    "callback_data": "Quienes_Somos"
                },
                {
                    "text": "Contactanos",
                    "callback_data": "Contactanos"
                },
                {
                    "text": "Cuentas Netflix",
                    "callback_data": "Cuentas_Netflix"
                }

            ]]
        }
    }

    r = requests.post(url,json=payload)
    return r

def tel_send_inlineurl(chat_id):
    url=f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {

        'chat_id': chat_id,
        'text': "Which link would you like to visit?",
        'reply_markup': {

            "inline_keyboard": [
                [
                    {"text": "google", "url": "https://www.google.com/"},
                    {"text": "youtube","url": "https://youtube.com"}
                ]
            ]
        }
    }

    r = requests.post(url, json=payload)
    return r

@app.route('/', methods=['GET','POST'])
def index():
    
    if request.method == 'POST':
        msg = request.get_json()
        
        try:
            chat_id,txt = tel_parse_message(msg)

            #Start bot with avatar
            if txt == "Hola!":
                send_logo(chat_id)
            elif txt == "Image":
                tel_send_image(chat_id)
            elif txt == "Audio":
                tel_send_audio(chat_id)
            elif txt == "Video":
                tel_send_video(chat_id)
            elif txt == "Document":
                tel_send_document(chat_id)
            elif txt == "Button":
                tel_send_button(chat_id)
            elif txt == "menu":
                tel_send_inlinebutton(chat_id)
            elif txt == "InlineUrl":
                tel_send_inlineurl(chat_id)
            elif txt == "Quienes_Somos":
                tel_send_message(chat_id, "Somos Starnel.")
            elif txt == "Contactanos":
                tel_send_message(chat_id, "Encuentranos en Instagram como @starnel_serviciosonline")
            elif txt == "Cuentas_Netflix":
                tel_send_message(chat_id, "Seleccionaste cuentas de netflix.")
            elif txt == "Adios!":
                tel_send_message(chat_id, "¡Hasta pronto! Gracias por tu preferencia.")
            else:
                tel_send_message(chat_id, 'from webhook')
        except:
            print("from index-->>")
        return Response('ok',status=200)
    
    else:
        return "<h1>An error has occured!</h1>"

if __name__ == '__main__':
    app.run(debug=True)

# Setup webhook
# https://api.telegram.org/bot5533094697:AAGT64X9wimKTC1s36GaZ3TtKJTm2RiItaM/setWebhook?url=https://ad7a-200-52-150-51.ngrok.io