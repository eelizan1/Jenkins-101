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
                curl --location --request GET 'https://mobile-test-adserver-internal-vip.savagebeast.com:9443/haymaker/management/jsonrpc' \
                --header 'Content-Type: application/json' \
                --data-raw '{
                    "jsonrpc": "2.0",
                    "method": "management-v1.info"
                }'
                '''
            }
        }
    }
}