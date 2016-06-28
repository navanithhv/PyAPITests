import requests

def test_login_get():
    r = requests.get('https://loadosophia.org/login/?provider=google');
    print r.status_code;
    #print r.text;
    print r.headers;

test_login_get()
