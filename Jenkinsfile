pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/i211568-noman/flask_App.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build Application') {
            steps {
                bat 'python -m py_compile app.py'
            }
        }

        stage('Deploy Application') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
