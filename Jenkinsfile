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
        }
    }
}