# AI-powered cloud usage controlling system in smart home environment

## Applications

### 1) Application 1
- [x] [Distribution](/app1/app1_distribution/)
- [x] [Rest Api](/app1/app1_rest_api/)
- [x] [System Architecture](/app1/app1.png)

### 2) Application 2
- [ ] [Distribution](/app2/app2_distribution/)
- [ ] [Rest Api](/app2/app2_rest_api/)
- [x] [System Architecture](/app2/app2.png)

### 3) Application 3
- [ ] [Distribution](/app3/app3_distribution/)
- [ ] [Rest Api](/app3/app3_rest_api/)
- [ ] [System Architecture](/app3/app3.png)



## General commands
	docker build -t app2-fog:latest . 
	
	docker run -d -p 81:5000 app2-fog:latest

	docker exec -it container_name sh

	docker logs -f --tail 10 container_name

	python3 -m aeneas.diagnostics

	python3 setup.py build_ext --inplace

	python3 aeneas_check_setup.py

	curl -X POST -F image=@traffic.jpg 'http://localhost:80/api/detect' --output traffic_yolo.png
