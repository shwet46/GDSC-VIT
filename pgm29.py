from PIL import Image, ImageFilter

def resize_image(input_path, output_path, size):
    try:
        image = Image.open(input_path)
        resized_image = image.resize(size)
        resized_image.save(output_path)
        print(f"Resized image and saved it to {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

def crop_image(input_path, output_path, box):
    try:
        image = Image.open(input_path)
        cropped_image = image.crop(box)
        cropped_image.save(output_path)
        print(f"Cropped image and saved it to {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

def apply_filter(input_path, output_path, filter_name):
    try:
        image = Image.open(input_path)
        filtered_image = image.filter(filter_name)
        filtered_image.save(output_path)
        print(f"Applied filter and saved it to {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    input_image_path = "input.jpg"
    output_image_path = "output.jpg"

    # Example: Resize image to 300x300 pixels
    resize_image(input_image_path, output_image_path, (300, 300))

    # Example: Crop image from (100, 100) to (400, 400)
    crop_box = (100, 100, 400, 400)
    crop_image(input_image_path, output_image_path, crop_box)

    # Example: Apply a Gaussian blur filter
    apply_filter(input_image_path, output_image_path, ImageFilter.GaussianBlur(5))
