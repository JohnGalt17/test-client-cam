# Camera1.py
import camera

print("Capturing image...")
img = camera.captureJPEG(300, 200)
camera.saveData(img, "/test.jpg")
print("JPEG saved")