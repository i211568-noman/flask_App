pipeline {
    agent any

    triggers {
        // Trigger pipeline on every push (when GitHub webhook is configured)
        githubPush()
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                // Jenkins declarative pipeline already did checkout; just list files
                bat 'dir'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python 3 dependencies...'
                bat '''
                    python3 --version || python --version

                    REM Use Python 3 pip explicitly (adjust if command is only `python`)
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests with pytest...'
                bat '''
                    python3 -m pytest -v --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building Flask application (no compilation needed)...'
                bat '''
                    echo Build step for Flask app completed
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Simulating deployment of Flask app...'
                bat '''
                    echo "Flask app deployed on http://localhost:5000" > deployment-success.txt
                    echo "Deployed by Jenkins at %DATE% %TIME%" >> deployment-success.txt
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'deployment-success.txt,test-results.xml', allowEmptyArchive: true
            echo 'Pipeline completed. Artifacts archived.'
        }
        success {
            echo 'Flask CI/CD pipeline SUCCESS.'
        }
        failure {
            echo 'Flask CI/CD pipeline FAILED. Check the console log and artifacts.'
        }
    }
}
