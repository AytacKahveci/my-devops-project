pipeline {
  agent any

  stages {
    // Stage 1: Build the Docker image
    stage('Build') {
      steps {
        script {
          sh "docker build -t my-app:${env.BUILD_NUMBER} ."
        }
      }
    }

    // Stage 2: Deploy to Kubernetes using Ansible
    steps {
      script {
        sh "ansible-playbook -i localhost, deploy.yml"
      }
    }
  }
}