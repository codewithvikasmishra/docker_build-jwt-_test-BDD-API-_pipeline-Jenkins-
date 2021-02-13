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

create_api=config['create_user']['API']
create_hdr=json.loads(config['create_user']['headers'])

scenarios('features/test_create_user.feature')

def test_create_user():
    pass

@pytest.fixture
@given('Execute the login API with valid <user_name> and <password> for admin')
def admin_get_token(user_name,password):
    token_output=get_login_api(login_api,login_hdr,user_name,password)
    return token_output[1].get('token')

@pytest.fixture
@when('Pass new <name> and <pwd> in request body for admin')
def admin_create_user(name,pwd,admin_get_token):
    user_list_output=post_api(create_api,name,pwd,admin_get_token)
    return user_list_output
        

@then('response should be <code> and <message> for admin')
def res_admin_create_user_output(admin_create_user,code,message):
    assert str(admin_create_user[0])==code
    assert admin_create_user[1].get('message')==message

@pytest.fixture
@given('Execute the login API with valid <user_name> and <password> for non-admin')
def non_admin_get_token(user_name,password):
    token_output=get_login_api(login_api,login_hdr,user_name,password)
    return token_output[1].get('token')

@pytest.fixture
@when('Pass new <name> and <pwd> in request body for non-admin')
def non_admin_create_user(name,pwd,non_admin_get_token):
    user_list_output=post_api(create_api,name,pwd,non_admin_get_token)
    return user_list_output
        

@then('response should be <code>  and <message> for non-admin')
def res_non_admin_create_user_output(non_admin_create_user,code,message):
    assert str(non_admin_create_user[0])==code
    assert non_admin_create_user[1].get('message')==message

@pytest.fixture
@when('Test the create user API with invalid <x_access_token> for new <user> and <pwd>')
def invalid_token_create_user(user,pwd,x_access_token):
    user_list_output=post_api(create_api,user,pwd,x_access_token)
    return user_list_output
        
@then('response should be <code>')
def res_invalid_token_create_user_output(invalid_token_create_user,code):
    assert str(invalid_token_create_user)==code