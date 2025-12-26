pipeline {
    agent any // 暂时改回 any，先绕过 Docker 问题

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t my-todo-app:latest .'
                }
            }
        }
        
        stage('Run Tests in Container') {
            steps {
                script {
                    // 使用明确的 docker run 命令，而不是 agent { docker }
                    bat 'docker run --rm -v "%CD%":/workspace -w /workspace my-todo-app:latest python -m unittest discover -v'
                }
            }
        }
        
        stage('Build') {
            steps {
                echo 'Build completed successfully'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}