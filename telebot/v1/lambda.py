import json
import requests

TELE_TOKEN='API'
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    requests.get(url)

def lambda_handler(event, context):
    request_body = json.loads(event['body'])
    chat_id = request_body['message']['chat']['id']
    command_arguments = request_body['message']['text'].split()
    command = command_arguments[0]
    
    if command == "/start":
        send_message("Hello there! What is your name?", chat_id)
    elif (command.upper().lower())=="dania" or (command.upper().lower())=="daniel":
        send_message("Oh, Hello Sir! Wanna learn how to do the same bot by yourself? Yes or no?", chat_id)
    elif (command.upper().lower())=="yes":
        send_message("Then let's start our learning! Call me!", chat_id)
    else:
        send_message("I don't know this response, try again!", chat_id)

    return {
        'statusCode': 200
    }
