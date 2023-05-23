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
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
                sh '''
                curl --location --request GET 'http://localhost:9001/haymaker/abcoachmark/jsonrpc' \
                --header 'Content-Type: application/json' \
                --data-raw '{
                    "jsonrpc": "2.0",
                    "method": "abcoachmark-v1.load",
                    "params": [
                        "type",
                        1
                    ]
                }'
                '''
            }
        }
    }
}