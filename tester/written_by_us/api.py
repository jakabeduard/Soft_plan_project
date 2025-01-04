import json

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



# headers = {
#     "X-API-Key": "E9A377-B0723B-53A5DC-D12E23-67E2F0",
#     "Content-Type": "application/json"
# }
host = ""
headers = {}

def set_host_and_headers(api_key, host_url):
    """Beállítja a host és a headers globális változókat."""
    global headers, host
    host = host_url
    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json"
    }

def get_domanin_all():
    # URL_GET_ALL_DOMAIN = "https://edu.mailserver.ro/api/v1/get/domain/all"
    URL_GET_ALL_DOMAIN = f"{host}/api/v1/get/domain/all"
    try:
        response = requests.get(URL_GET_ALL_DOMAIN , headers=headers, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_mailbox_all():
    # URL_GET_ALL_MAILBOX = "https://edu.mailserver.ro/api/v1/get/mailbox/all"
    URL_GET_ALL_MAILBOX = f"{host}/api/v1/get/mailbox/all"
    try:
        response = requests.get(URL_GET_ALL_MAILBOX, headers=headers, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def delete_mailboxes(email_list):
    # Az API végpont
    URL_DELETE_EMAIL_ADDRESSES = f"{host}/api/v1/delete/mailbox"
    # URL_DELETE_EMAIL_ADDRESSES = "https://edu.mailserver.ro/api/v1/delete/mailbox"

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




def delete_domains(domains):
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


def create_domain():
    CREATE_DOMAIN_API_URL = "https://edu.mailserver.ro/api/v1/add/domain"
    # CREATE_DOMAIN_API_URL = f"{host}/api/v1/add/domain"

    CREATE_DOMAIN_BODY = {
        "domain": "test.com",
        "description": "test",
        "aliases": 400,
        "mailboxes": 100,
        "defquota": 102040,
        "maxquota": 102040,
        "quota": 102040,
        "active": True,
        "rl_value": 10000,
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






def create_domain():
   # CREATE_DOMAIN_API_URL = "https://edu.mailserver.ro/api/v1/add/domain"
    CREATE_DOMAIN_API_URL = f"{host}/api/v1/add/domain"

    CREATE_DOMAIN_BODY = {
        "domain": "test.com",
        "description": "test",
        "aliases": 400,
        "mailboxes": 100,
        "defquota": 102040,
        "maxquota": 102040,
        "quota": 102040,
        "active": True,
        "rl_value": 10000,
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




def create_mailbox():
    #CREATE_MAILBOX_API_URL = "https://edu.mailserver.ro/api/v1/add/mailbox"
    CREATE_MAILBOX_API_URL = f"{host}/api/v1/add/mailbox"
    CREATE_MAILBOX_BODY = {
        "local_part": "tester",
        "domain": "test.com",
        "name": f"Teszter",
        "quota": 3072,
        "password": "0123456789",
        "password2": "0123456789",
        "active": True,
        "force_pw_update": True,
        "tls_enforce_in": True,
        "tls_enforce_out": True,
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
        print("Error adding mailbox:", e)
        return None




