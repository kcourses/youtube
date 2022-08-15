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
        send_message("Hello there! Wanna learn how to do the same bot by yourself?", chat_id)
    elif (command.upper().lower())=="yes":
        send_message("Then let's start our learning! Subscribe to the Architects diary channel!", chat_id)
    else:
        send_message("I don't know this response, try again!", chat_id)

    return {
        'statusCode': 200
    }
