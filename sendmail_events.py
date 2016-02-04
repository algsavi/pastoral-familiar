import requests

key = 'key-33ce21cfae03c5b1fbfd7c95029e258e'
sandbox = 'sandboxc1225f3611bf44c5a80ce616d1d21611.mailgun.org'

request_url = 'https://api.mailgun.net/v2/{0}/events'.format(sandbox)
request = requests.get(request_url, auth=('api', key), params={'limit': 5})

print 'Status: {0}'.format(request.status_code)
print 'Body:   {0}'.format(request.text)