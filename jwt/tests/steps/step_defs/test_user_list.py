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

scenarios('features/test_user_list.feature')

def test_user_list():
    pass

@pytest.fixture
@given('Execute the login API with valid <user_name> and <password> for admin')
def admin_get_token(user_name,password):
    token_output=get_login_api(login_api,login_hdr,user_name,password)
    return token_output[1].get('token')

@pytest.fixture
@when('Test the user_list API with valid x-access-token for admin')
def admin_user_list(admin_get_token):
    user_list_output=get_api(user_list_api,admin_get_token)
    return user_list_output

@then('response should be <code> for admin')
def res_user_list_output(admin_user_list,code):
    assert str(admin_user_list[0])==code
    assert len(admin_user_list[1])!=0

@pytest.fixture
@given('Execute the login API with valid <user_name> and <password> for non-admin')
def non_admin_get_token(user_name,password):
    token_output=get_login_api(login_api,login_hdr,user_name,password)
    return token_output[1].get('token')

@pytest.fixture
@when('Test the user_list API with valid x-access-token for non-admin')
def non_admin_user_list(non_admin_get_token):
    user_list_output=get_api(user_list_api,non_admin_get_token)
    return user_list_output

@then('response should be <code>  and <message> for non-admin')
def res_user_list_output(non_admin_user_list,code,message):
    assert str(non_admin_user_list[0])==code
    assert non_admin_user_list[1].get('message')==message

@pytest.fixture
@when('Test the user_list API with invalid <x_access_token>')
def invalid_token(x_access_token):
    user_list_output=get_api(user_list_api,x_access_token)
    return user_list_output

@then('response should be <code>')
def res_invalid_token(invalid_token,code):
    assert str(invalid_token)==code