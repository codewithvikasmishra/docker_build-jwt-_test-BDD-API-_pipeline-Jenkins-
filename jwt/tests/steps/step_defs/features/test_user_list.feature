Feature: passing parameters to user list API

    Scenario Outline: testing with valid x-access-token and user is as admin
        Given Execute the login API with valid <user_name> and <password> for admin
        When Test the user_list API with valid x-access-token for admin
        Then response should be <code> for admin
        Examples:
        | user_name | password | code |
        | Admin | 12345 | 200 |

    Scenario Outline: testing with valid x-access-token but user is not as admin
        Given Execute the login API with valid <user_name> and <password> for non-admin
        When Test the user_list API with valid x-access-token for non-admin
        Then response should be <code>  and <message> for non-admin
        Examples:
        | user_name | password | code | message |
        | Aashi | 2017 | 200 | User is not admin so Cannot perform that function! |

    Scenario Outline: testing with invalid x-access-token
        When Test the user_list API with invalid <x_access_token>
        Then response should be <code>
        Examples:
        | x_access_token | code |
        | ezJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiIzN2EwNGM1ZC00Y2U1LTRmN2UtYjBhOC1mNjAzNDU1OWE5ZDYiLCJleHAiOjE2MTMxNjA5Njd9.wP76DoBmB3icWFwxeG7nXL0Na-USo--6ECKWKJcYg00 | 401 |