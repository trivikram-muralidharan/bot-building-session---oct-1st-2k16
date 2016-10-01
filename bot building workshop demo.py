#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is the bot to bot interaction program
import os.path
import sys
import time
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai





IDLI_TOKEN     = 'Your idli client access token'
VADAI_TOKEN    = 'Your vadai client access token'
CHUTNEYS_TOKEN = 'Your chutneys client access token'
CHAPATHI_TOKEN = 'Your chapathi client access token'

def main():
    num=0
    while(1):

        idli     = apiai.ApiAI(IDLI_TOKEN)
        vadai    = apiai.ApiAI(VADAI_TOKEN) 
        chutney  = apiai.ApiAI(CHUTNEYS_TOKEN)
        chapathi = apiai.ApiAI(CHAPATHI_TOKEN)
        
        idli_request = idli.text_request()

        vadai_request = vadai.text_request()

        chutney_request = chutney.text_request()

        chapathi_request = chapathi.text_request()
        

        idli_request.lang = 'en'  # optional, default value equal 'en'
        vadai_request.lang = 'en'
        chutney_request.lang = 'en'
        chapathi_request.lang = 'en'

        
        # request.session_id = "<SESSION ID, UBIQUE FOR EACH USER>"
        if(num==0):
            print("Type \'hi\' to go on a tour of Indian cuisine. P.S. Broth runs deep in our veins")
            start = input()
            print("\nVadai : ",end=" ")
            vadai_request.query = start
            vadai_response = vadai_request.getresponse()
            vadai_responsestr = vadai_response.read().decode('utf-8')
            vadai_response_obj = json.loads(vadai_responsestr)
            endstr = vadai_response_obj["result"]["fulfillment"]["speech"]
            print(endstr)
            time.sleep(4)
            num=1
        else:
            if(num != 2):
                
                print("\n\nIdli : ",end=" ")
                
                idli_request.query = endstr
                idli_response = idli_request.getresponse()
                idli_responsestr = idli_response.read().decode('utf-8')
                idli_response_obj = json.loads(idli_responsestr)
                endstr = idli_response_obj["result"]["fulfillment"]["speech"]
                print(endstr)
                time.sleep(4)


            print("\nVadai : ",end=" ")
            vadai_request.query = endstr
            vadai_response = vadai_request.getresponse()
            vadai_responsestr = vadai_response.read().decode('utf-8')
            vadai_response_obj = json.loads(vadai_responsestr)
            endstr = vadai_response_obj["result"]["fulfillment"]["speech"]
            print(endstr)
            time.sleep(4)

            if(num==2):
                print("\n\nIdli : ",end=" ")
                
                idli_request.query = endstr
                idli_response = idli_request.getresponse()
                idli_responsestr = idli_response.read().decode('utf-8')
                idli_response_obj = json.loads(idli_responsestr)
                endstr = idli_response_obj["result"]["fulfillment"]["speech"]
                print(endstr)
                time.sleep(4)
                break


            

            if(endstr == 'Woah, chill bro. I was just pulling your leg! The chutneys are having a nice laugh listening to us quarrel.'):
                print("\nThe Chutney bros : ",end=" ")
                chutney_request.query = endstr
                chutney_response = chutney_request.getresponse()
                chutney_responsestr = chutney_response.read().decode('utf-8')
                chutney_response_obj = json.loads(chutney_responsestr)
                endstr = chutney_response_obj["result"]["fulfillment"]["speech"]
                print(endstr)
                time.sleep(4)
                num=2


                print("\nChapathi: ",end=" ")
                chapathi_request.query = endstr
                chapathi_response = chapathi_request.getresponse()
                chapathi_responsestr = chapathi_response.read().decode('utf-8')
                chapathi_response_obj = json.loads(chapathi_responsestr)
                endstr = chapathi_response_obj["result"]["fulfillment"]["speech"]
                print(endstr)
                time.sleep(4)
                
                 
            

          # print("\n\nBot\'s response :",end=" ")
         #  response = request.getresponse()
           # print(response)
           # responsestr = response.read().decode('utf-8')
          #  print(responsestr)
          # response_obj = json.loads(responsestr)
#
          #  print(response_obj["result"]["fulfillment"]["speech"])


if __name__ == '__main__':
    main()
