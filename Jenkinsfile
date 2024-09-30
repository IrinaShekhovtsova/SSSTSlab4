pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/IrinaShekhovtsova/SSSTSlab4.git', branch: 'main',credentialId: 'SSSTSGitCred'
            }
        }
        stage('Build and Test') {
            agent {
                docker {
                    image 'python:3.9-slim'
                }
            }
            steps {
                sh '''
                    if [ -f requirements.txt ]; then
                        pip install --no-cache-dir -r requirements.txt
                    fi
                    python -m unittest discover -v
                '''
            }
        }
    }
}

