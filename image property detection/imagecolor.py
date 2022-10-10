import cv2
import pandas as pd
import argparse


ap = argparse.ArgumentParser()   
ap.add_argument('-i', '--image', help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
img = cv2.imread(img_path)
# img = cv2.imread('bg.jpeg')

clicked=False
r=g=b=0


index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        
        
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname





cv2.destroyAllWindows()