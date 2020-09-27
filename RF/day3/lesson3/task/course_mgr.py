import requests

def listCourse():
    params = {'action': 'list_course', 'pagenum': '1', 'pagesize': 20}
    response = requests.get("http://localhost/api/mgr/sq_mgr/", params=params)

    bodyDict = response.json()

    return [one['name'] for one in bodyDict["retlist"]]





if __name__ == '__main__':
    cnamelist = listCourse()
    for one in cnamelist:
        print(one)