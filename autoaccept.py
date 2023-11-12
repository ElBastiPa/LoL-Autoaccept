import cv2
import pyautogui
import time

while(True):
	accept = pyautogui.locateOnScreen('accept.png', confidence = 0.7)
	if(accept):
		pyautogui.click(accept)
		time.sleep(2)