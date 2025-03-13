from datetime import datetime

import psutil
import subprocess
import time

import keyboard
import paramiko
import re
import paramiko

stop_thread = False
def key_listener():
    global stop_thread
    input("Nyomj meg egy billentyűt a leállításhoz...\n")
    stop_thread = True

def getting_server_info(time_to_wait_s, hostname, username, password):
    while not stop_thread:
        time.sleep(time_to_wait_s)

        result = get_system_stats_and_htop_output(hostname, username, password)
        if result:
            print(result)  # Csak akkor írjuk ki, ha nem üres


def get_system_stats_and_htop_output(host, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)

        stdin, stdout, stderr = ssh.exec_command(
            "python3 -c 'import psutil; import subprocess; "
            "print(psutil.cpu_percent(interval=1, percpu=True)); "
            "print(psutil.getloadavg()); "
            "print(subprocess.check_output([\"sensors\"], text=True))'"
        )

        output = stdout.read().decode().splitlines()
        if len(output) >= 2:
            cpu_percent = eval(output[0])
            cpu_load_avg = eval(output[1])
        else:
            cpu_percent = []
            cpu_load_avg = []

        sensors_output = "\n".join(output[2:])

        cpu_temp = "Hőmérséklet információ nem elérhető"
        adapter_temp = "Hőmérséklet információ nem elérhető"
        cpu_section = False
        adapter_section = False

        stdin, stdout, stderr = ssh.exec_command("top -b -n 1")
        top_output = stdout.read().decode()

        annotated_output = []

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

        result = (
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}\n"
            f"CPU homerseklet: {cpu_temp}\n"
            f"Adapter homerseklet: {adapter_temp}\n"
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
