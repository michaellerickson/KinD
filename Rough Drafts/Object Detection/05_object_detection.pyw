
import cv2
import numpy as np

def detect_objects(model, output_layers, classes, image_path, confidence_threshold=0.5):
    
    Detect objects in an image using a pre-configured model.

    model: Pre-configured object detection model (e.g., YOLO or SSD).
    output_layers: Names of the output layers in the model.
    classes: List of class names.
    image_path: Path to the image for detection.
    confidence_threshold: Confidence threshold for detection.
    :return: List of detected objects with class names, confidence scores, and bounding boxes.
    
    # Read image
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Prepare the image for the model
    blob = cv2.dnn.blobFromImage(image, scalefactor=1/255.0, size=(416, 416), swapRB=True, crop=False)
    model.setInput(blob)

    # Perform forward pass
    detections = model.forward(output_layers)

    # Parse detections
    detected_objects = []
    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confidence_threshold:
                # Scaling bounding box coordinates
                box = obj[0:4] * np.array([width, height, width, height])
                (centerX, centerY, box_width, box_height) = box.astype("int")
                x = int(centerX - (box_width / 2))
                y = int(centerY - (box_height / 2))

                detected_objects.append((classes[class_id], confidence, (x, y, box_width, box_height)))

    return detected_objects

def test_detection(model, output_layers, classes, image_path):
    """
    Test object detection by displaying detected objects in an image.

    model: Pre-configured object detection model.
    output_layers: Names of the output layers in the model.
    classes: List of class names.
    image_path: Path to the image for testing.
    :return: None
    """
    detected_objects = detect_objects(model, output_layers, classes, image_path)

    # Read image
    image = cv2.imread(image_path)

    # Draw bounding boxes and labels
    for (class_name, confidence, (x, y, w, h)) in detected_objects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = f"{class_name}: {confidence:.2f}"
        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display image
    cv2.imshow('Detected Objects', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
# model, output_layers, classes = ...  # As configured in yolo_config.py or ssd_config.py
# image_path = 'path_to_image.jpg'
# test_detection(model, output_layers, classes, image_path)
