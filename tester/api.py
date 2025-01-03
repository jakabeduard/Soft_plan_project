import requests

headers = {
    "X-API-Key": "E9A377-B0723B-53A5DC-D12E23-67E2F0",
    "Content-Type": "application/json"
}



def get_domanin_all():
    URL_GET_ALL_DOMAIN = "https://edu.mailserver.ro/api/v1/get/domain/all"
    try:
        response = requests.get(URL_GET_ALL_DOMAIN , headers=headers, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")




def get_mailbox_all():
    URL_GET_ALL_MAILBOX = "https://edu.mailserver.ro/api/v1/get/mailbox/all"
    try:
        response = requests.get(URL_GET_ALL_MAILBOX, headers=headers, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")



#create domanin



def create_domain():
    CREATE_DOMAIN_API_URL = "https://edu.mailserver.ro/api/v1/add/domain"
    CREATE_DOMAIN_BODY = {
        "domain": "test.com",
        "description": "test",
        "aliases": 400,
        "mailboxes": 10,
        "defquota": 3072,
        "maxquota": 10240,
        "quota": 10240,
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
    CREATE_MAILBOX_API_URL = "https://edu.mailserver.ro/api/v1/add/mailbox"
    CREATE_MAILBOX_BODY = {
        "local_part": "info",
        "domain": "test.com",
        "name": "Full name",
        "quota": 3072,
        "password": "0123456789",
        "password2": "0123456789",
        "active": True,
        "force_pw_update": True,
        "tls_enforce_in": True,
        "tls_enforce_out": True
    }

    try:
        response = requests.post(CREATE_MAILBOX_API_URL, headers=headers, json=CREATE_MAILBOX_BODY, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors

        if response.status_code == 200:
            print("Mailbox added successfully.")
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print("Error adding mailbox:", e)
        return None


def delete_mailbox(mailbox_id):
    URL_DELETE_MAILBOX = "https://edu.mailserver.ro/api/v1/delete/mailbox"
    try:
        response = requests.delete(URL_DELETE_MAILBOX, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# storage statistics for a mailbox


