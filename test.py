import request
def external_ip():
  print(request.get('https://checkip.amazonaws.com').text
