import cv2
import sys
from screeninfo import get_monitors

video_path = r'C:/Users/sandboxadmin/Videos/20230828.mp4' # PATH TO VIDEO

def setup_environment():

    # Set up the OpenCV environment.
    # This includes checking the OpenCV version and configuring GPU support if available

    # Get and print OpenCV version
    # Check OpenCV version
    major_ver, minor_ver, subminor_ver = cv2.__version__.split('.')
    print(f"OpenCV Version: {major_ver}.{minor_ver}.{subminor_ver}")

    # Check for GPU support and configure if available
    if cv2.cuda.getCudaEnabledDeviceCount() == 0:
        print("No GPU found, using CPU.")
    else:
        cv2.cuda.setDevice(0)
        print("GPU found, using GPU.")
    
    print("OpenCV environment set up successfully.")
    
def test_processing(video_path):
    # Get the screen size
    monitor = get_monitors()[0]
    screen_width, screen_height = monitor.width, monitor.height
    
    # Calculate the desired dimensions as a percentage of the screen size
    desired_width = int(screen_width * 0.35)
    desired_height = int(screen_height * 0.5)
    
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Check if video opened successfully
    if not video.isOpened():
        print("Error: Could not open video file.")
        sys.exit()
        
    print("Testing video processing...")
    
    while True:
        ret, frame = video.read()
        
        # Break the loop if the video has ended
        if not ret:
            break

# Resize the frame to the desired dimensions
        frame_resized = cv2.resize(frame, (desired_width, desired_height))
        
        # Display the resized frame
        cv2.imshow('Frame', frame_resized)
        
        # Press 'q' to exit the video window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # Release the video object and close windows
    video.release()
    cv2.destroyAllWindows()
    print("Video processing test completed.")

# Set up the OpenCV environment
setup_environment()

# Test video processing by displaying the video frames
test_processing(video_path)
