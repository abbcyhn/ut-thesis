FROM ubuntu:18.04
RUN apt-get update -y && apt-get install -y python3-pip python3-dev libsm6 libxext6 libxrender-dev libglu1
COPY . /app
WORKDIR /app
RUN bash install_dependencies.sh
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 setup.py build_ext --inplace
RUN python3 aeneas_check_setup.py
ENTRYPOINT [ "python3" ]
CMD [ "app2_rest_api.py" ]