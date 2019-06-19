import pyautogui

pyautogui.PAUSE = 0

def scratch():
	pyautogui.click(550,470)
	for i in range(3):
		pyautogui.dragRel(320, 0, duration=0)
		pyautogui.dragRel(0, 40, duration=0)
		pyautogui.dragRel(-320, 0, duration=0)
		pyautogui.dragRel(0, 40, duration=0)

def new_card():
	pyautogui.click(680,650)
	pyautogui.click(680,680)

for i in range(300):
	scratch()
	new_card()
