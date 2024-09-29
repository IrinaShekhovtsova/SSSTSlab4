pipeline {
    agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/IrinaShekhovtsova/SSSTSlab4.git', branch: 'main', credentialsId: 'SSSTSGitCred'
            }
        }

        stage('Setup Python and Run Tests') {
            steps {
                script {
                    // Run a Python 3.10 container to install dependencies and run tests
                    sh '''
                    docker run --rm -v $PWD:/app -w /app python:3.10 /bin/bash -c "
                        pip install --upgrade pip &&
                        pip install -r requirements.txt &&
                        python -m unittest test_math_operations.py
                    "
                    '''
                }
            }
        }
    }
}
