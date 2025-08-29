pipeline {
  agent any

  stages {
    // Stage 1: Build the Docker image
    stage('Build') {
      steps {
        script {
          sh "rm -rf my-devops-project || true"
          sh "git clone https://github.com/AytacKahveci/my-devops-project.git"
        }
        dir('my-devops-project') {
          script {
            sh "docker build -t my-app:latest ."
            sh "docker tag my-app:latest kaytac/my-app:latest"
          }
        }
      }
    }

    // Stage 2: Push the Docker image to a registry
    stage('Push') {
        steps {
            script {
              withCredentials([usernamePassword(credentialsId: 'dockerhub-token', passwordVariable: 'DOCKER_TOKEN', usernameVariable: 'DOCKER_USERNAME')]) {
                sh "echo ${DOCKER_TOKEN} | docker login --username ${DOCKER_USERNAME} --password-stdin"
                sh "docker push kaytac/my-app:latest"
              }
            }
        }
    }

    // Stage 3: Deploy to Kubernetes using Ansible
    stage('Deploy to Kubernetes') {
      steps {
        dir('my-devops-project') {
          script {
            sh "ansible-playbook -i localhost, deploy.yml -e 'image_tag=latest'"
          }
        }
      }
    }
  }
}