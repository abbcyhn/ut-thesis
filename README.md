# AI-powered cloud usage controlling system in smart home environment

## Applications

### 1) Application 1 - Deep learning based object classification using YOLOv3
- [x] [Client Side](/app1/app1_client/)
- [x] [Server Side](/app1/app1_server/)
- [x] [System Architecture](/app1/app1.png)
- Testing scripts
	- curl -X POST -F image=@traffic.jpg 'http://localhost:80/api/detect' --output traffic_yolo.png

### 2) Application 2 - Text-audio synchronisation or forced alignment (Aeneas)
- [ ] [Client Side](/app2/app2_client/)
- [ ] [Server Side](/app2/app2_server/)
- [x] [System Architecture](/app2/app2.png)
- Testing scripts
	- python3 -m aeneas.diagnostics
	- python3 setup.py build_ext --inplace
	- python3 aeneas_check_setup.py
	- curl -X POST -F audio=@p001.mp3 -F subtitle=@p001.xhtml 'http://localhost:81/api/sync' --output p001.json

### 3) Application 3 - Speech-to-text conversion (PocketSphinx)
- [ ] [Client Side](/app3/app3_client/)
- [ ] [Server Side](/app3/app3_server/)
- [ ] [System Architecture](/app3/app3.png)



## Docker commands

### 1) Docker config

- sudo groupadd docker
- sudo usermod -aG docker $USER
- newgrp docker
- sudo chmod 666 /var/run/docker.sock
- sudo systemctl restart docker

### 2) Docker build

- docker build -t $CONTAINER_NAME:latest . 
- docker build -t $IMAGE_NAME -f $DOCKER_FILE_NAME .
	
### 3) Docker run, exec, logs

- docker run -d -p 81:5000 $CONTAINER_NAME:latest
- docker exec -it $CONTAINER_NAME sh
- docker logs -f --tail 10 $CONTAINER_NAME
