pipeline{
    agent any
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
    }
}
