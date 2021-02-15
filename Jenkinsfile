pipeline {
    agent any
    stages{
        stage('Build Docker Image'){
            steps{
            sh 'sudo docker build -t vikasbca08/development_jwt .'
        }
        }
        stage('Push Docker Image'){
            steps{
            withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerhubpwd')]) {
                sh "sudo docker login -u vikasbca08 -p ${dockerhubpwd}"
                }
            
            sh 'sudo docker push vikasbca08/development_jwt'
        }
        }
        stage('Build'){
            agent{
                docker {
                    image 'development_jwt:latest'
                    }
                }
                steps{
                    sh 'sudo docker-compose up'
                    stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    }
}