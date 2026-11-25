pipeline {
  agent any
  options { buildDiscarder(logRotator(numToKeepStr: '10')) }
  environment { IMAGEN = 'proyecto-ci/app' }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Construir imagen') {
      steps { sh 'docker build -t $IMAGEN:$BUILD_NUMBER .' }
    }
    stage('Pruebas') {
      steps { sh 'docker run --rm $IMAGEN:$BUILD_NUMBER sh ./scripts/pruebas.sh' }
    }
    stage('Desplegar en desarrollo') {
      when { branch 'develop' }
      steps { sh 'PUERTO=8081 docker compose -p desarrollo up -d --build' }
    }
    stage('Desplegar en pruebas') {
      when { branch 'release/*' }
      steps { sh 'PUERTO=8082 docker compose -p pruebas up -d --build' }
    }
    stage('Desplegar en producción') {
      when { branch 'master' }
      steps {
        input message: '¿Desplegar en producción?'
        sh 'PUERTO=8083 docker compose -p produccion up -d --build'
      }
    }
    stage('Publicar versión') {
      when { buildingTag() }
      steps { sh 'docker tag $IMAGEN:$BUILD_NUMBER $IMAGEN:$TAG_NAME' }
    }
  }
  post {
    success { echo 'Construcción exitosa: informar al equipo.' }
    failure { echo 'Construcción fallida: revisar git log del último commit.' }
  }
}
