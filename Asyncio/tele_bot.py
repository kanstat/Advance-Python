from constants_ import BASE_URL
import requests
import json
from headlines import get_topheadlines



 
global msg_updateid_list  
msg_updateid_list = []

    
def get_updates():
    global msg_updateid_list 
    with open(r"Asyncio\last_update_id.txt","r") as f:
        read_last_update_id  = int(f.read())
        print(f"---------------Read update id = {read_last_update_id}----------------")
    update_url = f'{BASE_URL}/getUpdates'
    response = requests.get(update_url)
    response = response.text
    response = json.loads(response)

    print(f"len of result---{len(response['result'])}")
    print(f"complete result---{response['result']}")
    for itm in response["result"]:
        update_id = itm["update_id"]
        print(f"update_id -> {update_id}")
        user_txt = itm["message"]["text"]
        chat_id = itm["message"]["from"]["id"]
        if update_id>read_last_update_id:
            msg_updateid_list.append((update_id,user_txt,chat_id))
            with open(r"Asyncio\last_update_id.txt","w") as f:
                f.write(str(update_id))
                print(f"@@@@@@@@@@@@@@@@@@@@ Written update id = {update_id} @@@@@@@@@@@@@@@@@@@@")
    




def send_message():
    global msg_updateid_list
    while True:
        print(f"msg_updateid_list = {msg_updateid_list}")
        if len(msg_updateid_list)==0:
            get_updates()
            continue
        poped_item = msg_updateid_list.pop(0)
        update_id = poped_item[0]
        user_txt = poped_item[1]
        chat_id = poped_item[2]  
        if user_txt == "/start":
            text_to_user = "start, welcome to my news bot."      
            send_url = f"{BASE_URL}/sendMessage?chat_id={chat_id}&text={text_to_user}"
            res = requests.post(send_url)
        elif user_txt == "/news":
            text_to_user_lst = get_topheadlines()   
            for text_to_user in text_to_user_lst:   
                send_url = f"{BASE_URL}/sendMessage?chat_id={chat_id}&text={text_to_user}"
                res = requests.post(send_url)
        else:
            text_to_user = "Please choose options from menu."      
            send_url = f"{BASE_URL}/sendMessage?chat_id={chat_id}&text={text_to_user}"
            res = requests.post(send_url)
            
            # sleep(0.3)

if __name__ == "__main__":
    r = get_updates()   
    print(send_message())
    print(r)