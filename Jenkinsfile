pipeline {
    agent any

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