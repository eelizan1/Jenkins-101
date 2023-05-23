pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                python3 hello.py
                python3 hello.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Testing API...'
                sh '''
                curl --location --request GET 'https://jsonplaceholder.typicode.com/posts/1'
                '''
            }
        }
    }
}