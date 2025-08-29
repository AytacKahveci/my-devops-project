pipeline {
  agent any

  stages {
    // Stage 1: Build the Docker image
    stage('Build') {
      steps {
        dir('my-devops-project') {
          script {
            sh "docker build -t my-app:${env.BUILD_NUMBER} ."
          }
        }
      }
    }

    // Stage 2: Deploy to Kubernetes using Ansible
    stage('Deploy to Kubernetes') {
      steps {
        script {
          sh "ansible-playbook -i localhost, deploy.yml"
        }
      }
    }
  }
}