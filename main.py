import cv2
import time

face_detector = cv2.CascadeClassifier(
    "models/haarcascade_frontalface_default.xml"
)

camera = cv2.VideoCapture(0)
previous_time = 0


while True:

    success, frame = camera.read()

    if not success:
        print("Camera error")
        break


    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )


        cv2.putText(
            frame,
            "Face",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )


        cv2.putText(
            frame,
            f"Faces detected: {len(faces)}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )

    cv2.imshow("Face Detection",frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()