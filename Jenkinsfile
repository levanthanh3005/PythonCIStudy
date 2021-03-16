pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh "docker stop pybuild || true && docker rm pybuild || true"
                sh """
					docker run -d \
						--name pybuild \
						-v $(pwd)/PythonCIStudy/pythonTest:/todo \
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
						-v $(pwd)/PythonCIStudy/pythonTest:/todo \
						-w /todo \
						--network host \
						python bash -c 'pip install requests pytest && pytest -s test.py'
                """
            }
        }
        stage('finish') {
        	steps {
                sh "docker stop pybuild || true && docker rm pybuild || true"
        		echo ""
        	}
        }
    }
}