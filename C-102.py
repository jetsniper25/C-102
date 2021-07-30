import cv2

def takeSnapshot():
    videocapturobject=cv2.VideoCapture(0)
    result=True

    while(result):
        ret,frame=videocapturobject.read()
        print(ret)

        cv2.imwrite("newImage.jpg",frame)
        result=False
    
    videocapturobject.release()
    cv2.destroyAllWindows()

takeSnapshot()

