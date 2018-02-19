import requests     #import requests library
import urllib
APP_ACCESS_TOKEN = '4870715640.a48e759.874aba351e5147eca8a9d36b9688f494'    #access token
#APP_ACCESS_TOKEN= '4097850240.5b7c7d2.f1eb05309a9a44bf9ee156404b87c1f7'
base_url='https://api.instagram.com/v1/'

def self_info():
    req_url= requests.get("%susers/self/?access_token=%s"%(base_url,APP_ACCESS_TOKEN)).json()
    if 'data' in req_url:
        print 'Username: %s' % (req_url['data']['username'])
        print 'No. of followers: %s' % (req_url['data']['counts']['followed_by'])
        print 'No. of people you are following: %s' % (req_url['data']['counts']['follows'])
        print 'No. of posts: %s' % (req_url['data']['counts']['media'])
    else:
        print "wrong information"

def recent_post():
    req_url = requests.get("%susers/self/media/recent/?access_token=%s" % (base_url, APP_ACCESS_TOKEN)).json()
    if req_url['meta']['code'] == 200:  # code 200 is used to when information is access otherwise error occurs.
        if len(req_url['data'])>0:
            print req_url['data'][0]['id']
            print req_url['data'][0]['images']['standard_resolution']['url']
            name= req_url['data'][0]['id'] + ".jpg"
            url= req_url['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(url,name)
            print "image downloaded"
        else:
            print "no user post"
    else:
        print "wrong information"


def get_user_id(username):
    req_url = requests.get("%susers/search?q=%s&access_token=%s" % (base_url,username, APP_ACCESS_TOKEN)).json()
    if req_url['meta']['code'] == 200:
        if len(req_url['data']):
            return req_url['data'][0]['id']
        else:
            return None
    else:
        print "error"


def user_info(username):
        user_id = get_user_id(username)
        if user_id == None:
            print "user name is incorrect"
            exit()
        else:
            req_url= requests.get("%susers/%s/?access_token=%s"%(base_url,user_id,APP_ACCESS_TOKEN)).json()
            if 'data' in req_url:
                print 'Username: %s' % (req_url['data']['username'])
                print 'No. of followers: %s' % (req_url['data']['counts']['followed_by'])
                print 'No. of people you are following: %s' % (req_url['data']['counts']['follows'])
                print 'No. of posts: %s' % (req_url['data']['counts']['media'])
            else:
                    print "wrong information"




def user_recent_post(name):
    user_id=get_user_id(name);
    req_url = requests.get("%susers/%s/media/recent/?access_token=%s" % (base_url,user_id, APP_ACCESS_TOKEN)).json()
    if req_url['meta']['code'] == 200:  # code 200 is used to when information is access otherwise error occurs.
        if len(req_url['data'])>0:
            print req_url['data'][0]['id']
            print req_url['data'][0]['videos']['standard_resolution']['url']
            name = req_url['data'][0]['id'] + ".mp4"
            url = req_url['data'][0]['videos']['standard_resolution']['url']
            urllib.urlretrieve(url, name)
            print "video downloaded"
        else:
            print "no user post"
    else:
        print "wrong information"

while True:
    question=input("what do you want to do\n1.Get self information\n2.get recent post\n3.get user info\n4.get user recent post\n0.exit \n")
    if question==1:
        self_info()
    elif question==2:
        recent_post()
    elif question ==3:
        user_name=raw_input("what is the user name of the user")
        user_info(user_name)
    elif question==4:
        user_name = raw_input("what is the user name of the user")
        user_recent_post(user_name)
    elif question==0:
        exit()











