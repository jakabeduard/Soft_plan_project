from datetime import datetime

import psutil
import subprocess
import time

import keyboard
import paramiko
import re
import paramiko

from written_by_us import config

def actual_time():
    while config.running:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f\n")[:-3])
        time.sleep(600)




def getting_server_info(time_to_wait_s, hostname, username, password):
    while config.running:
        # time.sleep(time_to_wait_s)

        result = get_system_stats_and_htop_output(hostname, username, password)
        if result:
            print(result)  # Csak akkor írjuk ki, ha nem üres
        time.sleep(time_to_wait_s)


def get_system_stats_and_htop_output(host, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)

        # Get CPU per-core percent, load average, and temperature
        stdin, stdout, stderr = ssh.exec_command(
            "python3 -c 'import psutil; import subprocess; "
            "print(psutil.cpu_percent(interval=1, percpu=True)); "
            "print(psutil.cpu_percent(interval=1)); "  # Overall CPU load
            "print(psutil.getloadavg()); "
            "print(subprocess.check_output([\"sensors\"], text=True))'"
        )

        output = stdout.read().decode().splitlines()

        if len(output) >= 3:
            cpu_percent = eval(output[0])
            overall_cpu_percent = eval(output[1])  # Overall CPU usage
            cpu_load_avg = eval(output[2])
        else:
            cpu_percent = []
            overall_cpu_percent = 0
            cpu_load_avg = []

        sensors_output = "\n".join(output[3:])

        cpu_temp = "Hőmérséklet információ nem elérhető"
        adapter_temp = "Hőmérséklet információ nem elérhető"
        cpu_section = False
        adapter_section = False

        stdin, stdout, stderr = ssh.exec_command("top -b -n 1")
        top_output = stdout.read().decode()

        annotated_output = []

        # Parse temperature information and top output
        for line in sensors_output.splitlines() + top_output.splitlines():
            if "cpu_thermal-virtual-0" in line:
                cpu_section = True
                adapter_section = False
            elif "rp1_adc-isa-0000" in line:
                cpu_section = False
                adapter_section = True

            if cpu_section and "temp1" in line:
                cpu_temp = line.split()[1]
            if adapter_section and "temp1" in line:
                adapter_temp = line.split()[1]

            if line.startswith("%Cpu(s):"):
                annotated_output.append(f"CPU hasznalat: {line}")
            elif line.startswith("MiB Mem :"):
                annotated_output.append(f"Memoria hasznalat: {line}")
            elif line.startswith("MiB Swap:"):
                annotated_output.append(f"Swap memoria hasznalat: {line}")

        # Prepare final result
        result = (
                # f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}\n"
                f"CPU homerseklet: {cpu_temp}\n"
                f"Adapter homerseklet: {adapter_temp}\n"
                f"CPU terheles (ossz): {overall_cpu_percent}%\n"  # Display overall CPU load
                f"CPU terheles (magonként) %-ban: {cpu_percent}\n"
                + "\n".join(annotated_output)
                + "\n"
        )

        return result

    except Exception as e:
        return f"Hiba történt: {e}"
    finally:
        ssh.close()
#elozo
# def getting_server_info( time_to_wait_s, hostname, username, password):
#     while not stop_thread:
#         # print("Végtelen ciklus fut...")
#
#
#
#         # result=get_remote_system_stats(hostname, username, password)
#         # print(result)
#         # result2=get_htop_output(hostname, username, password)
#         # print(result2)
#
#         result2=get_system_stats_and_htop_output(hostname, username, password)
#         print(result2)
#         time.sleep(time_to_wait_s)

#
#elozo
# def get_system_stats_and_htop_output(host, username, password):
#     try:
#         # Create SSH client
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect(host, username=username, password=password)
#
#         # Execute the remote script to get system stats
#         stdin, stdout, stderr = ssh.exec_command(
#             "python3 -c 'import psutil; import subprocess; "
#             "print(psutil.cpu_percent(interval=1, percpu=True)); "
#             "print(psutil.getloadavg()); "
#             "print(subprocess.check_output([\"sensors\"], text=True))'"
#         )
#
#         # Read and process the output
#         output = stdout.read().decode().splitlines()
#         cpu_percent = eval(output[0])
#         cpu_load_avg = eval(output[1])
#         sensors_output = "\n".join(output[2:])
#
#         # Extract CPU and adapter temperatures
#         cpu_temp = "Hőmérséklet információ nem elérhető"
#         adapter_temp = "Hőmérséklet információ nem elérhető"
#         cpu_section = False
#         adapter_section = False
#
#         # Execute the 'top' command with -b and -n 1 flags
#         stdin, stdout, stderr = ssh.exec_command("top -b -n 1")
#         top_output = stdout.read().decode()
#
#         # Annotated output list
#         annotated_output = []
#
#         for line in sensors_output.splitlines() + top_output.splitlines():
#             if "cpu_thermal-virtual-0" in line:
#                 cpu_section = True
#                 adapter_section = False
#             elif "rp1_adc-isa-0000" in line:
#                 cpu_section = False
#                 adapter_section = True
#
#             if cpu_section and "temp1" in line:
#                 cpu_temp = line.split()[1]
#             if adapter_section and "temp1" in line:
#                 adapter_temp = line.split()[1]
#
#             if line.startswith("%Cpu(s):"):
#                 annotated_output.append(f"CPU hasznalat: {line}")
#             elif line.startswith("MiB Mem :"):
#                 annotated_output.append(f"Memória hasznalat: {line}")
#             elif line.startswith("MiB Swap:"):
#                 annotated_output.append(f"Swap memoria allapot: {line}")
#
#         # Static variable outputs
#         cpu_temp_output = f"CPU homerseklet: {cpu_temp}"
#         adapter_temp_output = f"Adapter homersekle: {adapter_temp}"
#         cpu_usage_output = f"CPU terheles (magonkent) %-ban: {cpu_percent}"
#         # cpu_avg_load_output = f"CPU terhelés (átlag): {cpu_load_avg}"
#
#         # Print outputs
#         print(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
#         print(cpu_temp_output)
#         print(adapter_temp_output)
#         print(cpu_usage_output)
#         # print(cpu_avg_load_output)
#         print("\n".join(annotated_output))
#         print("\n")
#
#     except Exception as e:
#         print(f"Hiba tortent: {e}")
#     finally:
#         # Close the connection
#         ssh.close()


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
        while config.running:

            active_threads = get_active_threads(ssh_client)
            # print("                                                                                                                                         ",datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
            print(f"\nAktiv szalak szama: {active_threads}\n")

            # Ha már csak a fő szál fut (ami a rendszer által alapértelmezett), kiléphetünk
            if active_threads <= 1:
                print("Nincsenek aktív szálak, kilépés.")
                break

              # 1 másodperc várakozás, hogy ne terhelje túl a rendszert
            time.sleep(wait_time)

        # SSH kapcsolat bontása
        ssh_client.close()

    except Exception as e:
        print(f"Hiba történt: {e}")