Feature: passing parameters to create user API

    Scenario Outline: testing with valid x-access-token and user is as admin
        Given Execute the login API with valid <user_name> and <password> for admin
        When Pass new <name> and <pwd> in request body for admin
        Then response should be <code> and <message> for admin
        Examples:
        | user_name | password | name | pwd | code | message |
        | Admin | 12345 | TestU1 | Test123 | 200 | New user created! |

    Scenario Outline: testing with valid x-access-token but user is not as admin
        Given Execute the login API with valid <user_name> and <password> for non-admin
        When Pass new <name> and <pwd> in request body for non-admin
        Then response should be <code>  and <message> for non-admin
        Examples:
        | user_name | password | name | pwd | code | message |
        | Aashi | 2017 | TestUser2 | Test2 | 200 | Token user is not admin so cannot perform that function! |

    Scenario Outline: testing with invalid x-access-token
        When Test the create user API with invalid <x_access_token> for new <user> and <pwd>
        Then response should be <code>
        Examples:
        | x_access_token | user | pwd | code |
        | ezJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiIzN2EwNGM1ZC00Y2U1LTRmN2UtYjBhOC1mNjAzNDU1OWE5ZDYiLCJleHAiOjE2MTMxNjA5Njd9.wP76DoBmB3icWFwxeG7nXL0Na-USo--6ECKWKJcYg00 | TestUser3 | Test3 | 401 |