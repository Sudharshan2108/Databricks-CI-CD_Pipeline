pipeline {
    agent any

    environment {
        KUBECONFIG_CREDENTIAL_ID = 'aks-kubeconfig'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', // use the correct branch
                    credentialsId: 'github-creds',
                    url: 'https://github.com/Sudharshan2108/Databricks-CI-CD_Pipeline.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Deploy to AKS') {
            steps {
                withCredentials([file(credentialsId: 'aks-kubeconfig', variable: 'KUBECONFIG')]) {
                    sh 'kubectl apply -f k8-jobs.yaml'
                }
            }
        }
    }
}
