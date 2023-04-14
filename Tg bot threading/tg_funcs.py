import json
import requests
from const import TGURL
from news_funcs import get_news
import threading
from threading import Lock


global lst_upd_id,q 
lst_upd_id = 0
q = []

lock = Lock()


def update_id():
    global lst_upd_id, q
    while True:
        upd_url = f"{TGURL}/getUpdates"
        res = requests.get(upd_url)
        res = json.loads(res.text)
        for itm in res["result"]:
            upd_id = itm["update_id"]
            if lst_upd_id == 0 or upd_id >lst_upd_id:
                usr_txt = itm["message"]["text"]
                chat_id = itm["message"]["from"]["id"]
                lock.acquire()
                q.append((upd_id,usr_txt,chat_id))
                lock.release()
                lst_upd_id = upd_id

def sender_func():
    global q
    while True:
        if q:
            lock.acquire()
            q_res = q.pop(0)
            lock.release()
            upd_id = q_res[0]
            usr_txt = q_res[1]
            chat_id = q_res[2]
            
            if usr_txt == "hello" or usr_txt =="/start":
                txt_to_snd = r"Welcome to my bot, please send /news for some latest top news headlines" 
                threading.Thread(target=send_all_msgs,args=(chat_id,txt_to_snd),name="send_all_msgs1").start()     
            if usr_txt == "/news":
                txt_to_snd_lst = get_news() 
                print(*txt_to_snd_lst)
                threading.Thread(target=send_all_msgs,args=(chat_id,*txt_to_snd_lst),name="send_all_msgs2").start()
                
              
def send_msg(chat_id,txt_to_snd):
    try:
        print("sending messg..")
        requests.post(f"{TGURL}/sendMessage?chat_id={chat_id}&text={txt_to_snd}")
    except Exception as e:
        print(e)

def send_all_msgs(chat_id,*args):
    try:
        for msg_to_snd in args:
            print(f"{TGURL}/sendMessage?chat_id={chat_id}&text={msg_to_snd}")
            threading.Thread(target=send_msg,args=(chat_id,msg_to_snd),name="send_msg")
    except Exception as e:
        print(e)
        raise Exception("Error in send_all_mssg")
                
                
if __name__ == "__main__":
    threading.Thread(target=update_id,name="updater").start()
    threading.Thread(target=sender_func,name="sendr").start()