from flask import Flask,render_template,request
import pandas as pd
import numpy as np
from flask import Response
from camera import VideoCamera
import cv2
from flask_cors import CORS 
import os
import time
import handTrackingModule as htm


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})



def getNumber(ar):
    s=""
    for i in ar:
       s+=str(ar[i]);
       
    if(s=="00000"):
        return (0)
    elif(s=="01000"):
        return(1)
    elif(s=="01100"):
        return(2) 
    elif(s=="01110"):
        return(3)
    elif(s=="01111"):
        return(4)
    elif(s=="11111"):
        return(5) 
    elif(s=="01001"):
        return(6)
    elif(s=="01011"):
        return(7)      
 




# app.config["SECRET_KEY"]="secret_key"
def gen(camera):
    while 1:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n'+frame+
            b'\r\n\r\n')

@app.route('/')
def index():
    # return render_template('index.html')
    return Response(gen(VideoCamera()),
        mimetype='multipart/x-mixed-replace;boundary=frame')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
        mimetype='multipart/x-mixed-replace;boundary=frame')


if __name__=='__main__':
    app.run(debug=True,port=3000)
