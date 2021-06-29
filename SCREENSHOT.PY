#importing PIL mdule for saving image file format5
#ImageGrab module can be used to copy the contents of the screen or the clipboard to a PIL image memory
from PIL import Image,ImageGrab
#importing time module  for taking screenshot in 
import time
#function for defining screenshot
def takescreenshot():

  image=ImageGrab.grab()
  image.show()
  
if __name__=="__main__":
  # in how much time user want to take screenshot..
  time.sleep(int(input('enter time in sec to take screenshot-->')))
  takescreenshot()  
