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
              - name: sonar-scanner
                image: sonarsource/sonar-scanner-cli:latest
                command:
                - cat
                tty: true
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
        // stage('Login to GitHub Container Registry') {
        //     steps {
        //         container('docker') {
        //             sh '''
        //             echo "$GHCR_TOKEN" | docker login ghcr.io -u "$GHCR_USERNAME" --password-stdin
        //             '''
        //         }
        //     }
        // }
        // stage('Build and Push Docker Image') {
        //     steps {
        //         container('docker') {
        //             sh '''
        //             docker build . --tag ghcr.io/itsmanibharathi/store:latest
        //             docker push ghcr.io/itsmanibharathi/store:latest
        //             '''
        //         }
        //     }
        // }
        stage('SonarQube Analysis') {
            environment {
                // Inject SonarQube environment variables configured in Jenkins
                SONARQUBE_ENV = 'demo-pip_test' // Name from SonarQube installations
            }
            steps {
                withSonarQubeEnv('demo-pip_test') {
                    container('sonar-scanner') {
                        sh '''
                            sonar-scanner \ 
                            -Dsonar.projectKey=demo-pip_test \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://3.80.11.183:9000 \
                            -Dsonar.login=sqp_d8bdb84e91c7e19f58746e808cc445772ba33dc0
                        '''
                    }
                }
            }
        }
        // stage('Scan Docker Image') {
        //     steps {
        //         container('docker') {
        //             sh '''
        //             # Install Trivy for image scanning
        //             wget -qO- https://github.com/aquasecurity/trivy/releases/latest/download/trivy_$(uname -s | tr '[:upper:]' '[:lower:]')_amd64.tar.gz | tar zxvf - -C /usr/local/bin
        //             # Scan the built Docker image
        //             trivy image ghcr.io/itsmanibharathi/store:latest
        //             '''
        //         }
        //     }
        // }
        stage('Quality Gate Check') {
            steps {
                waitForQualityGate abortPipeline: true
            }
        }
    }
}
