#sipiral effect using opencv
#credits - shreyas kapale
#29/09/2017


import cv2
import argparse

p = argparse.ArgumentParser()
p.add_argument("-i", "--image", required=True, help="link to the image")
args = vars(p.parse_args())
image = cv2.imread(args["image"])

(b, g,r ) = image[0,0]
#get the background colour
print "pixel at is %d %d %d" % (b,g,r)
color = (int(b),int(g),int(r))
# set color var = obtained pixel colour of the background
x = image.shape[1]/2
y = image.shape[0]/2
# get center

for a in xrange(0,175,25):
#loop to create circles with increasing radius
	cv2.circle(image, (x,y), a, color, 2 )
	# here a is raduis
cv2.imshow("image",image)
# show window
cv2.waitKey(0)
