import requests     #import requests library

#APP_ACCESS_TOKEN = '4870715640.a48e759.874aba351e5147eca8a9d36b9688f494'    #access token
APP_ACCESS_TOKEN= '1397099411.1436082.205d096159f742foae5b7d80389ef7cd'
base_url='https://api.instagram.com/v1/'

def self_info():
    req_url= requests.get("%susers/self/?access_token=%s"%(APP_ACCESS_TOKEN,base_url)).json()
    if req_url['meta']['code']==200:            #code 200 is used to when information is access otherwise error occurs.
        print req_url
    else:
        print "wrong information"

question=input("what do you want to do \n1.Get self information\n")
if question==1:
    self_info()










