pipeline {
    agent {dockerfile true}
    stages{
        stage('Build'){
            agent{
                docker {
                    image 'development_jwt:latest'
                    args '-v /tmp:/tmp'
                    }
                }
                steps{
                    sh 'docker-compose up'
                    stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
    }
}