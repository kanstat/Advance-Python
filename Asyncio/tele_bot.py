from constants_ import *
import requests
import json




global msg_update_list  
msg_updateid_list = []

url = f'{BASE_URL}/getUpdates'
def get_updates(base_url):
    response = requests.get(base_url)
    response = response.text
    response = json.loads(response)
    for itm in response["result"]:
        update_id = itm["update_id"]
        user_txt = itm["message"]["text"]
        chat_id = itm["message"]["from"]["id"]
        msg_updateid_list.append((update_id,user_txt,chat_id))
        
        # print(user_txt,chat_id,update_id)
    return update_id,user_txt,chat_id
    




def send_message(chat_id, text):
    base_url = f"{BASE_URL}/sendMessage?chat_id={chat_id}&text={text}"
    if chat_id in msg_update_list:
        res = requests.post(base_url)
        return res
        
        

r = get_updates(url)    
print(r)