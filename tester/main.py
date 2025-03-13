# This is a sample Python script.
import json
import os
import re
import sys
import threading
import time
from datetime import datetime

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


def monitor_active_threads(wait_time, hostname, username, password):


    """SSH kapcsolat létrehozása és az aktív szálak folyamatos monitorozása."""
    try:
        # SSH kapcsolat létrehozása
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, username=username, password=password)

        # Szálak monitorozása
        while True:
            time.sleep(wait_time)
            active_threads = get_active_threads(ssh_client)
            print("                                                                                                                                         ",datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
            print(f"                                                                                                                                          Aktiv szalak szama: {active_threads}\n")

            # Ha már csak a fő szál fut (ami a rendszer által alapértelmezett), kiléphetünk
            if active_threads <= 1:
                print("Nincsenek aktív szálak, kilépés.")
                break

              # 1 másodperc várakozás, hogy ne terhelje túl a rendszert

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
    sys.stdout = open("output7safsdkl.txt", "w", encoding="utf-8", errors="ignore")

    print("Hello,g!")



    # api_key="E9A377-B0723B-53A5DC-D12E23-67E2F0"
    # host_url="https://edu.mailserver.ro"
    # host_sever="edu.mailserver.ro"
    # ssh_user="admin"
    # ssh_password="01234"
    # n = 1000
    # max_paragraphs=10
    # wait_time=5
    #
    # # send_email_with_attachment(1,2,20,host_sever)
    # # fetch_and_save_email(2,host_sever)
    #
    # ###################################################################
    #
    #
    # # result = cleaning_server(host_url, api_key)
    # # print(json.dumps(result, indent=4))
    #
    # ################################################
    #
    #
    # # result = create_testers(n, host_url, api_key)
    # # print(json.dumps(result, indent=4))
    #
    #
    # # result= getting_server_info(1, host_sever, ssh_user,ssh_password)
    # # print(json.dumps(result))
    #
    # # key_listener_thread = threading.Thread(target=key_listener)
    # # key_listener_thread.start()
    #
    # #
    # # Indítunk egy szálat a getting_server_info függvényhez
    # getting_server_info_thread = threading.Thread(target=getting_server_info, args=(wait_time, host_sever, ssh_user,ssh_password))  # Módosítsd az argumentumokat a megfelelő értékekre
    # # getting_server_info_thread.daemon=True
    # getting_server_info_thread.start()
    # # Lista a szálak tárolására
    #
    #
    # active_thread_monitor = threading.Thread(target=monitor_active_threads,args=(wait_time,host_sever,ssh_user,ssh_password))
    # # active_thread_monitor.daemon=True
    # active_thread_monitor.start()
    #
    #
    #
    # num_threads = 2
    # threads = []
    #
    #
    # # Ciklusban elindítjuk a load_server_capacity szálakat
    # for _ in range(num_threads):
    #     thread = threading.Thread(target=load_server_capacity, args=( n, max_paragraphs, host_sever))
    #     thread.start()
    #     # thread.daemon = True
    #     threads.append(thread)
    #
    # # Megvárjuk, hogy minden load_server_capacity szál befejeződjön
    # for thread in threads:
    #     thread.join()
    #     print(thread)
    #
    #
    #
    # getting_server_info_thread.join()
    #
    # active_thread_monitor.join()

    sys.stdout.close()
