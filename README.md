# Gesture-Mouse
A mouse which works by tracking a blue object in camera view.

# INTRO
just another quick and dirty project made over a weekend. Uses opencv library to find blue objects in the camera view to track it's movements and move the mouse accordingly. You might be thinking... why blue? I used blue because it was the only colour to be detected with least amount of background noise.
I didn't use any object detectors because they slow things down and couldn't provide satisfactory results I wanted.
intead I just drew a contour around the blue object and found its center to move the mouse.

# How to use

to start open the script and place a blue object you want to track in front of camera and run the script. Now try moving the object and see the mouse move accordingly. To click just keep the pointer steady at same place and it will do a click action. If you want to see the contour of the object just uncomment the lines in script. 
To exit you will need to move to the terminal from which you are running the script and press ctrl+c.
