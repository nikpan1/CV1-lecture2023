# https://medium.com/programming-fever/how-to-find-hsv-range-of-an-object-for-computer-vision-applications-254a8eb039fc


#finding hsv range of target object(pen)
import cv2
import numpy as np
import time
# A required callback method that goes into the trackbar function.
def nothing(x):
    pass


# Create a window named trackbars.
cv2.namedWindow("Trackbars", cv2.WINDOW_NORMAL)

# Now create 6 trackbars that will control the lower and upper range of 
# H,S and V channels. The Arguments are like this: Name of trackbar, 
# window name, range,callback function. For Hue the range is 0-179 and
# for S,V its 0-255.
cv2.createTrackbar("L - R", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - G", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - B", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - R", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - G", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - B", "Trackbars", 255, 255, nothing)

frame = cv2.imread("data/pyraminx.jpg")
while True:
    # Convert the BGR image to HSV image.
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = frame
    # Get the new values of the trackbar in real time as the user changes 
    # them
    l_h = cv2.getTrackbarPos("L - R", "Trackbars")
    l_s = cv2.getTrackbarPos("L - G", "Trackbars")
    l_v = cv2.getTrackbarPos("L - B", "Trackbars")
    u_h = cv2.getTrackbarPos("U - R", "Trackbars")
    u_s = cv2.getTrackbarPos("U - G", "Trackbars")
    u_v = cv2.getTrackbarPos("U - B", "Trackbars")
 
    # Set the lower and upper HSV range according to the value selected
    # by the trackbar
    lower_range = np.array([l_h, l_s, l_v])
    upper_range = np.array([u_h, u_s, u_v])
    
    # Filter the image and get the binary mask, where white represents 
    # your target color
    mask = cv2.inRange(hsv, lower_range, upper_range)
 
    # You can also visualize the real part of the target color (Optional)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Converting the binary mask to 3 channel image, this is just so 
    # we can stack it with the others
    mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    # stack the mask, orginal frame and the filtered result
    stacked = np.hstack((mask_3,frame,res))
    
    # Show this stacked frame at 40% of the size.
    cv2.imshow('Trackbars',cv2.resize(stacked,None,fx=0.4,fy=0.4))
    
    # If the user presses ESC then exit the program
    key = cv2.waitKey(1)
    if key == 27:
        break
    
    # If the user presses `s` then print this array.
    if key == ord('s'):
        
        thearray = [[l_h,l_s,l_v],[u_h, u_s, u_v]]
        print(thearray)
        
        # Also save this array as penval.npy
        np.save('hsv_value',thearray)
        break
    
# Release the camera & destroy the windows.    
cv2.destroyAllWindows()
