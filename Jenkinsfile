pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/IrinaShekhovtsova/SSSTSlab4.git', branch: 'main', credentialsId: 'SSSTSGitCred'
            }
        }

        stage('Setup Python') {
            steps {
                    sh '''
                        pip install -r requirements.txt 
                    '''
            }
        }
	stage('Run Tests') {
	    steps {
		sh 'python -m unittest discover -v'
		}
	}
    }
}
