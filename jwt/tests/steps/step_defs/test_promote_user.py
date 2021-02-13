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

promote_api=config['promote_user']['API']
promote_hdr=json.loads(config['promote_user']['headers'])

scenarios('features/test_promote_user.feature')

def test_promote_user():
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
@when('Pass the public id and token to promote user API')
def admin_promote_user(admin_user_list,admin_get_token):
    promote_user_output=put_api(promote_api+'/'+admin_user_list,admin_get_token)
    return promote_user_output
    

@then('response should be <code> and <message> for admin')
def res_promote_user_output(admin_promote_user,code,message):
    assert str(admin_promote_user[0])==code
    assert admin_promote_user[1].get('message')==message