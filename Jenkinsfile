pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root'
        }
    }
    parameters {

        string(name: 'APP_URL', defaultValue: 'https://opensource-demo.orangehrmlive.com', description: 'App URL')

    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sudhananda84/SeleniumPOMOrangeHRm.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh "pytest --app-url=${APP_URL} --html=report.html || true"
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Pytest Report'
                ])
            }
        }
    }
}