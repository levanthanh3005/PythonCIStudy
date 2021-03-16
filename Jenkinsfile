pipeline {
    agent any

    environment {
        imagename = "dockerJenkins"
        registryCredential = ''
        dockerImage = ''
    }

    stages {
        stage('clone') {
            steps {
                git branch: 'main',credentialsId: 'gittest',url: 'git@github.com:levanthanh3005/PythonCIStudy.git'
                sh "pwd"
                sh "ls -lat"
            }
        }
        stage('build') {
            steps {
                sh "docker stop pybuild || true && docker rm pybuild || true"
                sh """
                    docker run -d \
                        --name pybuild \
                        -v /var/jenkins_home/workspace/dockerTest/pythonTest:/todo \
                        -w /todo \
                        -p 5000:80 \
                        python bash -c 'pip install flask && python hello.py'
                """
            }
        }
        stage('tryrun') {
            steps {
                sleep 10
                sh "curl localhost:5000"
            }
        }
        stage('test') {
            steps {
                sh """
                    docker run -t --rm \
                        --name pytest \
                        -v /var/jenkins_home/workspace/dockerTest/pythonTest:/todo \
                        -w /todo \
                        --network host \
                        python bash -c 'pip install requests pytest && pytest -s test.py'
                """
            }
        }
        stage('finish') {
            steps {
                sh "docker stop pybuild || true && docker rm pybuild || true"
                echo "Done"
            }
        }
        stage('build image') {
            steps {
                dockerImage = docker.build(imagename,"-f pythonTest/Dockerfile .")
            }
        }
    }
}