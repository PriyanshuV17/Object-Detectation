# Object Tracking Simulation Project Using OpenCV: MOTA, SOTA, and LSOT

This project is a dynamic object tracking simulation developed in Python using OpenCV and other libraries, featuring three primary tracking algorithms: **Multi-Object Tracking Algorithm (MOTA)**, **Single-Object Tracking Algorithm (SOTA)**, and **Large Single Object Tracking (LSOT)**. The simulation allows users to track multiple objects, a single object, or a large dominant object in real-time, with customizable features for each mode.

## Features
- **Multi-Object Tracking (MOTA):** Tracks multiple objects in real-time using the `MultiTracker` class from OpenCV, supporting unique ID assignment and accurate tracking through occlusions.
- **Single-Object Tracking (SOTA):** Utilizes OpenCV’s KCF tracker to follow a single object with high precision, adapting to occlusions and fast movements.
- **Large Single Object Tracking (LSOT):** Designed for large dominant objects in the frame, maintaining focus and bounding box stability, even with rapid motion.
- **Interactive Bounding Box Selection:** Allows users to select objects interactively in the first frame, providing flexibility in defining the tracked regions.
- **Real-Time Updates:** Real-time frame-by-frame object position updates, with consistent visualization of bounding boxes.
  
## Libraries Used
- **OpenCV (cv2):** Core library for computer vision tasks, used for object tracking, video processing, and interactive bounding box selection.
- **sys:** Assists in system control for managing video capture, ensuring a smooth exit if the video stream fails.

## Installation
To run this project, install the required libraries:
```bash
pip install opencv-python
```

## Usage
1. Clone the repository and navigate to the project folder.
2. Run the simulation script:
   ```bash
   python object_tracking_simulation.py
   ```
3. Follow the prompts to select objects to track:
   - For **MOTA**, select multiple objects by drawing bounding boxes and confirm each by pressing 'c'.
   - For **SOTA** and **LSOT**, select a single object to track.

4. Use the ESC key to exit the tracking session.

## File Structure
- `object_tracking_simulation.py` - Main script implementing MOTA, SOTA, and LSOT with interactive UI.
- `README.md` - Project documentation.

## Requirements
- Python 3.6+
- OpenCV 4.x

## Contributing
Feel free to submit issues or pull requests to improve the functionality or fix any bugs. 

---

This project is a practical example of using OpenCV for real-time object tracking, suitable for applications in surveillance, motion analysis, and real-world object detection tasks.



---

**PRIYANSHU VERMA**  
Registration Number: 22190503040  
Central University of Jharkhand  
Integrated B.Tech-M.Tech (5 years) in Computer Science and Engineering (Honors)  
Specialization: Machine Learning and Data Science  
Department of Computer Science and Engineering  
Mobile: +91 7376021218  

---
