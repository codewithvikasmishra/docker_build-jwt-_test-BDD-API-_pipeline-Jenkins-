import json
import requests
from requests.auth import HTTPBasicAuth

def get_login_api(API,header,user_name,password):
    response = requests.get(API,headers=header,auth=HTTPBasicAuth(user_name,password))
    if response.status_code in (200,202):
        return response.status_code,response.json()
    else:
        return response.status_code

def get_api(API,header):
    response = requests.get(API,headers={'x-access-token':header})
    if response.status_code in (200,202):
        return response.status_code,response.json()
    else:
        return response.status_code

def post_api(API,user_name,password,header):
    response = requests.post(API,json={'name':user_name,'password':password},headers={'x-access-token':header})
    if response.status_code in (200,202):
        return response.status_code,response.json()
    else:
        return response.status_code

def put_api(API,header):
    response = requests.put(API,headers={'x-access-token':header})
    if response.status_code in (200,202):
        return response.status_code,response.json()
    else:
        return response.status_code

def delete_user_api(API,header):
    response = requests.delete(API,headers={'x-access-token':header})
    if response.status_code in (200,202):
        return response.status_code,response.json()
    else:
        return response.status_code