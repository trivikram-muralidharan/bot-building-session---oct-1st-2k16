#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is the code for the waiter bot
import os.path
import sys

import json

try:
    import apiai
except ImportError:
    sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
)
import apiai





CLIENT_ACCESS_TOKEN = 'Your waiter bot client access token'



while(1):

    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    # request.session_id = "<SESSION ID, UBIQUE FOR EACH USER>"
    print("\n\nYou: ",end=" ")
    request.query = input()

    print("\n\nWitty Waiter :",end=" ")
    response = request.getresponse()
    print(response)
    responsestr = response.read().decode('utf-8')
    print(responsestr)
    response_obj = json.loads(responsestr)

    print(response_obj["result"]["fulfillment"]["speech"])

