import cv2

def extract_keyframes(video_path, interval=2):
    """
    Extract frames from a video at a given time interval (in seconds).
    Returns a list of frames (as NumPy arrays).
    """
    cap = cv2.VideoCapture(video_path) # pylint: disable=no-member
    if not cap.isOpened():
        return []

    fps = cap.get(cv2.CAP_PROP_FPS) # pylint: disable=no-member
    frame_skip = int(fps * interval)
    keyframes = []
    frame_count = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        if frame_count % frame_skip == 0:
            keyframes.append((frame_count, frame))
        frame_count += 1

    cap.release()
    return keyframes

# Example usage
if __name__ == "__main__":
    frames = extract_keyframes("data/video/sample_video/customer_support_demo.mp4", interval=2)
    print(f"Extracted {len(frames)} keyframes.")
