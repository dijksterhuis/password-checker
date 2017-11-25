docker run --rm -d -p 8080:8080 -v jenkins-vol:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins-ci jenkinsci/blueocean
