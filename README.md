Thesis

DOCKER CMDS:
	docker build -t app1-fog:latest .
	
	docker run -d -p 80:5000 app1-fog:latest

CURL CMNDS:
	curl -X POST -F image=@traffic.jpg 'http://localhost:80/api/detect' --output traffic_yolo.png

Video Source: 
    https://drive.google.com/file/d/1gCIWNk4M59dtERQUPnKbBQcotHAE1HJH/view?usp=sharing




docker build -t app2-fog:latest . 


docker run -d -p 81:5000 app2-fog:latest

docker exec -it container_name sh

docker logs -f --tail 10 container_name

python3 -m aeneas.diagnostics

python3 setup.py build_ext --inplace

python3 aeneas_check_setup.py

