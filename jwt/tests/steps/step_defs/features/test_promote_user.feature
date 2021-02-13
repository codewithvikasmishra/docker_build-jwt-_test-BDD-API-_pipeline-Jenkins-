Feature: passing parameters to promote user API

    Scenario Outline: testing with valid x-access-token and user is as admin
        Given Execute the login API with valid <user_name> and <password> for admin
        When Pass token to user_list API and get the list of <user>
        When Pass the public id and token to promote user API
        Then response should be <code> and <message> for admin
        Examples:
        | user_name | password | user | code | message |
        | Admin | 12345 | TestU1 | 200 | The user has been promoted as admin! |