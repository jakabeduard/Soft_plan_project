import msvcrt
import time
from datetime import datetime

# from written_by_us.get_and_send_emails import receive_n_per_2_email
from written_by_us.imap import fetch_and_save_email
from written_by_us.random_generator import random_number
from written_by_us.smtp import send_email_with_attachment

stop_thread = False
def key_listener():
    global stop_thread
    input("Nyomj meg egy billentyűt a leállításhoz...\n")
    stop_thread = True

def load_server_capacity( n_emails,max_paragraphs,host_sever):
    while not stop_thread:

        # print(f"{time_to_wait_s} másodperc eltelt!")
        wait = random_number(1,20 )
        print("Aktuális idő:", datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
        print(f"{wait}-másodperc  várakozás\n")

        time.sleep(wait)


        # Meghívok max n/2 email felhasználót, hogy küldjenek emailt a másik n/2-nek

        sender_num = random_number(0, n_emails)
        print(f"          {sender_num}- Küldő \n")
            #fogadok szama
        receiver_num=random_number(0,n_emails)
        print(f"                      {receiver_num}- Fogadó\n")

        if(sender_num==receiver_num):continue
        print( datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
        send_email_with_attachment(sender_num, receiver_num, max_paragraphs, host_sever)

        print( datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
        fetch_and_save_email(receiver_num, host_sever)

