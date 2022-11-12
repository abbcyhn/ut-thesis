# AI-powered cloud usage controlling system in smart home environment

## Applications

### 1) Application 1
- [x] [Distribution](/app1/app1_distribution/)
- [x] [Rest Api](/app1/app1_rest_api/)
- [x] [System Architecture](/app1/app1.png)
- Testing scripts
	- curl -X POST -F image=@traffic.jpg 'http://localhost:80/api/detect' --output traffic_yolo.png

### 2) Application 2
- [ ] [Distribution](/app2/app2_distribution/)
- [ ] [Rest Api](/app2/app2_rest_api/)
- [x] [System Architecture](/app2/app2.png)
- Testing scripts
	- python3 -m aeneas.diagnostics
	- python3 setup.py build_ext --inplace
	- python3 aeneas_check_setup.py
	- curl -X POST -F audio=@p001.mp3 -F subtitle=@p001.xhtml 'http://localhost:81/api/sync' --output p001.json

### 3) Application 3
- [ ] [Distribution](/app3/app3_distribution/)
- [ ] [Rest Api](/app3/app3_rest_api/)
- [ ] [System Architecture](/app3/app3.png)



## General commands

### 1) Docker build

- docker build -t $CONTAINER_NAME:latest . 
- docker build -t $IMAGE_NAME -f ./docker/$DOCKER_FILE_NAME .
	
### 2) Docker run, exec, logs

- docker run -d -p 81:5000 $CONTAINER_NAME:latest
- docker exec -it $CONTAINER_NAME sh
- docker logs -f --tail 10 $CONTAINER_NAME
