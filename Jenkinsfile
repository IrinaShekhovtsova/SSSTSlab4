pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/IrinaShekhovtsova/SSSTSlab4.git', branch: 'main', credentialsId: 'SSSTSGitCred'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'sudo apt-get install python3.10'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m unittest test_math_operations.py'
            }
        }
    }
}
