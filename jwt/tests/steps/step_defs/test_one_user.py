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

one_user_api=config['get_one_user']['API']
one_user_hdr=json.loads(config['get_one_user']['headers'])

scenarios('features/test_one_user.feature')

def test_one_user():
    pass

@pytest.fixture
@given('Execute the login API with valid <user_name> and <password> for admin')
def admin_get_token(user_name,password):
    token_output=get_login_api(login_api,login_hdr,user_name,password)
    return token_output[1].get('token')

@pytest.fixture
@when('Pass token to user_list API and get the list of <user>')
def admin_user_list(admin_get_token,user):
    user_list_output=get_api(one_user_api,admin_get_token)
    for i in range(len(user_list_output[1].get('users'))):
        if user_list_output[1].get('users')[i].get('name')==user:
            return user_list_output[1].get('users')[i].get('public_id')
        

@pytest.fixture
@when('Pass the public id and token to one user')
def admin_one_user(admin_user_list,admin_get_token):
    one_user_output=get_api(one_user_api+'/'+admin_user_list,admin_get_token)
    return one_user_output
    

@then('response should be <code> for admin')
def res_one_user_output(admin_one_user,code):
    assert str(admin_one_user[0])==code
    assert len(admin_one_user[1].get('user'))!=0