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
                sh 'apt-get update'
                sh 'apt-get install python3.8'
                sh 'apt-get install python3-pip'
                sh 'python3 -m venv env'
                sh 'source env/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source env/bin/activate'
                sh 'python -m unittest test_math_operations.py'
            }
        }
    }
}
