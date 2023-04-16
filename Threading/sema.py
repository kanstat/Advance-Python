import threading
import time

obj = threading.Semaphore(4)

def print_hello(nameof_thread):
    for i in range(6):
        obj.acquire()
        print(f"Hello {nameof_thread} /n")
        time.sleep(5)
        obj.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=print_hello,args=("th1",))           
    t2 = threading.Thread(target=print_hello,args=("th2",))           
    t3 = threading.Thread(target=print_hello,args=("th3",))           
    t4 = threading.Thread(target=print_hello,args=("th4",))           
    t5 = threading.Thread(target=print_hello,args=("th5",))           

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    