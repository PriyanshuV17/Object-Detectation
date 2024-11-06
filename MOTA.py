import cv2

# Initialize MultiTracker
multi_tracker = cv2.MultiTracker_create()

# Capture video from file or webcam
video = cv2.VideoCapture(0)  # Use 0 for webcam or provide a video file path

if not video.isOpened():
    print("Could not open video")
    sys.exit()

# Read the first frame
ok, frame = video.read()
if not ok:
    print("Cannot read video file")
    sys.exit()

# Allow the user to select multiple bounding boxes for multiple objects
bboxes = []
while True:
    bbox = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
    bboxes.append(bbox)
    print("Press 'c' to confirm selection or any other key to add more objects")
    if cv2.waitKey(0) & 0xFF == ord('c'):
        break

# Initialize MultiTracker with the first frame and all bounding boxes
for bbox in bboxes:
    multi_tracker.add(cv2.TrackerKCF_create(), frame, bbox)

# Process the video
while True:
    ok, frame = video.read()
    if not ok:
        break

    # Update all the trackers and get the updated positions of all objects
    ok, boxes = multi_tracker.update(frame)

    # Draw the bounding boxes
    for box in boxes:
        p1 = (int(box[0]), int(box[1]))
        p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

    # Display the frame
    cv2.imshow("Multi-Object Tracking", frame)

    # Exit if the ESC key is pressed
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to stop
        break

# Release video capture and close windows
video.release()
cv2.destroyAllWindows()
