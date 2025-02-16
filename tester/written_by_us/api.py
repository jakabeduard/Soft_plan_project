
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def get_domanin_all(host, api_key):
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    URL_GET_ALL_DOMAIN = f"{host}/api/v1/get/domain/all"
    try:
        response = requests.get(URL_GET_ALL_DOMAIN , headers=headers, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_mailbox_all(host, api_key):
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    URL_GET_ALL_MAILBOX = f"{host}/api/v1/get/mailbox/all"
    try:
        response = requests.get(URL_GET_ALL_MAILBOX, headers=headers, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def delete_mailboxes(email_list,host, api_key):
    # Az API végpont
    URL_DELETE_EMAIL_ADDRESSES = f"{host}/api/v1/delete/mailbox"
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}

    try:
        # POST kérés küldése az email címek listájával
        response = requests.post(URL_DELETE_EMAIL_ADDRESSES, headers=headers, json=email_list, verify=False)

        # Ellenőrizzük, hogy sikeres volt-e a kérés
        if response.status_code == 200:
            response_data = response.json()
            for item in response_data:
                if item["type"] == "success":
                    print(f"Success: {item['msg']}")
                    print(f"Log: {item['log']}")
                else:
                    print(f"Error: {item['msg']}")
        else:
            print(f"Request failed with status code {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")




def delete_domains(domains,host, api_key):
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    URL_DELETE_DOMAINS = f"{host}/api/v1/delete/domain"
    # URL_DELETE_DOMAINS = "https://edu.mailserver.ro/api/v1/delete/domain"
    print("URL:", URL_DELETE_DOMAINS)
    print("Headers:", headers)
    print("Body:", domains)

    try:
        response = requests.post(URL_DELETE_DOMAINS, headers=headers, json=domains, verify=False)

        if response.status_code == 200:
            response_data = response.json()
            for item in response_data:
                if item["type"] == "success":
                    print(f"Success: {item['msg']}")
                    print(f"Log: {item['log']}")
                else:
                    print(f"Error: {item['msg']}")
        elif response.status_code == 403:
            print("Error: Forbidden - Check your API key or permissions.")
        elif response.status_code == 401:
            print("Error: Unauthorized - API key might be invalid.")
        else:
            print(f"Request failed with status code {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")




def create_domain(host, api_key):
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    CREATE_DOMAIN_API_URL = f"{host}/api/v1/add/domain"

    CREATE_DOMAIN_BODY = {
        "domain": "test.com",
        "description": "test",
        "aliases": 400,
        "mailboxes": 1000,
        "defquota": 3072,
        "maxquota": 110240,
        "quota": 110240,
        "active": True,
        "rl_value": 999999999999,
        "rl_frame": "s",
        "backupmx": False,
        "relay_all_recipients": False,
        "restart_sogo": True
    }


    try:
        response = requests.post(CREATE_DOMAIN_API_URL, headers=headers, json=CREATE_DOMAIN_BODY, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Domain added successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error adding domain:", e)
        return None



def create_mailbox(i,host, api_key):
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    CREATE_MAILBOX_API_URL = f"{host}/api/v1/add/mailbox"
    CREATE_MAILBOX_BODY = {
        "local_part": f"tester{i}",
        "domain": "test.com",
        "name": f"Teszter{i} Janoska",
        "quota": 100,
        "password": "123456",
        "password2": "123456",
        "active": True,
        "force_pw_update": True,
        "tls_enforce_in": False,
        "tls_enforce_out": True
    }

    try:
        response = requests.post(CREATE_MAILBOX_API_URL, headers=headers, json=CREATE_MAILBOX_BODY, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors

        if response.status_code == 200:
            print(f"Mailbox {CREATE_MAILBOX_BODY['local_part']} added successfully.")
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error adding mailbox {CREATE_MAILBOX_BODY['local_part']}:", e)
        return None




def update_mailbox_password(i, host, api_key):
    headers = {"X-API-Key": api_key, "Content-Type": "application/json"}
    UPDATE_MAILBOX_API_URL = f"{host}/api/v1/edit/mailbox"

    UPDATE_MAILBOX_BODY = {
        "items": f"tester{i}@test.com",
        "attr": {
            "password": "9876543210",
            "password2": "9876543210",
            "force_pw_update": "0"
        }
    }

    try:
        response = requests.post(UPDATE_MAILBOX_API_URL, headers=headers, json=UPDATE_MAILBOX_BODY, verify=False)
        response.raise_for_status()  # HTTP hibák kezelése

        if response.status_code == 200:
            print(f"Password for tester{i}@test.com updated successfully.")
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error updating password for tester{i}@test.com:", e)