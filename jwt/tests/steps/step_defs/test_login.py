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

scenarios('features/test_login.feature')

def test_login():
    pass

@pytest.fixture
@when('Execute the login API with valid <user_name> and <password>')
def valid_login_check(user_name,password):
    login_output=get_login_api(login_api,login_hdr,user_name,password)
    return login_output

@then('response should be <code> for valid id and pwd')
def res_valid_login_output(valid_login_check,code):
    assert str(valid_login_check[0])==code
    assert len(valid_login_check[1].get('token'))!=0

@pytest.fixture
@when('Execute the login API with invalid <user_name> and <password>')
def invalid_login_check(user_name,password):
    login_output=get_login_api(login_api,login_hdr,user_name,password)
    return login_output

@then('response should be <code> for invalid id and pwd')
def res_invalid_login_output(invalid_login_check,code):
    assert str(invalid_login_check)==code


@pytest.fixture
@when('Execute the login API with invalid <user_name> and valid <password>')
def mix1_login_check(user_name,password):
    login_output=get_login_api(login_api,login_hdr,user_name,password)
    return login_output

@then('response should be <code> for invalid id and valid pwd')
def res_mix1_login_output(mix1_login_check,code):
    assert str(mix1_login_check)==code

@pytest.fixture
@when('Execute the login API with valid <user_name> and invalid <password>')
def mix2_login_check(user_name,password):
    login_output=get_login_api(login_api,login_hdr,user_name,password)
    return login_output

@then('response should be <code> valid id and invalid pwd')
def res_mix2_login_output(mix2_login_check,code):
    assert str(mix2_login_check)==code