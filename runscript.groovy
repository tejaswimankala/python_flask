pipeline {
    agent any
     
    }
    
    parameters{
        string(name:'imageName_fromBuild', defaultValue: '', description:'Build source')
    }

    stages {
        stage('Initialize'){
            steps{
                script{
                    def dockerHome = tool 'docker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                    echo "Running ${env.BUILD_ID} job on ${env.JENKINS_URL}"
                }
            }
        }
        stage('Pull image from Hub'){
            steps{
                echo "${params.imageName_fromBuild}"
                sh("docker pull ${params.imageName_fromBuild}")
            }
        }
        stage('Test run app'){
            steps{
                runApp()
            }
        }
    } 
}

def runApp(){
    sh("docker run -d -p 8083:5000 ${params.imageName_fromBuild}")
}
