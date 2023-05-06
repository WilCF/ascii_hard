---

# Image to ASCII Converter

This Python script takes an input image file in one of the popular image formats, converts it to ASCII art, and saves the output as a `.HARD` file, per Steve's insatiable demands.

## Features

- Supports popular image formats (JPEG, PNG, GIF, BMP, TIFF, etc.).
- Resizes and maintains the aspect ratio of the input image.
- Converts the image to greyscale before generating ASCII art.
- Adds a progress bar using the colorama library.

## Requirements

- Python 3.x
- Pillow
- colorama

## Installation

1. Clone the repository or download the `image_to_ascii.py` file.

2. Install the required packages:

```sh
pip install Pillow
pip install colorama
```

## Usage

Run the script from the command line, providing the path to the input image file:

```sh
python image_to_ascii.py path_to_input_image
```

Replace `path_to_input_image` with the path to the input image file you want to convert.

The script will create an ASCII art file with the same name as the input image but with a `.HARD` extension in the same directory.

## Example

Suppose you have an image called `example.jpg`. To convert it to ASCII art, run:

```sh
python image_to_ascii.py example.jpg
```

The script will generate a file called `example.HARD` containing the ASCII art.

## License

This project is licensed under the MIT License.

---

This README file provides an overview of the image-to-ASCII Python script, its features, requirements, installation steps, and usage. You can use this as a starting point for your project's README on GitHub. If you need any help or have questions, please let me know!
