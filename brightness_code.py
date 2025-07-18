import os
from PIL import Image, ImageEnhance

def adjust_brightness_for_folder(input_folder, output_folder, levels):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            input_image_path = os.path.join(input_folder, filename)
            image = Image.open(input_image_path)
            for level in levels:
                enhancer = ImageEnhance.Brightness(image)
                brightened_image = enhancer.enhance(level)
                output_image_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_brightness_{level:.1f}{os.path.splitext(filename)[1]}")
                brightened_image.save(output_image_path)

if __name__ == "__main__":
    input_folder = "<input_folder_path>"
    output_folder = "<output_folder_path>"
    brightness_levels = [0.1 * i for i in range(1, 11)]  # 10 different levels of brightness

    adjust_brightness_for_folder(input_folder, output_folder, brightness_levels)
