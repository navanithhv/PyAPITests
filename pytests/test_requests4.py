import requests

def test_post():
	url = 'http://10.137.142.173:8184/messenger/User/Add';
	params = {'Username' : 'Tafcfghdhgfdsdrun' , 'Email' : 'Oinsdhfsdvhscdsvno@gmail.com', 'Phone' : '563653433543525', 'City' : 'Bnaaglaore'};
	r = requests.post(url, params=params);
	print r.status_code;
    
test_post();


