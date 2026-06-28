# Object Orientation Detection using OpenCV

## 📌 Project Overview

This project is a real-time object orientation detection system developed using **Python**, **OpenCV**, and **NumPy**.

The application captures live video from a **webcam** or **DroidCam**, detects the largest object in the frame using contour detection, and calculates its orientation angle using **Principal Component Analysis (PCA)**.

The detected object is highlighted with a **green contour**, and its orientation is represented by a **blue axis** along with the calculated angle.

---

## ✨ Features

- Live video capture using Webcam or DroidCam
- Real-time object detection
- Contour detection using OpenCV
- PCA-based object orientation estimation
- Green contour around the detected object
- Blue orientation axis
- Live angle display
- Real-time processing

---

## 🛠 Technologies Used

- Python 3
- OpenCV
- NumPy
- DroidCam (Optional)

---

## ⚙️ How It Works

1. Capture live video from the camera.
2. Convert the frame to grayscale.
3. Apply Gaussian Blur to reduce image noise.
4. Perform binary thresholding.
5. Detect contours in the threshold image.
6. Select the largest contour.
7. Simplify the contour using polygon approximation.
8. Apply Principal Component Analysis (PCA).
9. Draw the contour and orientation axis.
10. Display the orientation angle on the live video.

---

## 📂 Files

```
live_orientation.py
Sooraj_M2C_Software & AI Department
README.md
```

---

## 📷 Output

The application displays:

- Live camera feed
- Green contour around the detected object
- Blue orientation axis
- Object orientation angle (degrees)
- Detected contour area

---

## ⚠️ Limitations

- Detects the largest object in the frame.
- Best performance is achieved with a plain background and good lighting.
- Detection accuracy depends on the quality of contour extraction.
- Nearly square objects may produce slight orientation fluctuations.

---

## 🚀 Future Improvements

- Improve contour filtering for complex backgrounds.
- Increase orientation stability.
- Support multiple object detection.
- Integrate AI-based object detection in future versions.

---

## 👨‍💻 Author

**Sooraj Krishna J**

B.Tech Mechanical Engineering Student

---

## 📄 License

This project is intended for educational and academic purposes.
