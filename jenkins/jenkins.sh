docker run --rm -d -u root -p 8080:8080 -v jenkins-vol:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins-ci jenkinsci/blueocean ; docker attach jenkins-ci
