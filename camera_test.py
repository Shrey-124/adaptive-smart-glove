
import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not found. Check your camera connection.")
    raise SystemExit

while True:
    success, frame = camera.read()

    if not success:
        print("Could not read from camera.")
        break

    frame = cv2.flip(frame, 1)
    cv2.imshow("Smart Glove - Camera Test", frame)

    # Press Q to close the camera window
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
