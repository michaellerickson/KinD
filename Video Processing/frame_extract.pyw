# Import the required module `cv2` is from OpenCV
import cv2
import os

# Extract Frames
def extract_frames(video_path, output_path, frame_rate=30):

    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not video.isOpened():
        print("Error: Could not open video file.")
        return

    # Frame count
    frame_count = 0
      
    while True:
        ret, frame = video.read()

        # Break the loop if the video is ended
        if not ret:
            break  
      
        # Save frame at specified rate
        if frame_count % frame_rate == 0:
            frame_path = f"{output_path}/frame_{frame_count}.png"
            cv2.imwrite(frame_path, frame)
            print(f"Saved {frame_path}")

        frame_count += 1
    
# Release the video object and close windows
    video.release()
    cv2.destroyAllWindows()
    print("Frame extraction completed.")
       
# Call extract_frames function
video_path = r'C:/Users/sandboxadmin/Videos/20230828.mp4' #PATH TO THE VIDEO THAT NEEDS FRAMES EXTRACTED
output_path = r'C:/Users/sandboxadmin/Videos/frames' #PATH TO STORE FRAME(S)
frame_rate = 5 #ADJUST THIS TO CHOOSE HOW MANY FRAMES ARE CREATED PER SECOND | USE THE VIDEO FRAME RATE OVER THIS NUMBER
extract_frames(video_path, output_path, frame_rate)

# Preprocess Frames
def preprocess_frames(frame_path, output_path, resize_dims=(224, 224), grayscale=True):

    # Read the frame
    frame = cv2.imread(frame_path)

    # Resize the frame
    frame_resized = cv2.resize(frame, resize_dims)

    # Convert to grayscale if required
    if grayscale:
        frame_resized = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # Save the preprocessed frame
    cv2.imwrite(output_path, frame_resized)
    print(f"Preprocessed and saved frame at {output_path}")

# Call preprocess_frames function for each extracted frame
frame_path = r'C:/Users/sandboxadmin/Videos/frames/frame_0.png'

# Adjust this to match output_path/frame_0.png
output_path = r'C:/Users/sandboxadmin/Videos/preprocessed/frame_0.png'

# Path to store the preprocessed frame(s)
frames_dir = r'C:/Users/sandboxadmin/Videos/frames'
preprocessed_dir = r'C:/Users/sandboxadmin/Videos/preprocessed'
resize_dims = (224, 224)
grayscale = True

for frame_name in os.listdir(frames_dir):
	frame_path = os.path.join(frames_dir, frame_name)
	output_path = os.path.join(preprocessed_dir, frame_name)
	preprocess_frames(frame_path, output_path, resize_dims, grayscale)
