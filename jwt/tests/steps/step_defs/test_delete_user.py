import os
import json
import pytest
from pytest_bdd import scenarios,parsers,given,when,then
from jwt_test_api import *
from configparser import ConfigParser


path_file = os.path.dirname(__file__)
print(path_file)
file = path_file+'/config.ini'

config=ConfigParser()
config.read(file)

login_api=config['login']['API']
login_hdr=json.loads(config['login']['headers'])

user_list_api=config['user_list']['API']
user_list_hdr=json.loads(config['user_list']['headers'])

delete_api=config['delete_user']['API']
delete_hdr=json.loads(config['delete_user']['headers'])

scenarios('features/test_delete_user.feature')

def test_delete_user():
    pass

@pytest.fixture
@given('Execute the login API with valid <user_name> and <password> for admin')
def admin_get_token(user_name,password):
    token_output=get_login_api(login_api,login_hdr,user_name,password)
    return token_output[1].get('token')

@pytest.fixture
@when('Pass token to user_list API and get the list of <user>')
def admin_user_list(admin_get_token,user):
    user_list_output=get_api(user_list_api,admin_get_token)
    for i in range(len(user_list_output[1].get('users'))):
        if user_list_output[1].get('users')[i].get('name')==user:
            return user_list_output[1].get('users')[i].get('public_id')
        

@pytest.fixture
@when('Pass the public id and token to delete user API')
def admin_delete_user(admin_user_list,admin_get_token):
    delete_user_output=delete_user_api(delete_api+'/'+admin_user_list,admin_get_token)
    return delete_user_output
    

@then('response should be <code> for admin')
def res_delete_user_output(admin_delete_user,code):
    assert str(admin_delete_user[0])==code