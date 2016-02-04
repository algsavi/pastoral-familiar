#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests

key = 'key-33ce21cfae03c5b1fbfd7c95029e258e'
sandbox = 'pastoralfamiliarsagradafamilia.com'
recipient = 'algsavi@gmail.com'

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), data={
    'from': 'Pastoral Familiar - Sagrada Família <pastoralfamiliarsagradafamilia@hotmail.com>',
    'to': recipient,
    'subject': 'teste de envio',
    'text': 'Bom dia, hoje teremos formação!!!'
})

print 'Status: {0}'.format(request.status_code)
print 'Body:   {0}'.format(request.text)