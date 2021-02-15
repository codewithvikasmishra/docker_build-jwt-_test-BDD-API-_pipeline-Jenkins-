pipeline {
    agent any
    stages{
        stage('Build Docker Image'){
            sh 'docker build -t vikasbca08/development_jwt .'
        }
        stage('Push Docker Image'){
            withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerhubpwd')]) {
                sh "docker login -u vikasbca08 -p ${dockerhubpwd}"
                }
            
            sh 'docker push vikasbca08/development_jwt'
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