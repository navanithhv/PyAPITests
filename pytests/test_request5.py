import requests

def test_all():
	r = requests.get('http://10.137.142.173:8184/messenger/User/All');
	print r.status_code;
	print r.text;
	
test_all();
