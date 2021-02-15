pipeline {
    agent any
    stages{
        stage('Build'){
            agent{
                docker {
                    image 'development_jwt:latest'
                    }
                }
                steps{
                    sh 'docker-compose up'
                    stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    }
}