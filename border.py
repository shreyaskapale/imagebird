#Border generator using opencv
#credits - shreyas kapale
#github project - 28/9/2017  
import argparse 
import cv2
# import cv2 and argparse
p = argparse.ArgumentParser()
# create a argument parser  A and P should be capitol as it is
p.add_argument("-i", "--image", required=True, help="path to the image" )
# define the argument which should be passed
color=raw_input("Select the border colour (choose from red , blue, green, white, black ) : ")
# get input...ask for colour ! you can define whichever colour you want it should be in the form (b, g, r)
if color =="red":
	setcolor = (0, 0, 255)
elif color =="blue":
	setcolor = (255, 0, 0)
elif color =="green":
	setcolor = (0, 255, 0)
elif color == "black":
	setcolor = (0, 0, 0)
#conditions for colour and set it to border colour var setcolour

border=raw_input("Mention the border thickness from 0 to 10 : ")
# get input for border size and set to the border
border = int(border)
# remember to typedef it to int !! else border will take it as a char and you get a error !


args = vars(p.parse_args())
#set args to parsed argument 

image = cv2.imread(args["image"])
#set image to image file using imread function !
x = image.shape[1]
# set the width of the image ... as image.shape[1] will take the width of the input image
y = image.shape[0]
# similarly height
cv2.line(image,(0,0),(0,y),setcolor,border)
# now use line funtion to create to create a line from 0,0 cordinate to 0,y coordinate
cv2.line(image,(0,0),(x,0),setcolor,border)
# similary for all sides 
cv2.line(image,(x,0),(x,y),setcolor,border)
cv2.line(image,(0,y),(x,y),setcolor,border)

cv2.imshow("output", image)
cv2.waitKey(4000)

cv2.destroyAllWindows()

#display the rotated image
get = raw_input("Wanna save the image ? (yes/no): ")
if get =="yes":
	format = raw_input("Please name the new file name with its extension ex - new.jpg : ")
	cv2.imwrite(format, image)
	# to write the file ( SAVE FILE)
else:
	sys.exit(0)
#waikey ! remember K in Key is capitol
# this is to pause window
