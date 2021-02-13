pytest /jwt/tests/steps/step_defs/test_login.py --junitxml=/jwt/tests/reports/login_test_report.xml
pytest /jwt/tests/steps/step_defs/test_create_user.py --junitxml=/jwt/tests/reports/create_user_test_report.xml
pytest /jwt/tests/steps/step_defs/test_one_user.py --junitxml=/jwt/tests/reports/get_one_user_test_report.xml
pytest /jwt/tests/steps/step_defs/test_user_list.py --junitxml=/jwt/tests/reports/user_list_test_report.xml
pytest /jwt/tests/steps/step_defs/test_promote_user.py --junitxml=/jwt/tests/reports/promote_user_test_report.xml
pytest /jwt/tests/steps/step_defs/test_delete_user.py --junitxml=/jwt/tests/reports/delete_user_test_report.xml

# docker-compose run --entrypoint=python development_jwt /jwt/app/api.py
# docker-compose run --entrypoint=bash test_jwt run_tests.sh