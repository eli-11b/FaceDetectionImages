import cv2
import streamlit as st
from PIL import Image
import numpy as np

# Load the cascade
face_cascade = cv2.CascadeClassifier('/Users/Eli/Documents/Dev/Python/haarcascade_frontalface_default.xml')

#app title
st.title("Face detection")

#create form
with st.form(key='my_form'):
    allowed_types = ['jpg','png','jpeg']
    st.write("Parameter tuning:")
    scale_factor = st.text_input(label="scale factor",value=1.1)
    min_neighbors = st.text_input(label="min neighbors",value=4)
    file_location = st.file_uploader('Upload Image',type=allowed_types,accept_multiple_files=False)

    # if there is an image selected.
    if file_location is not None:
    # Read the input image
        img = Image.open(file_location)
        img = np.array(img)
    submit_button = st.form_submit_button(label='Submit')   

            
#file upload
if submit_button:
    scale_factor = float(scale_factor)
    min_neighbors = int(min_neighbors)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces and post number of faces in image. 
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=scale_factor,
                                          minNeighbors=min_neighbors,
                                          )
    st.write('**I found {} faces!**'.format(len(faces)))

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the output
    st.write('Are you seeing what i\'m seeing? they will have a box drawn on them.')
    st.image(img,use_column_width=True)



#-----------------------------------SOURCES:-------------------------------------------------
#https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
#https://realpython.com/face-detection-in-python-using-a-webcam/
#https://realpython.com/face-recognition-with-python/
#https://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html    
