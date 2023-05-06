# Import necessary libraries
from PIL import Image
import os
import sys
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Define the image_to_ascii function
def image_to_ascii(image_path, output_path):
    # Open the image file
    image = Image.open(image_path)
    # Get the width and height of the image
    image_width, image_height = image.size
    # Calculate the aspect ratio of the image
    aspect_ratio = image_height / float(image_width)
    # Set the new width and calculate the new height while maintaining the aspect ratio
    new_width = 80
    new_height = int(aspect_ratio * new_width)

    # Resize the image with the new dimensions
    resized_image = image.resize((new_width, new_height))
    # Convert the resized image to greyscale
    greyscale_image = resized_image.convert('L')
    # Get the pixel data of the greyscale image
    pixels = greyscale_image.getdata()
    # Define the ASCII characters used for conversion
    ascii_chars = ['@', '%', '#', '*', '+', '=', '-', ';', ':', ',', '.']
    # Map the pixels to ASCII characters
    new_pixels = [ascii_chars[pixel // 25] for pixel in pixels]
    # Combine the ASCII characters into a single string
    ascii_image = ''.join(new_pixels)

    # Split the ASCII string into lines based on the new_width
    ascii_image = [ascii_image[index:index + new_width] for index in range(0, len(ascii_image), new_width)]
    # Join the lines with newline characters to form the final ASCII image
    ascii_image = "\n".join(ascii_image)
    
    # Write the ASCII image to the output file
    with open(output_path, 'w') as f:
        f.write(ascii_image)

    # Print the progress bar
    print(f"{Fore.GREEN}Converting image to ASCII:")
    for i in range(101):
        progress = '#' * (i // 2)
        spaces = ' ' * (50 - len(progress))
        print(f"\r{Fore.GREEN}[{progress}{spaces}] {i}% ", end='')
        sys.stdout.flush()

# Main function
if __name__ == '__main__':
    # Get the input file path from the command-line argument
    input_file = sys.argv[1]
    # Remove the file extension from the input file
    file_name, _ = os.path.splitext(input_file)
    # Create the output file path with the .hard extension
    output_file = f"{file_name}.HARD"
    # Call the image_to_ascii function to convert the input image and save it as a .hard file
    image_to_ascii(input_file, output_file)
    print(f"\n{Fore.GREEN}Image converted and saved as {output_file}.HARD you HARDBOY you")
