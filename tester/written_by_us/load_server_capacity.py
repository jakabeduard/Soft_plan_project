import msvcrt
import time

from written_by_us.get_and_send_emails import receive_n_per_2_email, send_n_per_2_email
from written_by_us.random_generator import random_number


# # def set_n_for_load(n_email):
# #     global n_emails
# #     n_emails=n_email
#
# stop_thread = False
#
# # Gombnyomás figyelése külön szálon
# def key_listener():
#     global stop_thread
#     input("Nyomj meg egy billentyűt a leállításhoz...\n")
#     stop_thread = True
#
#
# def load_server_capacity(time_to_wait_s,n_emails):
#     while not stop_thread:
#
#             # N perc várakozás
#         print(f"{time_to_wait_s} masodperc eltelt!")
#         time.sleep(time_to_wait_s)  # `n` masodperc várakozás (perc * 60 másodperc)
#
#         #meghivok max  n/2 email felhasznalot    hogy  kuldjon  email a  masik n/2 nek
#         activ_emails=random_number(1, n_emails/2)
#
#         for i in range(activ_emails//2):  # n/2-től fut a ciklus
#             #kuldok szama
#             sender_num=random_number(0,n_emails)
#
#             #fogadok szama
#             receiver_num=random_number(0,n_emails)
#
#             if(sender_num==receiver_num):continue
#
#             send_n_per_2_email(sender_num, receiver_num)
#             receive_n_per_2_email(receiver_num)
#
#
#
stop_thread = False
def key_listener():
    global stop_thread
    input("Nyomj meg egy billentyűt a leállításhoz...\n")
    stop_thread = True

def load_server_capacity(time_to_wait_s, n_emails):
    while not stop_thread:
        time.sleep(time_to_wait_s)
        print(f"{time_to_wait_s} másodperc eltelt!")
        activ_emails = random_number(1, int(n_emails / 2))

        # Meghívok max n/2 email felhasználót, hogy küldjenek emailt a másik n/2-nek
        for i in range(activ_emails // 2):  # n/2-től fut a ciklus
            print("Üdvözöllek!")
            # kuldok szama
            sender_num = random_number(0, n_emails)

            #fogadok szama
            receiver_num=random_number(0,n_emails)
        #
            if(sender_num==receiver_num):continue
        #
            send_n_per_2_email(sender_num, receiver_num)
            receive_n_per_2_email(receiver_num)
