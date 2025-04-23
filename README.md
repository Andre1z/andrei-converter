# EASY CONVERT - Image Converter Application

EASY CONVERT is a user-friendly Python application for converting images between various formats. It provides a drag-and-drop interface and supports popular formats like JPEG, PNG, BMP, GIF, WEBP, and TIFF.

## Features
- **Drag-and-Drop Interface**: Easily add files to convert.
- **Manual File Selection**: Browse and select images for conversion.
- **Format Support**: Convert between JPEG, PNG, BMP, GIF, WEBP, and TIFF.
- **Error Handling**: Notifies users of invalid file paths or missing input.

## Prerequisites
To run this application, you need:
- **Python 3.6 or later**
- The following Python libraries:
  - `tkinter`
  - `Pillow`
  - `tkinterdnd2` (installed automatically if missing)

## Installation
1. Clone this repository or download the source code as a ZIP file.
2. Ensure you have Python installed on your machine.
3. Install the required dependencies:
   ```bash
   pip install Pillow tkinterdnd2
   ```
 ## How to Use  
 1. Run the script:
 ```bash
 python convertidor_img.py
```
2. Drag and drop your image into the application or click the area to manually select a file.
3. Choose the desired output format from the dropdown menu.
4. Click "Convert Image" and save the file to your desired location.

## Notes
· If the selected image has an alpha channel (e.g., PNG) and you convert it to JPEG, the transparency will be removed, and the image will be converted to RGB mode.
· Ensure the ```logoconverter.ico``` file is available at the specified path, or update the icon path in the script.
