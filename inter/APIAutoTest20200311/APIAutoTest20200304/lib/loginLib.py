from config import HOST
def login(username,password):
    import requests
    dict1 = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        "username": username,
        "password": f"{password}"
    }
    try:
        r = requests.post(f'{HOST}/api/mgr/loginReq', data=payload,verify=False, headers=dict1)
        return r.cookies['sessionid']
    except:
        return '11111111'

