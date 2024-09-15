# FaceDetectionImages
Web app in streamlit that detects faces in images. 
<img src="images/Intro.png">
<img src="images/results.png">

## Instructions

1. Download
2. Navigate to the location of the .py file
3. Type:
```
streamlit run face_detection.py
```


Open a web browser to http://localhost:8501

<hr>

### Docker
```
#build docker image
docker build -t face_detector:v1 .
```

```
#run docker image
docker run -it -p 5000:5000 --gpus all face_detector:v1
```
Download, make changes, enjoy!

# Questions?
<br>
<img src="https://github.com/user-attachments/assets/710669b1-49b7-4936-834c-c523781db754"  height="150">
