pipeline {
    agent any
    stages {
        stage('Cleanup Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Check Git Installation') {
            steps {
                sh 'git --version'
            }
        }
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/IrinaShekhovtsova/SSSTSlab4.git', branch: 'main', credentialsId: 'SSSTSGitCred'
            }
        }
        stage('Build and Test') {
            agent {
                docker {
                    image 'python:3.9-slim'
                    reuseNode true
                }
            }
            steps {
                sh '''
                    echo "Current Directory: $(pwd)"
                    echo "Workspace Contents:"
                    ls -la
                    echo "Recursive Directory Listing:"
                    ls -R
                    
                    if [ -f requirements.txt ]; then
                        echo "Installing Dependencies..."
                        pip install --no-cache-dir -r requirements.txt
                    else
                        echo "No requirements.txt found."
                    fi
                    
                    echo "Running Tests..."
                    pytest -v
                '''
            }
        }
    }
}

