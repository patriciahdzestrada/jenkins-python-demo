pipeline {
    agent any

    environment {
        DEMO_TOKEN = credentials('demo-token')
        APP_ENV = 'dev'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\mauri\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install --upgrade pip'
                bat '"C:\\Users\\mauri\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\mauri\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pytest.exe"'
            }
        }

        stage('Run Python') {
            steps {
                bat '"C:\\Users\\mauri\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" hello.py'
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'resultado.txt', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente'
        }

        failure {
            echo 'Pipeline falló. Revisar las pruebas.'
        }
    }
}