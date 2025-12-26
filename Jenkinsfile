pipeline {
    agent any
    
    stages {
        // 新增阶段：在拉取代码前清理工作区
        stage('Clean Workspace Before Build') {
            steps {
                script {
                    echo '正在清理工作区...'
                    deleteDir() // 递归删除当前工作目录[1,2,3](@ref)
                }
            }
        }
        
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                script {
                    bat 'python --version'
                    bat 'python -m pip --version'
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'python -m unittest test_todo_manager.py -v'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Build completed successfully'
            }
        }
    }
    
    // 新增部分：构建后操作
    post {
        always {
            echo 'Pipeline completed'
            // 构建结束后再次清理，确保释放空间[4,6](@ref)
            deleteDir()
            echo '✅ 工作区已清理完毕'[6](@ref)
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}