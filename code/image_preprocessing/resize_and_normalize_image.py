from PIL import Image
import numpy as np

def resize_and_normalize_image(image_path, target_size=(512, 512), mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)):
    # Step 1: Load and preprocess the image
    image = Image.open(image_path).convert("RGB")
    
    # Preserve aspect ratio
    original_size = image.size
    ratio = min(target_size[0] / original_size[0], target_size[1] / original_size[1])
    new_size = (int(original_size[0] * ratio), int(original_size[1] * ratio))
    image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    # Create a new image with the target size and paste the resized image onto it
    new_image = Image.new("RGB", target_size)
    new_image.paste(image, ((target_size[0] - new_size[0]) // 2, (target_size[1] - new_size[1]) // 2))
    
    # Convert to NumPy array and normalize
    arr = np.array(new_image, dtype=np.float32) / 255.0
    arr = (arr - mean) / std  # Normalize
    
    # Step 2: Revert normalization (denormalize)
    arr = (arr * std) + mean  # Denormalize
    arr = (arr * 255.0).clip(0, 255).astype('uint8')  # Rescale to [0, 255] and ensure valid range
    
    # Step 3: Convert back to an image
    processed_image = Image.fromarray(arr)
    return processed_image

if __name__ == "__main__":
    img = resize_and_normalize_image("data/images/sample_customer_images/sample_customer_screenshot.png")
    img.show() 