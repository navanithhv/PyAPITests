from urllib import quote
import requests

def funct_status():
	op1, op2, operator = '8', '3', '-';
	url = 'http://10.137.143.6:8184/messenger/webapi/Calculator/{}/{}/{}'.format(quote(op1), quote(op2), quote(operator));
	r = requests.get(url);
	return r.status_code;

def test_functstatus():
	assert funct_status() == 200;
	