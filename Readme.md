# docker_build-jwt-_test-BDD-API-_pipeline-Jenkins-
Using docker I created end to end development - 
I build jwt API using FLASK on docker environment in development_jwt container
Then I created testing container (test_jwt) for testing where I used API Testing like RestAssured in Java and also I used BDD (Given, When, Then) framewwork.
I have used single docker-compose file for creating two different container's.
Lastly I pushed into pipeline(jenkins) for build and test.

If you wnat to use this repo then you will need of admin username as 'Admin' and password as '12345'