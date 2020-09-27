import pyautogui
import time

class TabOpt:
	def __init__(self):
		pass

	def switchTab(self):
		pyautogui.hotkey('ctrl','tab')

	def closeTab(self):
		pyautogui.hotkey('ctrl','w')

	def newTab(self):
		pyautogui.hotkey('ctrl','n')


class WindowOpt:
	def __init__(self):
		pass

	def openWindow(self):
		self.maximizeWindow()
	
	def closeWindow(self):
		pyautogui.hotkey('alt','F4')
	
	def minimizeWindow(self):
		pyautogui.hotkey('win','down')
		time.sleep(0.05)
		pyautogui.hotkey('win','down')
	
	def maximizeWindow(self):
		pyautogui.hotkey('win', 'up')

	def moveWindow(self, operation):
		if "left" in operation: pyautogui.hotkey('win','left')
		elif "right" in operation: pyautogui.hotkey('win','right')
		elif "down" in operation: pyautogui.hotkey('win','right')
		elif "up" in operation: pyautogui.hotkey('win','up')

	def switchWindow(self):
		pyautogui.hotkey('alt','tab')

	def takeScreenShot(self):
		pyautogui.screenshot('ss.png')

def isContain(text, lst):
	for word in lst:
		if word in text:
			return True
	return False

def Win_Opt(operation):
	w = WindowOpt()
	if isContain(operation, ['open']):
		w.openWindow()
	elif isContain(operation, ['close']):
		w.closeWindow()
	elif isContain(operation, ['mini']):
		w.minimizeWindow()
	elif isContain(operation, ['maxi']):
		w.maximizeWindow()
	elif isContain(operation, ['move', 'slide']):
		w.moveWindow(operation)
	elif isContain(operation, ['switch','which']):
		w.switchWindow()
	elif isContain(operation, ['screenshot','capture','snapshot']):
		w.takeScreenShot()
	return

def Tab_Opt(operation):
	t = TabOpt()
	if isContain(operation, ['new','open','another','create']):
		t.newTab()
	elif isContain(operation, ['switch','move','another','next','previous','which']):
		t.switchTab()
	elif isContain(operation, ['close','delete']):
		t.closeTab()
	else:
		return
















# screen_x, screen_y = pyautogui.size()
# print(screen_x, screen_y)

# cursor_x, cursor_y = pyautogui.position()
# print(cursor_x, cursor_y)

# pyautogui.moveTo(29,44)
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
# pyautogui.click()
# pyautogui.click(13,41)
# pyautogui.doubleClick()

# pyautogui.write('Hello World', interval=0.5)
# pyautogui.press('win')
# pyautogui.keyDown('shift')
# pyautogui.keyUp('shift')
# pyautogui.write(['left', 'left', 'left'])
# pyautogui.hotkey('ctrl','v')

# pyautogui.alert('This is an alert box.')
# pyautogui.confirm('Shall I proceed?')
# pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
# pyautogui.prompt('What is your name?')
# pyautogui.password('Enter password (text will be hidden)')

# pyautogui.screenshot('my_screenshot.png')

"""
    >>> import pyautogui
    >>> button7location = pyautogui.locateOnScreen('button.png') # returns (left, top, width, height) of matching region
    >>> button7location
    (1416, 562, 50, 41)
    >>> buttonx, buttony = pyautogui.center(button7location)
    >>> buttonx, buttony
    (1441, 582)
    >>> pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
"""

"""
	>>> import pyautogui
    >>> buttonx, buttony = pyautogui.locateCenterOnScreen('button.png') # returns (x, y) of matching region
    >>> buttonx, buttony
    (1441, 582)
    >>> pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
"""