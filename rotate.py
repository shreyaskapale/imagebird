#image rotator using opencv
#credits - shreyas kapale
#github project - 28/9/2017  
import argparse 
import cv2
import sys # it is for exit function
# import cv2 and argparse
p = argparse.ArgumentParser()
# create a argument parser  A and P should be capitol as it is
p.add_argument("-i", "--image", required=True, help="path to the image" )
# define the argument which should be passed
angle=raw_input(" Enter the Angle : ") 
angle = float(angle)
args = vars(p.parse_args())
#set args to parsed argument 

image = cv2.imread(args["image"])
x = image.shape[1]
y = image.shape[0]
center = (x/2,y/2)


matrix = cv2.getRotationMatrix2D(center,angle,0.54)
#get a rotation matrix
rotated = cv2.warpAffine(image, matrix, (x,y))

#rotate the image 
cv2.imshow("Rotated image ", rotated)
cv2.waitKey(4000)

cv2.destroyAllWindows()

#display the rotated image
get = raw_input("Wanna save the image ? (yes/no): ")
if get =="yes":
	format = raw_input("Please name the new file name with its extension ex - new.jpg : ")
	cv2.imwrite(format, rotated)
else:
	sys.exit(0)



