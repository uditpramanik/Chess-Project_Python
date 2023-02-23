"""
####      Project Python chess board by Udit Pramanik


## Installation of  external libraries used

# !pip install opencv-python    to install opencv
# !pip install numpy            to install numpy  


"""



import cv2
import numpy as np

for i in range(5):
    print(".")
print("Put the File with FEN Notation in the same folder as this program")


def display_image(img):
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
## Colour scheme for board (Uncomment the block to use alternatively)

background_colour=(230, 216, 173) 
foreground_colour=(143, 143, 8)
text_colour=(79,69,54)




## Another colour scheme for board (Uncomment the block to use alternatively)

# background_colour=(179,222,245) #Light squares
# foreground_colour=(107,154,193)   #Dark squares
# text_colour=(120,120,120)


## Chessboard Creation

#Creation of background of 800 X 800 pixels 

background=np.zeros((800,800,3),dtype= np.uint8) #uint=unsigned integer
background[:,0:800]= background_colour


# Vertical axis
for i in range(100,800,200):
    for j in range(200,900,200):
        board = cv2.rectangle(background, (i,j),(i-100,j-100), foreground_colour, -1)
    
     
#  Horizontal axis    
for k in range(0,700,200):
    for l in range(100,800,200):
          board = cv2.rectangle(background, (l,k),(l+100,k+100), foreground_colour, -1)
    
     

#Long-form for Chessboard generation
   
# # # #Horizontal
# image = cv2.rectangle(background, (100,0),(200,100), (80,100,200), -1)
# image = cv2.rectangle(background, (300,0),(400,100), (80,100,200), -1)
# image = cv2.rectangle(background, (500,0),(600,100), (80,100,200), -1)
# image = cv2.rectangle(background, (700,0),(800,100), (80,100,200), -1)


# image = cv2.rectangle(background, (100,200),(200,300), (80,100,200), -1)
# image = cv2.rectangle(background, (300,200),(400,300), (80,100,200), -1)
# image = cv2.rectangle(background, (500,200),(600,300), (80,100,200), -1)
# image = cv2.rectangle(background, (700,200),(800,300), (80,100,200), -1)


# image = cv2.rectangle(background, (100,400),(200,500), (80,100,200), -1)
# image = cv2.rectangle(background, (300,400),(400,500), (80,100,200), -1)
# image = cv2.rectangle(background, (500,400),(600,500), (80,100,200), -1)
# image = cv2.rectangle(background, (700,400),(800,500), (80,100,200), -1)

# image = cv2.rectangle(background, (100,600),(200,700), (80,100,200), -1)
# image = cv2.rectangle(background, (300,600),(400,700), (80,100,200), -1)
# image = cv2.rectangle(background, (500,600),(600,700), (80,100,200), -1)
# image = cv2.rectangle(background, (700,600),(800,700), (80,100,200), -1)
    
    
    
# # # Vertical
# image = cv2.rectangle(background, (100,200),(0,100), (80,100,200), -1)
# image = cv2.rectangle(background, (100,400),(0,300), (80,100,200), -1)
# image = cv2.rectangle(background , (100,600),(0,500), (80,100,200), -1)
# image = cv2.rectangle(background, (100,800),(0,700), (80,100,200), -1)
        
# image = cv2.rectangle(background, (300,200),(200,100), (80,100,200), -1)
# image = cv2.rectangle(background, (300,400),(200,300), (80,100,200), -1)
# image = cv2.rectangle(background, (300,600),(200,500), (80,100,200), -1)
# image = cv2.rectangle(background, (300,800),(200,700), (80,100,200), -1)
        
# image = cv2.rectangle(background, (500,200),(400,100), (80,100,200), -1)
# image = cv2.rectangle(background, (500,400),(400,300), (80,100,200), -1)
# image = cv2.rectangle(background, (500,600),(400,500), (80,100,200), -1)
# image = cv2.rectangle(background, (500,800),(400,700), (80,100,200), -1)

# image = cv2.rectangle(background, (700,200),(600,100), (80,100,200), -1)
# image = cv2.rectangle(background, (700,400),(600,300), (80,100,200), -1)
# image = cv2.rectangle(background, (700,600),(600,500), (80,100,200), -1)
# image = cv2.rectangle(background, (700,800),(600,700), (80,100,200), -1)
        

## To display just the chessboard without pieces
# cv2.imshow("Chessboard",board)

#Dummy variable to avoid mismatch or overlapp for board image
eb=board


## Creation of alpha channel (to facilitate better merging with chess pieces later)
b_chan, g_chan, r_chan = cv2.split(board)
alpha_chan = np.ones(b_chan.shape, dtype=b_chan.dtype) * 25 #creating a dummy alpha channel image.
img_BGRA = cv2.merge((b_chan, g_chan, r_chan, alpha_chan))



#Dummy variable to avoid mismatch or overlapp for the board image with alpha channel 
eb1=img_BGRA


# cv2.imshow("board",eb1)

# display_image(eb1)



        
#Function to merge the chess piece image with the background

def image_merge(bg_img,piece_img):
    alpha_s = piece_img[:, :, 3]           #Creation of alpha channel
    alpha_in = 255.0 - alpha_s               #Inversion of alpha channel 
    for c in range(3):
        bg_img[:, :, c] = (alpha_s/255.0 * piece_img[:, :, c] + alpha_in/255.0 * bg_img[:,:, c])  
    return bg_img





    

##Slicing chess pices from image provided into individual chess pieces

pieces={}  
piec= cv2.imread('chess_pieces.png',cv2.IMREAD_UNCHANGED)  # 
# for pi in range(1,7):
#     print(pi*100-100,pi*100)
#     p[pi]=pieces[100:200, pi*100-100:pi*100]

# #Black pieces
p= piec[100:200, 0:100]     #Black pawn
n= piec[100:200, 100:200]   #Black knight
b= piec[100:200, 200:300]   #Black bishop
r= piec[100:200, 300:400]   #Black rook
q= piec[100:200, 400:500]   #Black queen
k= piec[100:200, 500:600]   #Black king

bem=eb[0:100,100:200]


# #White pieces
P= piec[0:100, 0:100]     #White pawn
N= piec[0:100, 100:200]   #White knight
B= piec[0:100, 200:300]   #White bishop
R= piec[0:100, 300:400]   #White rook
Q= piec[0:100, 400:500]   #White queen
K= piec[0:100, 500:600]   #White king

wem=eb[0:100,100:200]

pieces['p']=p;pieces['n']=n;pieces['b']=b;pieces['r']=r;pieces['q']=q;pieces['k']=k
pieces['P']=P;pieces['N']=N;pieces['B']=B;pieces['R']=R;pieces['Q']=Q;pieces['K']=K
    



    


# #Let us say dimensions of china image (china.shape) is 427 x 640 x 3. And we want to extract the portion of this image, and dimensions of this portion are - row numbers from 150 to 220 and column numbers from 130 to 250 in the 'china' NumPy array.



 
 
#Function to read FEN notation file

def read_fenfile(path):
    with open(path,"rt") as sd:
        for f in sd:
            fen=f.split(" ")[0]
            return fen           
            
        
        
# #Reading FEN notation from file            



# ab=read_fenfile(r"Default_FEN.txt")
# row=ab.split("/")
# bp=[]
# pd=[]

# for i in range(0,len(row)):
#     a=row[i]
#     countfl = 0
#     fl = 0
#     for j in range(0,len(a)):
#         pos=a[j]
        
#         if(pos=='2' or pos=='3' or pos=='1' or pos=='8' or pos=='4'or pos=='5'or pos=='6'or pos=='7'  ):
#             countfl += 1 -fl
#             fl=int(pos)           
#         else:
#             # print(f"{i*100}:{i*100+100},{(j-countfl+fl)*100}:{(j-countfl+fl)*100+100}")
#             bp=eb1[i*100:i*100+100,(j-countfl+fl)*100:(j-countfl+fl)*100+100]
#             pd=image_merge(bp, pieces[str(pos)])
#             eb1[i*100:i*100+100,(j-countfl+fl)*100:(j-countfl+fl)*100+100]=pd
            
            


n=input("Enter File name with extension :")
ab=read_fenfile(f"{n}")
row=ab.split("/")
bp=[]
pd=[]

for i in range(0,len(row)):
    a=row[i]
    countfl = 0
    fl = 0
    for j in range(0,len(a)):
        pos=a[j]
        
        if(pos=='2' or pos=='3' or pos=='1' or pos=='8' or pos=='4'or pos=='5'or pos=='6'or pos=='7'  ):
            countfl += 1 -fl
            fl=int(pos)           
        else:
            # print(f"{i*100}:{i*100+100},{(j-countfl+fl)*100}:{(j-countfl+fl)*100+100}")
            bp=eb1[i*100:i*100+100,(j-countfl+fl)*100:(j-countfl+fl)*100+100]
            pd=image_merge(bp, pieces[str(pos)])
            eb1[i*100:i*100+100,(j-countfl+fl)*100:(j-countfl+fl)*100+100]=pd
            
            




## Labelling of the text board                    
                    
                    
# # Using cv2.putText() method
# #cv2.putText(image, text, org, font, fontScale, color, thickness)

for i in range(715,14,-100):
    org=(790,i)
    text=cv2.putText(eb1,f"{int(((800-i)+15)/100)}", org, cv2.FONT_HERSHEY_PLAIN, 0.8, text_colour,2)

for l in range(0,8):
    org=((l*100)+3,796)
    text=cv2.putText(eb1,f"{chr(l+97)}", org, cv2.FONT_HERSHEY_PLAIN, 0.8,text_colour,2)
    



        
display_image(text)

fimg=n.split(".")
print(f"{fimg[0]}.png")
cv2.imwrite(f"{fimg[0]}.png",fimg)

# # cv2.imshow("text",text)
# cv2.imwrite("Chessboard.png",text)












