pipeline {
  agent any
  stages {
    stage('检出') {
      steps {
        checkout([
          $class: 'GitSCM',
          branches: [[name: env.GIT_BUILD_REF]],
          userRemoteConfigs: [[url: env.GIT_REPO_URL, credentialsId: env.CREDENTIALS_ID]]
        ])
      }
    }
    stage('推送部署') {
      steps {
        echo '正在推送文件...'
        sh 'git fetch https://zzzzz167:"${GITHUB_TOKEN}"@github.com/zzzzz167/xiaosbot.git'
        sh 'git push -f https://zzzzz167:"${GITHUB_TOKEN}"@github.com/zzzzz167/xiaosbot.git HEAD:master'
        echo '已完成文件推送.'
      }
    }
  }
}