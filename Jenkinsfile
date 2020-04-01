pipeline{
    agent any
    stages {
        
        stage('Build') {
            steps {
                    echo "Builds the checked out project!";
            }
        }
        
        stage('Quality-Gate') {
            steps {
                    echo "Verifying Quality Gates";
            }
        }
        
        stage('Deploy') {
            steps {
                echo "Deploying to stage enviornment for more tests";
            }
        }
    }
        
    post {
        always {
            echo 'This is always block'
        }
        success {
            echo 'This is success block'
        }
        failure {
            echo 'This is failure block'
        }
        unstable {
            echo 'This is unstable block'
        }
        changed {
            echo 'This will run only if pipleine status is changed'
            echo 'For example if the pipeline was previosly failing but now is successfull'
        }
        
    }
}
