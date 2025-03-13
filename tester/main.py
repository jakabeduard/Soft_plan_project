# This is a sample Python script.
import json
import os
import re
import sys
import threading
import time

import paramiko

from tester.written_by_us.monitoring import getting_server_info
from written_by_us.create_testers import create_testers
from written_by_us.imap import fetch_and_save_email
from written_by_us.load_server_capacity import key_listener, load_server_capacity

from written_by_us.reset_server import cleaning_server
from written_by_us.smtp import send_email_with_attachment


# def print_active_threads(threads):
#     """Kiírja az aktuálisan futó szálak számát."""
#     while True:
#         time.sleep(1)
#         active_threads = threading.active_count()
#         threads = [t for t in threads if t.is_alive()]
#
#         # print(f"{' ' * (cols - len(f'Aktív szálak száma: {active_threads}'))}Aktív szálak száma: {active_threads}")
#         print(f"                                                                                                                                          Aktív szálak száma: {active_threads}")
#         print(f"                                                                                                                                      Aktív szálak száma: {len(threads)}")
#         if active_threads <= 1:  # Ha már csak a fő szál van futásban, akkor kiléphetünk
#             break
# stop=False
# def number_of_threads(threads):
#     while stop:
#          print(f"Started {len(threads)} threads for server load tasks.")
def get_active_threads(ssh_client):
    """Visszaadja az aktív szálak számát egy remote szerveren."""
    stdin, stdout, stderr = ssh_client.exec_command('ps -eLf | wc -l')
    # stdin, stdout, stderr = ssh_client.exec_command('ps -eLf | grep python')
    active_threads = int(stdout.read().decode().strip())  # a szálak száma
    return active_threads


def monitor_active_threads(hostname, username, password):


    """SSH kapcsolat létrehozása és az aktív szálak folyamatos monitorozása."""
    try:
        # SSH kapcsolat létrehozása
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, username=username, password=password)

        # Szálak monitorozása
        while True:
            active_threads = get_active_threads(ssh_client)

            print(
                f"                                                                                                                                          Aktív szálak száma: {active_threads}")

            # Ha már csak a fő szál fut (ami a rendszer által alapértelmezett), kiléphetünk
            if active_threads <= 1:
                print("Nincsenek aktív szálak, kilépés.")
                break

            time.sleep(1)  # 1 másodperc várakozás, hogy ne terhelje túl a rendszert

        # SSH kapcsolat bontása
        ssh_client.close()

    except Exception as e:
        print(f"Hiba történt: {e}")


def count_errors_in_log(log_text):
    errors = {
        "too_many_connections": 0,
        # "none_lines": 0,
        # "high_threads": 0,
        # "high_cpu_temp": 0,
        # "high_cpu_usage": 0
    }

    lines = log_text.split("\n")

    for line in lines:
        # 1. "Too many connections" hibák számlálása
        if "Error: (421, b'4.7.0 edu.mailserver.ro Error: too many connections" in line:
            errors["too_many_connections"] += 1

        # # 2. "None" előfordulások
        # if line.strip() == "None":
        #     errors["none_lines"] += 1
        #
        # # 3. Aktív szálak számának figyelése
        # thread_match = re.search(r"Aktív szálak száma: (\d+)", line)
        # if thread_match:
        #     thread_count = int(thread_match.group(1))
        #     if thread_count > 1150 or thread_count < 1100:  # Példa: ha extrém érték
        #         errors["high_threads"] += 1
        #
        # # 4. CPU hőmérséklet figyelése
        # temp_match = re.search(r"CPU hőmérséklet: \+(\d+\.\d+)°C", line)
        # if temp_match and float(temp_match.group(1)) > 45.0:
        #     errors["high_cpu_temp"] += 1
        #
        # # 5. CPU magas használata
        # cpu_match = re.search(r"%Cpu\(s\):\s+(\d+\.\d+)\s+us", line)
        # if cpu_match and float(cpu_match.group(1)) > 80.0:
        #     errors["high_cpu_usage"] += 1

    return errors



if __name__ == '__main__':
    sys.stdout = open("output77.txt", "w", encoding="utf-8",errors="ignore")


    # log_path = "outputlh.txt"
    #
    # if not os.path.exists(log_path):
    #         print(f"Hiba: A(z) {log_path} fájl nem található!")
    # else:
    #     with open(log_path, "r", encoding="utf-8",errors="ignore") as log_file:
    #         log_content = log_file.read()
    #     error_counts = count_errors_in_log(log_content)
    #     for key, value in error_counts.items():
    #         print(f"{key}: {value}")



    api_key="E9A377-B0723B-53A5DC-D12E23-67E2F0"
    host_url="https://edu.mailserver.ro"
    host_sever="edu.mailserver.ro"
    ssh_user="admin"
    ssh_password="01234"
    n = 1000
    max_paragraphs=10
    wait_time=12

    # send_email_with_attachment(1,2,20,host_sever)
    # fetch_and_save_email(2,host_sever)

    ###################################################################


    # result = cleaning_server(host_url, api_key)
    # print(json.dumps(result, indent=4))

    ################################################


    # result = create_testers(n, host_url, api_key)
    # print(json.dumps(result, indent=4))


    # result= getting_server_info(1, host_sever, ssh_user,ssh_password)
    # print(json.dumps(result))

    # key_listener_thread = threading.Thread(target=key_listener)
    # key_listener_thread.start()


    # # Indítunk egy szálat a getting_server_info függvényhez
    # getting_server_info_thread = threading.Thread(target=getting_server_info, args=(1, host_sever, ssh_user,ssh_password))  # Módosítsd az argumentumokat a megfelelő értékekre
    # # getting_server_info_thread.daemon=True
    # getting_server_info_thread.start()
    # # Lista a szálak tárolására
    #
    #
    # active_thread_monitor = threading.Thread(target=monitor_active_threads,args=(host_sever,ssh_user,ssh_password))
    # # active_thread_monitor.daemon=True
    # active_thread_monitor.start()

    #

    num_threads = 2
    threads = []


    # Ciklusban elindítjuk a load_server_capacity szálakat
    for _ in range(num_threads):
        thread = threading.Thread(target=load_server_capacity, args=( n, max_paragraphs, host_sever))
        thread.start()
        # thread.daemon = True
        threads.append(thread)

    # Megvárjuk, hogy minden load_server_capacity szál befejeződjön
    for thread in threads:
        thread.join()
        print(thread)


    #
    # getting_server_info_thread.join()
    #
    # active_thread_monitor.join()
    #
    sys.stdout.close()

    # Indítunk egy szálat a load_server_capacity függvényhez
    # load_server_capacity_thread = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread.start()
    # load_server_capacity_thread2 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread2.start()
    # load_server_capacity_thread3 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread3.start()
    # load_server_capacity_thread4 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread4.start()
    # load_server_capacity_thread5 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread5.start()
    # load_server_capacity_thread6 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread6.start()
    # load_server_capacity_thread7 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread7.start()
    # load_server_capacity_thread8 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread8.start()
    # load_server_capacity_thread9 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread9.start()
    # load_server_capacity_thread10 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread10.start()
    # load_server_capacity_thread11 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread11.start()
    # load_server_capacity_thread12 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread12.start()
    # load_server_capacity_thread13 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread13.start()
    # load_server_capacity_thread14 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread14.start()
    # load_server_capacity_thread15 = threading.Thread(target=load_server_capacity, args=(wait_time, n,  max_paragraphs, host_sever))  # Módosítsd az argumentumokat a megfelelő értékekre
    # load_server_capacity_thread15.start()
    #
    #
    #
    # # Várjuk, hogy a szálak befejeződjenek
    # # key_listener_thread.join()
    # load_server_capacity_thread.join()
    # load_server_capacity_thread2.join()
    # load_server_capacity_thread3.join()
    # load_server_capacity_thread4.join()
    # load_server_capacity_thread5.join()
    # load_server_capacity_thread6.join()
    # load_server_capacity_thread7.join()
    # load_server_capacity_thread8.join()
    # load_server_capacity_thread9.join()
    # load_server_capacity_thread10.join()
    # load_server_capacity_thread11.join()
    # load_server_capacity_thread12.join()
    # load_server_capacity_thread13.join()
    # load_server_capacity_thread14.join()
    # load_server_capacity_thread15.join()
    # getting_server_info_thread.join()

#
# import json
# import threading
# import tkinter as tk
# from tkinter import scrolledtext, Label, Entry, Button
# import sys
# from io import StringIO
#
# from tester.written_by_us.monitoring import getting_server_info
# from written_by_us.create_testers import create_testers
# from written_by_us.load_server_capacity import key_listener, load_server_capacity
# from written_by_us.reset_server import cleaning_server
#
# def redirect_output(output_widget):
#     class StdoutRedirector(StringIO):
#         def write(self, message):
#             output_widget.insert(tk.END, message)
#             output_widget.see(tk.END)
#     return StdoutRedirector()
#
# def start_cleaning_server():
#     sys.stdout = redirect_output(cleaning_output)
#     result = cleaning_server(host_url_entry.get(), api_key_entry.get())
#     print(json.dumps(result, indent=4))
#     sys.stdout = sys.__stdout__
#
# def start_create_testers():
#     sys.stdout = redirect_output(testers_output)
#     result = create_testers(int(n_entry.get()), host_url_entry.get(), api_key_entry.get())
#     print(json.dumps(result, indent=4))
#     sys.stdout = sys.__stdout__
#
# def start_key_listener():
#     sys.stdout = redirect_output(key_listener_output)
#     threading.Thread(target=key_listener, daemon=True).start()
#     print("Key Listener started.")
#     sys.stdout = sys.__stdout__
#
# def start_load_server_capacity():
#     sys.stdout = redirect_output(server_load_output)
#     thread = threading.Thread(target=load_server_capacity, args=(int(wait_time_entry.get()), int(n_entry.get()), int(max_paragraphs_entry.get()), host_sever_entry.get()), daemon=True)
#     thread.start()
#     thread.join()
#     sys.stdout = sys.__stdout__
#
# def start_getting_server_info():
#     sys.stdout = redirect_output(server_info_output)
#     thread = threading.Thread(target=getting_server_info, args=(host_sever_entry.get(), ssh_user_entry.get(), ssh_password_entry.get()), daemon=True)
#     thread.start()
#     thread.join()
#     sys.stdout = sys.__stdout__
#
# # GUI Setup
# root = tk.Tk()
# root.title("Server Management Interface")
#
# frame = tk.Frame(root)
# frame.pack(pady=10)
#
# # Input Fields
# Label(frame, text="API Key:").grid(row=0, column=0)
# api_key_entry = Entry(frame)
# api_key_entry.grid(row=0, column=1)
# api_key_entry.insert(0, "E9A377-B0723B-53A5DC-D12E23-67E2F0")
#
# Label(frame, text="Host URL:").grid(row=1, column=0)
# host_url_entry = Entry(frame)
# host_url_entry.grid(row=1, column=1)
# host_url_entry.insert(0, "https://edu.mailserver.ro")
#
# Label(frame, text="Host Server:").grid(row=2, column=0)
# host_sever_entry = Entry(frame)
# host_sever_entry.grid(row=2, column=1)
# host_sever_entry.insert(0, "edu.mailserver.ro")
#
# Label(frame, text="SSH User:").grid(row=3, column=0)
# ssh_user_entry = Entry(frame)
# ssh_user_entry.grid(row=3, column=1)
# ssh_user_entry.insert(0, "admin")
#
# Label(frame, text="SSH Password:").grid(row=4, column=0)
# ssh_password_entry = Entry(frame, show='*')
# ssh_password_entry.grid(row=4, column=1)
# ssh_password_entry.insert(0, "01234")
#
# Label(frame, text="N:").grid(row=5, column=0)
# n_entry = Entry(frame)
# n_entry.grid(row=5, column=1)
# n_entry.insert(0, "5")
#
# Label(frame, text="Max Paragraphs:").grid(row=6, column=0)
# max_paragraphs_entry = Entry(frame)
# max_paragraphs_entry.grid(row=6, column=1)
# max_paragraphs_entry.insert(0, "10")
#
# Label(frame, text="Wait Time:").grid(row=7, column=0)
# wait_time_entry = Entry(frame)
# wait_time_entry.grid(row=7, column=1)
# wait_time_entry.insert(0, "2")
#
# # Buttons & Output Windows
# cleaning_output = scrolledtext.ScrolledText(frame, width=80, height=5)
# cleaning_output.grid(row=8, column=0, columnspan=2)
# Button(frame, text="Clean Server", command=start_cleaning_server).grid(row=9, column=0, padx=5, pady=5)
#
# testers_output = scrolledtext.ScrolledText(frame, width=80, height=5)
# testers_output.grid(row=10, column=0, columnspan=2)
# Button(frame, text="Create Testers", command=start_create_testers).grid(row=11, column=0, padx=5, pady=5)
#
# key_listener_output = scrolledtext.ScrolledText(frame, width=80, height=5)
# key_listener_output.grid(row=12, column=0, columnspan=2)
# Button(frame, text="Start Key Listener", command=start_key_listener).grid(row=13, column=0, padx=5, pady=5)
#
# server_load_output = scrolledtext.ScrolledText(frame, width=80, height=5)
# server_load_output.grid(row=14, column=0, columnspan=2)
# Button(frame, text="Load Server Capacity", command=start_load_server_capacity).grid(row=15, column=0, padx=5, pady=5)
#
# server_info_output = scrolledtext.ScrolledText(frame, width=80, height=5)
# server_info_output.grid(row=16, column=0, columnspan=2)
# Button(frame, text="Get Server Info", command=start_getting_server_info).grid(row=17, column=0, padx=5, pady=5)
#
# Button(frame, text="Exit", command=root.quit).grid(row=18, column=0, columnspan=2, padx=5, pady=5)
#
# root.mainloop()
