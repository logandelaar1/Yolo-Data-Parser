# Image Processing and YOLO Data Parsing Scripts

This repository consists of Python scripts for various image processing tasks including filtering, sorting, renaming images, and parsing YOLO label files.

## Scripts Description

- **filter.py**: A script that allows the user to view images from a source directory and decide whether to delete or move them to a target directory. It uses OpenCV to open and display images.

- **imagesort.py**: Similar to `filter.py`, this script allows the user to view images and decide to delete or move them to a target directory. However, it uses the Python Imaging Library (PIL) to open and display images.

- **rename.py**: A script used to rename all `.jpg` files in a specified directory. The files are renamed in numerical order and moved to a destination folder.

- **yolodataparser_autodelete.py**: A YOLO data parser that automatically deletes all lines in text files within a directory that start with '0'.

- **yolodataparser_manual.py**: A more complex YOLO data parser that presents images associated with YOLO label files to the user for manual annotation. After processing all images, the script moves any label and image files associated with empty label files to a separate directory.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.7 or later.
- You have a Windows/Linux/Mac machine with admin rights. This is required to install the necessary software packages.

## Installing Dependencies

To install the dependencies, run the following command:

```bash
pip install opencv-python pillow
