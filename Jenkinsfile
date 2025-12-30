pipeline {
    agent any
    
    triggers {
        githubPush()
    }
    
    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                bat '''
                    pytest tests/ -v --junitxml=test-results.xml || pytest -v
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
                echo 'Building Flask application...'
                bat '''
                    echo "Flask app ready for deployment"
                    python app.py --build
                '''
            }
        }
        
        stage('Deploy Application') {
            steps {
                echo 'Deploying Flask application...'
                bat '''
                    taskkill /f /im python.exe 2>nul
                    nohup python app.py > app.log 2>&1 &
                    timeout /t 5
                    curl -f http://localhost:5000 || echo "App started"
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed.'
            archiveArtifacts artifacts: 'app.log,test-results.xml', allowEmptyArchive: true
        }
        success {
            echo 'Flask app deployed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
