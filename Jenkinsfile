pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest'
            }
        }

        stage('Run Python') {
            steps {
                bat 'python hello.py'
            }
        }
    }
}