import requests

TOKENBot = ''
link = 'https://api.telegram.org/bot' + TOKENBot + '/'
updateId = 0

def Action(Message):
    chatId = Message["message"]["chat"]["id"]
    messageFromUser = Message["message"]["text"]
    ActionAnswer(chatId,messageFromUser)

def ActionAnswer(chatId,text):
    if(text == '0'):
        SendMessage(chatId,'1')
    elif(text == '2'):
        SendMessage(chatId,'3')
    elif(text == '4'):
        SendMessage(chatId,'5')
    else:
        SendMessage(chatId,'Bye')

def SendMessage(chatId,text):
    requests.get(link + 'sendMessage?chat_id=' + str(chatId) + '&text='+ text)

while True:
    response = requests.get(link + 'getUpdates')
    if(len(response.json()["result"]) == 0):
        updateId = 0
    else:
        for i in response.json()["result"]:
            if(i["update_id"] > updateId):
                Action(i)
                updateId = i["update_id"]