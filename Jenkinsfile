pipeline {
  agent any
  stages {
    stage('run python script') {
      steps {
        bat 'cd script'
        bat '.\\exec_script_local.bat'
      }
    }

  }
}