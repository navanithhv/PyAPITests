from urllib import quote

op1, op2, operator = '8', '3', '+'
url = 'http://localhost:8184/messenger/webapi/Calculator/{}/{}/{}'.format(
    quote(op1), quote(op2), quote(operator))