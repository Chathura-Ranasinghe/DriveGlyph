import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("D:/Projects/DriveGlyph/best.pt")

# Capture a frame from the video source
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Flip the frame horizontally
    flipped_frame = cv2.flip(frame, 1)

    # Predict on the flipped frame
    model.predict(source=flipped_frame, show=True, conf=0.8)

    # Wait until a key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close any open windows
cap.release()
cv2.destroyAllWindows()