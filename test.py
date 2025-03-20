import cv2

def check_webcam():
    for i in range(4):  # Check indices 0 to 3 (you can increase the range)
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Webcam found at index {i}")
            cap.release()
            return i  # Return the working index
        else:
            print(f"Webcam NOT found at index {i}")
    return None  # No webcam found in tested indices

webcam_index = check_webcam()

if webcam_index is not None:
    print(f"Using webcam at index: {webcam_index}")
    cap = cv2.VideoCapture(webcam_index) # Use the working index
    if not cap.isOpened(): # Double check again after finding index
         print("ERROR: Still could not open webcam even with found index.")
         exit()
else:
    print("ERROR: No webcam found at indices 0, 1, 2, 3. Please check webcam connection and drivers.")
    exit()

# ... rest of your code (DeepFace, Gemini, etc.) ...

while True: # Keep the rest of your code the same from the while loop onwards
    ret, frame = cap.read()
    if not ret:
        print("ERROR: проблем with capturing frame from webcam. Exiting inside loop.") # More specific error
        break
    # ... rest of your while loop ...