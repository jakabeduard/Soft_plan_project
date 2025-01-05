import paramiko
import time
import keyboard  # A keyboard könyvtár importálása

def get_server_info_ssh(hostname, username, password):
    """
    SSH-n keresztül lekéri a szerver hardverinformációit 30 Hz-es frissítéssel végtelen ciklusban.
    A ciklus leáll, ha bármilyen billentyűt lenyomsz.

    Args:
        hostname (str): A szerver címe.
        username (str): Az SSH felhasználónév.
        password (str): Az SSH jelszó.
    """
    try:
        # SSH kapcsolat létrehozása
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)

        commands = {
            "cpu_capacity": "lscpu | grep 'Model name'",
            "memory_capacity": "free -h | grep 'Mem:'",
            "temperature": "sensors | grep 'Package id 0:'"
        }

        while True:
            # Ellenőrizzük, hogy lenyomtak-e egy billentyűt
            if keyboard.is_pressed():  # Ha bármilyen billentyű lenyomásra kerül
                print("Kilépés a programból...")
                break  # Kilépés a ciklusból

            start_time = time.time()

            results = {}
            for key, command in commands.items():
                stdin, stdout, stderr = client.exec_command(command)
                results[key] = stdout.read().decode().strip()

            # Eredmények kiírása
            print("CPU Kapacitás:", results.get("cpu_capacity", "N/A"))
            print("Memória Kapacitás:", results.get("memory_capacity", "N/A"))
            print("Hőmérséklet:", results.get("temperature", "N/A"))
            print("-" * 40)

            # 30 Hz-es frissítés
            elapsed_time = time.time() - start_time
            sleep_time = max(0, (1 / 30) - elapsed_time)
            time.sleep(sleep_time)

        client.close()

    except Exception as e:
        print(f"Hiba történt: {str(e)}")

