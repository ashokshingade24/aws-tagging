pipeline {
   agent any
   environment {
      REGION =''
   }

   stages {
      stage('user input') {
         steps {
            script {
               timeout ( time: 10, unit: "MINUTES" )  {
                  REGION=input message: 'Select Region',  parameters: [choice(choices: 'eu-west-3\nus-west-2', description: '', name: 'Region:')]
                  if (REGION == "eu-west-3" ) {
                    sh "python3 --version"
                  }
                }
            }
         }
      }
   }
}

