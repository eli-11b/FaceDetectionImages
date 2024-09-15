FROM python:3.12.4-bookworm

WORKDIR app

COPY face_detection.py .
COPY haarcascade_frontalface_default.xml .
COPY requirements.txt .

RUN apt-get update -y && apt-get upgrade -y \
    && pip3 install -r requirements.txt

EXPOSE 5000    
ENTRYPOINT ["streamlit", "run" "face_detection.py", "-server.port", "5000"]
