pipeline {
  agent any
  stages {
    stage('Print Message') {
      steps {
        echo 'Teste Blue Ocean'
      }
    }

    stage('') {
      steps {
        bat(script: 'python\\scripts\\exportar_templates.py', label: 'python')
      }
    }

  }
}