# Chess-Project_Python
This program generates a chessboard and renders the chess pieces according to the FEN notation


The main code can be found in the .py(Python file) : Final_Project Chess.py

Additional Instruction can be found in the file : Readme for Git.pdf

All the files can be found together in an downloadable zip file titled :


Description :


This project report effectively describes a Python program which reads FEN notation as described in  problem statement from a file and  subsequently generates a 800 x 800 px chessboard based  populated with chesspieces based on the FEN notation.Then it exports the image in PNG format with the same file name as the input file.

External Libraries Used:

Numpy: Numpy is a very popular ,open-source and free Python external package for Scientific calculations especially for working with arrays and matrices. It has a variety of features which increases Python's computation capabilities much beyond the boundaries of standard python.Usually numpy is imported as a variable np and the same is used in the Python program and the report described.The pip module can effectively be used as a method of installation Syntax: pip install numpy

OpenCV: OpenCV is an open source external Python library widely used for image processing & computer vision which can be additionally used for machine learing.Usually OpenCV is imported as cv2 (Syntax: import cv2).However it is to be noted that OpenCV imports and uses the colour space BGR instead of the convensional RGB module which one needs to be careful about during its usage.The pip module can effectively be used as a method of installation Syntax: pip install opencv-python








Methodology used in writing the program:

•	First a background space is created for 800 x 800 pix and BGR format with 3 channels  using the numpy array.

•	Upon it a pattern repeatation of 100 x 100 pix darker squares is drawn  using the cv2.rectangle( ) feature along the vertical and horizontal axis of the background space to replicate the look of an entire chessboard.

•	 The board image is then converted into an image with 4 channels (BGRA) using a dummy alpha channel as the 4th channel to enable transparency and better merging of the chesspieces provides in the .png  format which itself contains 4 channel by default.

•	Liberty of introducing dummy variables was taken to avoid mismatch or overlapp.

•	The provided image titled “chess_pieces.png” was read unchanged as a .png format and using the image slicing operation, the individual pieces of the chessboard were obtained.

•	The chess pieces obtained were stored in a dictionary to make it easier to cross refference and place the pieces on the chessboard image accordingly 

•	An input from the user was programmed to be required which consists of the name of the file containg the FEN notation along with the file extension.(Syntax example:  M-1.txt )  

•	File containing the FEN notation was read and using the  norms of FEN notation were put into the respective rows and coloumns.

•	The board with pieces arranged from the FEN notation read was labelled with the coordinates as per the requirement of the game of chess

•	The image with coordinates was split into its individual channels and merged back without its alpha channel to erradicate the issue of  the added transparent layer existing on top of the required image while exporting it.

•	The final image was exported with the same file name as the input file but under .png format.The  generated image can be found in the same directory as the one with the Python program used.

•	Additionally a colour scheme was provided at  beginning of the program as an option to be chosen from.


