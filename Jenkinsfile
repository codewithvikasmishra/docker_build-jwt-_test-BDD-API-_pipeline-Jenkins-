pipeline {
    agent none{
    stages{
        stage('Build'){
            agent{
                docker { image 'development_jwt' }
                }
                steps{
                    sh 'docker-compose up'
                    stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    stage('test'){
            agent{
                docker {image 'test_jwt'}
                }
                steps{
                sh 'docker-compose run --entrypoint=bash test_jwt run_tests.sh'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    }
}