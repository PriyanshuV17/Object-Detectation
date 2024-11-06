import cv2
import sys

# Initialize the tracker
tracker = cv2.TrackerKCF_create()  # You can use other trackers like MIL, TLD, CSRT

# Capture video from file or webcam
video = cv2.VideoCapture(0)  # Use 0 for webcam, or provide a video file path

if not video.isOpened():
    print("Could not open video")
    sys.exit()

# Read the first frame
ok, frame = video.read()
if not ok:
    print("Cannot read video file")
    sys.exit()

# Select object to track
bbox = cv2.selectROI(frame, False)

# Initialize tracker with the first frame and bounding box
ok = tracker.init(frame, bbox)

while True:
    # Read a new frame
    ok, frame = video.read()
    if not ok:
        break

    # Update the tracker
    ok, bbox = tracker.update(frame)

    # Draw the bounding box
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        cv2.putText(frame, "Tracking failure", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display result
    cv2.imshow("Tracking", frame)

    # Exit if ESC is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()
