pipeline {
  agent any
  stages {
    stage('run python script') {
      steps {
        bat 'scripts\\exec_script_local.bat'
      }
    }

    stage('GitHub push') {
      steps {
        bat 'git add .'
        bat 'git commit -m "update files"'
        bat 'git push origin master'
      }
    }

  }
}