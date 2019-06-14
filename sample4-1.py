import cv2
n="1"

cascade_path = 'C:/Users/1623047/Anaconda3/Library/etc/haarcascades/cascade.xml'
cascade = cv2.CascadeClassifier(cascade_path)
if cascade.empty():
    print("特徴ファイルが読み込めません")
    import sys
    sys.exit()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("カメラを起動できない")
    import sys
    sys.exit()

cv2.namedWindow("image")

while True:
    _, frame = cap.read()

    if frame is None:
        break
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4) 

    cv2.imshow('image',frame)

    key = cv2.waitKey(17)
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite("sample4-"+n+".bmp",frame)
        n=n+"1"

cv2.destroyAllWindows()
cap.release
