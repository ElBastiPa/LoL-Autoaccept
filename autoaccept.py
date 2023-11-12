import cv2
import pyautogui
import time

while(True):
	aceptar = pyautogui.locateOnScreen('accept.png', confidence = 0.7)
	accept = pyautogui.locateOnScreen('acceptEN.png', confidence = 0.7)
	if(accept):
		pyautogui.click(accept)
		time.sleep(2)
	if(aceptar):
		pyautogui.click(aceptar)
		time.sleep(2)