Feature: passing parameters to login API

    Scenario Outline: testing with valid user_name and password
        When Execute the login API with valid <user_name> and <password>
        Then response should be <code> for valid id and pwd
        Examples:
        | user_name | password | code |
        | Admin | 12345 | 200 |

    Scenario Outline: testing with invalid user_name and password
        When Execute the login API with invalid <user_name> and <password>
        Then response should be <code> for invalid id and pwd
        Examples:
        | user_name | password | code |
        | Sophia | 123sop | 401 |

    Scenario Outline: testing with invalid user_name and valid password
        When Execute the login API with invalid <user_name> and valid <password>
        Then response should be <code> for invalid id and valid pwd
        Examples:
        | user_name | password | code |
        | Sophia | 12345 | 401 |

    Scenario Outline: testing with valid user_name and invalid password
        When Execute the login API with valid <user_name> and invalid <password>
        Then response should be <code> valid id and invalid pwd
        Examples:
        | user_name | password | code |
        | Sophia | 123sop | 401 |