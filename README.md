# ColorDetector
Its an Color Detector GUI using python.

Required liabraries:
1. tkinter
2. PIL (pillow)
3. colorthief
4. os


1.Tkinter:

Purpose: Tkinter is the standard GUI (Graphical User Interface) library in Python. It is used to create windows, dialogs, buttons, labels, and other GUI elements.
Functions and Classes Used:
  Tk(): Creates the main application window.
  Label: Used to create text or image labels.
  Button: Used to create clickable buttons.
  Frame: Used to group and organize widgets.
  Canvas: Used for drawing shapes and images.
  filedialog: A module within Tkinter that provides file selection dialogs.


2.PIL (Pillow):

Purpose: Pillow is a fork of the Python Imaging Library (PIL) that adds support for opening, manipulating, and saving many different image file formats.
Functions and Classes Used:
  Image: Used to open and manipulate images.
  ImageTk: Used to convert images from PIL format to a format that Tkinter can display.

3.colorthief:

Purpose: The colorthief library is used to extract dominant colors from an image.
Functions and Classes Used:
  ColorThief: The main class used to load an image and extract its color palette.
  get_palette(): A method of the ColorThief class that retrieves a specified number of dominant colors from the image.
  
4.os:

Purpose: The os module provides a way of using operating system-dependent functionality, like reading or writing to the file system.
Functions Used:
  os.getcwd(): Returns the current working directory. Used here to set the initial directory for the file dialog.
  







