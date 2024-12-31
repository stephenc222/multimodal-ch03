from PIL import Image

def convert_to_grayscale(image_path):
    image = Image.open(image_path).convert("L")  # <1>
    return image  # <2>

if __name__ == "__main__":
    # Example usage
    gray_img = convert_to_grayscale("data/images/sample_customer_images/sample_customer_screenshot.png")  # <3>
    gray_img.show()  # <4>