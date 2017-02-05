import cv2 as cv

frame_name = 'frame'
cv.startWindowThread()
cv.namedWindow(frame_name)
faceCascade = cv.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

camera = cv.VideoCapture(0)


while True:
    ret, frame = camera.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow(frame_name, frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv.destroyAllWindows()
