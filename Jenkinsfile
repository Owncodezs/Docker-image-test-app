pipeline {
    agent {
        kubernetes {
            label 'jenkins-agent'
            yaml """
            apiVersion: v1
            kind: Pod
            spec:
              containers:
              - name: docker
                image: docker:20.10
                command:
                - cat
                tty: true
                volumeMounts:
                - name: docker-sock
                  mountPath: /var/run/docker.sock
              volumes:
              - name: docker-sock
                hostPath:
                  path: /var/run/docker.sock
            """
        }
    }
    environment {
        GHCR_USERNAME = credentials('github-username') // Replace with Jenkins credential ID for GitHub username
        GHCR_TOKEN = credentials('github-token')       // Replace with Jenkins credential ID for GitHub token
    }
    stages {
        stage('Checkout Repository') {
            steps {
                checkout scm
            }
        }
        stage('Login to GitHub Container Registry') {
            steps {
                sh '''
                echo "$GHCR_TOKEN" | docker login ghcr.io -u "$GHCR_USERNAME" --password-stdin
                '''
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                sh '''
                docker build . --tag ghcr.io/itsmanibharathi/store:latest
                docker push ghcr.io/itsmanibharathi/store:latest
                '''
            }
        }
    }
}
