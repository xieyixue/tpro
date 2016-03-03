# coding=utf-8
import requests
import json


def start_check():
    with open("url.json", "r") as f:
        data = json.load(f)

    urls = [i["url"] for i in data["data"]]
    result = map(check_url, urls)
    return result


def check_url(url):
    r = requests.get(url)
    return {"url":url, "code": r.status_code}


def get_urls():
    r = requests.get("http://127.0.0.1:8000/api/geturls/")
    with open("url.json","w") as f:
        data = r.json()
        json.dump(data,f)


def post_data(data):
    import socket
    hostname = socket.gethostname()
    data = json.dumps(data)
    r = requests.post("http://127.0.0.1:8000/api/geturls/",{"data": data,"hostname": hostname})
    print r.status_code, r.text


start_check()
# check_url("http://www.baidu.com")

if __name__ == "__main__":
    # get_urls()
    data = [{'url': u'http://baidu.com', 'code': 200}, {'url': u'http://qssec.com', 'code': 200}]
    print data
    post_data(data)