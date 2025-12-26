pipeline {
    agent {
        docker {

            image 'my-todo-app:latest'

            reuseNode true
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }


        stage('Run Tests in Docker') {
            steps {

                sh 'python -m unittest discover -v'
            }
        }
        stage('Build') {
            steps {
                echo 'Docker completed！'
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