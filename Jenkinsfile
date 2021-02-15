pipeline {
    agent any
    stages{
        stage('Build Docker Image'){
            sh 'docker build -t vikasbca08/jwt_jenkins:1.0.0 .'
        }
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