"""
####      Project  chess  by Udit Pramanik


## Installation of  external libraries used

# !pip install opencv-python    to install opencv
# !pip install numpy            to install numpy  

"""

import cv2
import numpy as np


#Message declarations for the program user
for i in range(5):
    print(".")
print("The File with FEN Notation must be in the same folder as this program")
print("The File with chess_pieces  must be in the same folder as this program")




### Colour scheme for board   
    
## [blue] 
background_colour=(230, 216, 173)  #Light squares
square_colour=(143, 143, 8)    #Dark squares
text_colour=(79,69,54)


##  Another Colour scheme [green] for board (Uncomment the block to use this colour scheme alternatively)
# background_colour=(144, 238, 144)  #Light squares
# square_colour=(96, 158, 0)     #Dark squares
# text_colour=(79,69,54)


## Another colour scheme for board [brown] (Uncomment the block to use this colour scheme alternatively)
# background_colour=(179,222,245) #Light squares
# square_colour=(107,154,193)   #Dark squares
# text_colour=(120,120,120)




### Chessboard Creation


#   Creation of background of 800 X 800 pixels  using numpy arrays
background=np.zeros((800,800,3),dtype= np.uint8) #datatype is uint=unsigned integer
background[:,0:800]= background_colour           #assigning colour


##  Drawing  darker square pattern  on the background on the vertical and horizontal axis using cv2.rectange() method.
#   (to replicate the form of a chessboard)
#   Vertical axis
for i in range(100,800,200):
    for j in range(200,900,200):
        board = cv2.rectangle(background, (i,j),(i-100,j-100), square_colour, -1)
    
#   Horizontal axis    
for k in range(0,700,200):
    for l in range(100,800,200):
          board = cv2.rectangle(background, (l,k),(l+100,k+100), square_colour, -1)
    
     



#  Function effectively used to display the image in the program(rectifying the cv2.imshow display problem)
def display_image(img):
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



## To display just the chessboard without pieces
# display_image(board)



## Converting the image of the board to format with 4 channels(.png,4th_ch - alpha channel)
# (to facilitate better merging with chess pieces later)


#Splitting image into individual channels          
b_chan, g_chan, r_chan = cv2.split(board)   
#creating a dummy alpha channel image using numpy with similar shape and data type as the second channel for similarity                    
alpha_chan = np.ones(b_chan.shape, dtype=b_chan.dtype) * 25  
 #Merging individual channels into images along with alpha channel   
board_BGRA = cv2.merge((b_chan, g_chan, r_chan, alpha_chan))     



#Dummy variable to avoid mismatch or overlapp for the board image with alpha channel 
eb1=board_BGRA
#For better debugging purpose
# display_image(eb1)





#Function to merge two images of .png format with similar dimensions (used to merge chess piece image with the background)

def image_merge(bg_img,piece_img):
    alpha_c = piece_img[:, :, 3]           #Creation of alpha channel
    alpha_in = 255.0 - alpha_c             #Inversion of alpha channel 

#Merging of alpha channel with the image of the pieces and inverted alpha channel with the background for all the BGRA layers
    for c in range(3):
        bg_img[:, :, c] = (alpha_c/255.0 * piece_img[:, :, c] + alpha_in/255.0 * bg_img[:,:, c])  #The channels are normalized by dividing by 255.0 
    return bg_img                           #Returing merged image





    
## Slicing chess pices from image provided into individual chess pieces using slicing operation on images

pieces={}   #declaration of the dictionary for pieces
piec= cv2.imread('chess_pieces.png',cv2.IMREAD_UNCHANGED)  # Reading the provided image in unchanged format( .png )


##Slicing operation and assigning image of pieces to individual letters

# Black pieces
p= piec[100:200, 0:100]     #Black pawn
n= piec[100:200, 100:200]   #Black knight
b= piec[100:200, 200:300]   #Black bishop
r= piec[100:200, 300:400]   #Black rook
q= piec[100:200, 400:500]   #Black queen
k= piec[100:200, 500:600]   #Black king


# #White pieces
P= piec[0:100, 0:100]     #White pawn
N= piec[0:100, 100:200]   #White knight
B= piec[0:100, 200:300]   #White bishop
R= piec[0:100, 300:400]   #White rook
Q= piec[0:100, 400:500]   #White queen
K= piec[0:100, 500:600]   #White king



#Chess pieces stored into a dictionary for convience in cross referencing later.
pieces['p']=p;pieces['n']=n;pieces['b']=b;pieces['r']=r;pieces['q']=q;pieces['k']=k
pieces['P']=P;pieces['N']=N;pieces['B']=B;pieces['R']=R;pieces['Q']=Q;pieces['K']=K
    




#Function to read FEN notation file
def read_fenfile(path):
    with open(path,"rt") as sd:
        for f in sd:
            fen=f.split(" ")[0]     #Splitting the text from FEN notation file to be able to read the required part. 
            return fen              #Returing the FEN notation
            
        
        


### Reading FEN notation from file            


n=input("Enter File name with extension :")  #Input the file name in text format from the user
ab=read_fenfile(f"{n}")                      #Reading the corresponding file
row=ab.split("/")                            #Extracting the concerned part of FEN number   
bp=[]                                        #Declaration of empty list for convinience
pd=[]                                        #Declaration of empty list for convinience

for i in range(0,len(row)):
    a=row[i]                                #Stores FEN notation of each row 
    countfl = 0                             #Counting the occurence of numbers in FEN notation of a single row
    fl = 0                                  #Variable to store the number/digit from FEN  for calculation 
    for j in range(0,len(a)):
        pos=a[j]                            #Stores each letter/number of the FEN notation
 
# Condition if we encounter a digit(number) in FEN notation       
        if(pos=='2' or pos=='3' or pos=='1' or pos=='8' or pos=='4'or pos=='5'or pos=='6'or pos=='7'  ):   
            countfl += 1 -fl                #Calculation for number- count to be used as a general formula in the loop
            fl=int(pos)                     #Conversion into integer as number detected is a string     
        else:
#Slicing of board to enable merging with image of pieces with similar dimensions            
            bp=eb1[i*100:i*100+100,(j-countfl+fl)*100:(j-countfl+fl)*100+100]
#Merging the individual chess pieces with the background               
            pd=image_merge(bp, pieces[str(pos)])   
#Merging the merged piece above back into the chessboard                                         
            eb1[i*100:i*100+100,(j-countfl+fl)*100:(j-countfl+fl)*100+100]=pd               
            
            


## Labelling of the text board                    
                    
                    
#  Using cv2.putText() method
#  cv2.putText(image, text, org, font, fontScale, color, thickness)

#For 1-8 coordinates
for i in range(715,14,-100):
    org=(790,i)
    text=cv2.putText(eb1,f"{int(((800-i)+15)/100)}", org, cv2.FONT_HERSHEY_PLAIN, 0.8, text_colour,2)

#For a-h coordinates
for l in range(0,8):
    org=((l*100)+3,796)
    text=cv2.putText(eb1,f"{chr(l+97)}", org, cv2.FONT_HERSHEY_PLAIN, 0.8,text_colour,2)
    

    

#Splitting of image with text into seperate channels 
b_ch, g_ch, r_ch,alpha= cv2.split(text) 
#Merging without the alpha channel to erradicate problems with additional transparent layer on top of required image
final_image = cv2.merge((b_ch, g_ch, r_ch)) 
        
#To display the final Image
display_image(final_image)


#Instruction for the user 
for i in range(5):
    print(".")
print("Close the window containing the board image to get the exported image file properly")


#To write the final image in a .png file format with the same name as input file
fimg=n.split(".")                          #Extracting the file name from the input without its extension
cv2.imwrite(f"{fimg[0]}.png",final_image)
