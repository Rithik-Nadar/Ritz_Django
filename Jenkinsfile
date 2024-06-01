pipeline{
    agent any
        environment {
            PRISMA_API_URL="https://api.ind.prismacloud.io"
        }
    stages{
        stage("Code Clone"){
            steps{
                echo "cloning the website"
                git url:"https://github.com/Rithik-Nadar/Ritz_Django.git", branch: "main"
                
            }
            
        }
        stage("Code Build"){
            steps{
                echo "building the website"
                sh "docker build -t test:latest ."
            }
            
        }
        stage("Push to Dockerhub"){
        steps{
        echo "pushing the website"
        withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
        sh "docker login -u ${env.dockerHubUser}1@gmail.com -p ${env.dockerHubPass}"
        sh "docker build -t ${env.dockerHubUser}/ritz_django:latest ."
        sh "docker push ${env.dockerHubUser}/ritz_django:latest"
        }
    }
}
    stage("Deploy"){
        steps{
        echo "deploying the container"
            sh "docker-compose down && docker-compose up -d"
        }
      }
                stage('Checkout') {
              steps {
                  git branch: 'main', url: 'git@github.com:Rithik-Nadar/Ritz_Django.git'
                  stash includes: '**/*', name: 'source'
              }
            }
            stage('Checkov') {
                steps {
                    withCredentials([string(credentialsId: 'PC_USER', variable: 'pc_user'),string(credentialsId: 'PC_PASSWORD', variable: 'pc_password')]) {
                        script {
                            docker.image('bridgecrew/checkov:latest').inside("--entrypoint=''") {
                              unstash 'source'
                              try {
                                  sh 'checkov -d . --use-enforcement-rules -o cli -o junitxml --output-file-path console,results.xml --bc-api-key ${pc_user}::${pc_password} --repo-id  git@github.com:Rithik-Nadar/Ritz_Django --branch main'
                                  junit skipPublishingChecks: true, testResults: 'results.xml'
                              } catch (err) {
                                  junit skipPublishingChecks: true, testResults: 'results.xml'
                                  throw err
                              }
                            }
                        }
                    }
                }
            }
        }
        options {
            preserveStashes()
            timestamps()
        }
    }

