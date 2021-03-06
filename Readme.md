# Guide to study Jenkins

## Some docker command to support 
```
docker run -d -p 8080:8080 --name=jenkins-master \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v /home/test/jenkins:/home/test/jenkins \
	-u root \
	jenkins/jenkins
```
```
docker run -d \
	--name=jenkins-master \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v /home/test/jenkins:/home/test/jenkins \
	-v /var/jenkins_home/:/var/jenkins_home/ \
	-u root \
    --privileged \
    --cap-add=NET_ADMIN \
    --net host \
    --pid=host \
	jenkins/jenkins:2.277.1-lts-jdk11

###This one is prefered with priviledge
```
```
docker run -d -p 8080:8080 --name=jenkins-master \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v /home/test/jenkins:/home/test/jenkins \
	jenkins/jenkins
```
### Then you can remove jenkins when you want

`docker rm -f jenkins-master`

### Other comamnds to supports

`docker exec -it jenkins-master bash`

`docker exec -it -u root jenkins-master bash`

### To get the admin password:

`docker exec jenkins-master cat /var/jenkins_home/secrets/initialAdminPassword`

### If the main screen is logged out, lets login by this waym

login: admin

password: $(docker exec jenkins-master cat /var/jenkins_home/secrets/initialAdminPassword)

# Configure in Jenskin

## Start with set up recommended plugins

## Copy all needed files to jenkins
`scp -r /Users/vanthanhle/Desktop/Tools/jenkins test@10.10.21.108:/home/test/`

## Work with Git SSH

Make ssh keys: https://8gwifi.org/sshfunctions.jsp
Go there and generate a key with public key and private key
Then go to your git: https://github.com/settings/profile
Choose SSH and GPG keys, then New SSH Keys, paste the public key there
Now, back to Jenkins, Manage Jenkins, Credentials at:

http://10.10.21.108:8080/credentials/

Choose Jenkins > Global credentials (unrestricted) > adding some credentials?

In the form : 

Kind > SSH Username with private key

ID > "gittest"
Username > "levanthanh3005"
Private Key > Add > Paste private key here:
```
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAhJkMm4YqDibtUHfG240xSEiBV0PwQpLcFEndarkLtEiLEgZ8
D+UTx9wGkxton/XugfPZr93FC73rt7LsjFnG2Ax+Xs774JbW/CyQUcLvwVMA5N3O
P/Nc4R9n6hTqXEUNQ44LMkSJIJ/MOA/I4pv0Omw/OV/9rQXjrNlo9YwkM9Wqyguy
cVYxJXgxXJOvgYdj3J4HfVhsEIuJtn3mVFrZtb/bj8dVxaO9ddaP6hLv5ViqUPpO
BtNo2NMm28stXZ8WXQISYnv96Vl41ZOkogxhumq3NVMRx3BVtUc5hbOv7w81Fekz
BkNta8SDZwmlgBW5mEe+WVghWfysThB0mHNEdQIDAQABAoIBAGmKeKKB04+YJGRc
MggnBgcGzwxqox4aTtpHQNnlmA9Tfn5GcxEjwO7fjswgkNJhqgn90lNNLb3+2VRK
MkY0XzUwHJXSImHNLiliPy0VAEjcjGWetr/oMRFvMgL7yt7Oh5Qxx2+nZY52ItKs
nbThdS/bYSeF5CCIA4RdOFHZzicC0a7HL9d1iC/M3Di4ReAcdY983500FMAYmhBU
0/l7t+mXcZVXdzcdqUX8DcmXsXK7gC/qrQ3HtyOQVwh70dg5jtYCb2hvnYse9mpp
tWB+CxSQCfOSZsR0NMXu1gIj7MzlmiQPHXujobnSx+8O225cPYss0W8yQSN+gHJR
CD++3jECgYEAusoJvV2+33Gf6ltAlIs3CQuAbdUj61a8mWPwTOhOC7WWOvU4LCX4
QNcohgbUEA5Cc9ugHASibD/dzjF1tGwp4qoMKgqzgAtySPDujDlRMulw4LzutvD5
jFJy1s7dssHhv0S7iXSGIIS7y1q3/7Kug3Jtn2bnfopL3XQfINmlIAMCgYEAtbqr
N6ZcXu1HOm8YatYby8U6L72poLj1JgbTEdzjFU+6TrOuVTrTADlIRpiunYRM/KFP
c+fS7tcSTt2iPEj5GmrQCJnnNBobZXo1Uiajc6q9gFB7T5hbxOthbidoH3J2CdyE
wT/qHCIoh/vf5Z1jioWtEO5Mq+Q+1Y+YWX5DzCcCgYBWpxG7orjAqdKZAvpDrw26
CXbr/Pvr2lImCsHYu9AxCG2ILmh/uqGfWvE2tAY+6I6Vduag+NlsxHgehr1nFOKd
f2ujOVGqbiT3h6XysUhlCPzPlXZcsg/itAEIe/FHU0Bp3fXuP3tVrJ3+KbjAS2FA
I56NW0y7XGbzdkJWmAFNhwKBgGBIxdyXTQuShhGkuPgp9tIw7hJLV+tq86AxL3Wg
ZcRt2JVISA6qOw88Sln1HVchuLSFNxZ+9lhLJU0ZypJMS4c+nnhgKoqFZoyOgl/D
TwjCpuKsQZk7bSvZVmbJhDZdK8MvzjqhhYVgZ78cqVT73biP+NEmoQLVzKDUEvEf
oAYzAoGAHDi5IHshXXUr21NQlid1rbPqn76iSq/Pp5+FH64yf+OOqqgA7l2AtNpI
QLLgzKpl2BHL0uCeUqeYnSX+1/GN2avi7TYw2UYaOrjggwR+hNO42mq+xNeUQCbU
cRKe/BUcgqfB2mOuS0aMlPfnrXx0SNX4mD0goJ+HBIXNrgfAW4g=
-----END RSA PRIVATE KEY-----
```

Then click Ok
Now, back to Jenkins home > New Item > Paste the Jenkinsfile into the configuration
## For Docker
Go to /home/test/jenkins, run setupDocker.sh

Then go to manage plugin and install docker plugins

More infor with docker build: 
https://dzone.com/articles/building-docker-images-to-docker-hub-using-jenkins

#For testing locally docker container

`scp -r /Users/vanthanhle/Desktop/Tools/jenkins test@10.10.21.108:/home/test/`

```
docker run -it --rm \
--name pybuild \
-v /home/test/jenkins/pythonTest:/todo \
-w /todo \
-p 5000:80 \
python bash 
```
```
docker run -it --rm \
--name pytest \
-v /home/test/jenkins/pythonTest:/todo \
-w /todo \
--network host \
python bash 
```