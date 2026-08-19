pipeline {
    agent any

    stages {
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
