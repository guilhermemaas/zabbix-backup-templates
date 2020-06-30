pipeline {
  agent any
  stages {
    stage('run python script') {
      steps {
        bat 'cd scripts'
        bat '.\\exec_script_local.bat'
      }
    }

  }
}