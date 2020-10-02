from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import os
from os.path import isfile, join
from threading import Thread
from userHandler import UserData
import FACE_UNLOCKER as FU

background, textColor = 'white', 'black'
face_classifier = cv2.CascadeClassifier('Cascade/haarcascade_frontalface_default.xml')

if os.path.exists('userData')==False:
	os.mkdir('userData')
if os.path.exists('userData/faceData')==False:
	os.mkdir('userData/faceData')


###### ROOT1 ########
def startLogin():		
	try:
		result = FU.startDetecting()
		if result:
			user = UserData()
			user.extractData()
			userName = user.getName().split()[0]
			welcLbl['text'] = 'Hi '+userName+',\nWelcome to the world of\nScience & Technology'
			Lbl['text'] = 'Hi '+userName+',\nWelcome to the world of\nScience & Technology'
			loginStatus['text'] = 'UNLOCKED'
			loginStatus['fg'] = 'green'
			faceStatus['text']='(Logged In)'
			raise_frame(root3)
		else:
			print('Error Occurred')

	except Exception as e:
		print(e)

####### ROOT2 ########
def trainFace():
	data_path = 'userData/faceData/'
	onlyfiles = [f for f in os.listdir(data_path) if isfile(join(data_path, f))]

	Training_data = []
	Labels = []

	for i, files in enumerate(onlyfiles):
		image_path = data_path + onlyfiles[i]
		images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
		
		Training_data.append(np.asarray(images, dtype=np.uint8))
		Labels.append(i)


	Labels = np.asarray(Labels, dtype=np.int32)

	model = cv2.face.LBPHFaceRecognizer_create()
	model.train(np.asarray(Training_data), np.asarray(Labels))

	print('Model Trained Successfully !!!')
	model.save('userData/trainer.yml')
	print('Model Saved !!!')

def face_extractor(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(gray, 1.3, 5)

	if faces is():
		return None

	for (x, y, w, h) in faces:
		cropped_face = img[y:y+h, x:x+w]

	return cropped_face

cap = cv2.VideoCapture(0)
count = 0
def startCapturing():
	global count
	ret, frame = cap.read()
	if face_extractor(frame) is not None:
		count += 1
		face = cv2.resize(face_extractor(frame), (200, 200))
		face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

		file_name_path = 'userData/faceData/img' + str(count) + '.png'
		cv2.imwrite(file_name_path, face)
		print(count)
		progressLbl['text'] = 'Progress ' + str(count) + '%'

		cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
	else:
		progressLbl['text'] = 'Face Not Clear'
	
	if count==100:
		lmain['image'] = defaultImg2
		statusLbl['text'] = '(Face added successfully)'
		cap.release()
		cv2.destroyAllWindows()
		trainFace()
		return
	
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	frame = cv2.flip(frame, 1)
	img = Image.fromarray(frame)
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, startCapturing)

def Add_Face():
	user = nameField.get()
	gender = r.get()
	if user is not '' and gender!=0:
		startCapturing()
		statusLbl['text'] = ''
		gen = 'Male'
		if gender==2: gen = 'Female'
		u = UserData()
		u.updateData(user, gen)
	else:
		statusLbl['text'] = '(Please fill the details)'



def raise_frame(frame):
	frame.tkraise()

if __name__ == '__main__':

	root = Tk()
	root.title('ASSISTANT')
	root.geometry('350x600')
	root.configure(bg=background)

	root1 = Frame(root, bg=background)
	root2 = Frame(root, bg=background)
	root3 = Frame(root, bg=background)

	for f in (root1, root2, root3):
		f.grid(row=0, column=0, sticky='news')	
	
	################################
	########  MAIN SCREEN  #########
	################################

	image1 = Image.open('images/menu.jpg')
	defaultImg1 = ImageTk.PhotoImage(image1)

	dataFrame1 = Frame(root1, bd=10, bg=background)
	dataFrame1.pack()
	logo = Label(dataFrame1, width=300, height=250, image=defaultImg1)
	logo.pack(padx=10, pady=10)

	#welcome label
	welcLbl = Label(root1, text='Hi there,\nWelcome to the world of\nScience & Technology', font=('Arial', 15), fg=textColor, bg=background)
	welcLbl.pack(padx=10, pady=20)


	#add face
	loginStatus = Label(root1, text='LOCKED', font=('Arial Bold', 15), bg=background, fg='red')
	loginStatus.pack(pady=(50,0))	

	if os.path.exists('userData/trainer.yml')==False:
		loginStatus['text'] = 'Your Face is not registered'
		addFace = Button(root1, text='Add Face', font=('Arial', 12), bg='blue', fg='white', command=lambda:raise_frame(root2))
		addFace.pack(ipadx=10)
	else:
		Thread(target=startLogin).start()
	
	#status of add face
	faceStatus = Label(root1, text='(Face Not Detected)', font=('Arial 10'), fg=textColor, bg=background)
	faceStatus.pack(pady=5)

	##################################
	########  FACE ADD SCREEN  #######
	##################################

	image2 = Image.open('images/defaultFace2.jpg')
	defaultImg2 = ImageTk.PhotoImage(image2)

	dataFrame2 = Frame(root2, bd=10, bg=background)
	dataFrame2.pack(fill=X)
	lmain = Label(dataFrame2, width=300, height=250, image=defaultImg2)
	lmain.pack(padx=10, pady=10)

	#Details
	detailFrame2 = Frame(root2, bd=10, bg=background)
	detailFrame2.pack(fill=X)
	userFrame2 = Frame(detailFrame2, bd=10, width=300, height=250, relief=FLAT, bg=background)
	userFrame2.pack(padx=10, pady=10)

	#progress
	progressLbl = Label(dataFrame2, text='', font=('Arial Bold', 10), bg=background, fg=textColor)
	progressLbl.place(x=120, y=265)

	#name
	nameLbl = Label(userFrame2, text='Name', font=('Arial Bold', 12), fg=textColor, bg=background)
	nameLbl.place(x=10,y=10)
	nameField = Entry(userFrame2, bd=5, font=('Arial 10'), width=25)
	nameField.focus()
	nameField.place(x=80,y=10)

	genLbl = Label(userFrame2, text='Gender', font=('Arial Bold', 12), fg=textColor, bg=background)
	genLbl.place(x=10,y=50)
	r = IntVar()
	genMale = Radiobutton(userFrame2, text='Male' ,font=('Arial 10'), value=1, bg=background, fg=textColor, variable=r)
	genMale.place(x=80,y=50)
	genFemale = Radiobutton(userFrame2, text='Female' ,font=('Arial 10'), value=2, bg=background, fg=textColor, variable=r)
	genFemale.place(x=180,y=50)

	#agreement
	agree = Checkbutton(userFrame2, text='I agree to use my face for Security purpose', fg=textColor, bg=background)
	agree.place(x=30, y=100)

	#add face
	addBtn = Button(userFrame2, text='Add Face', font=('Arial Bold', 12), bg='green', fg='white', command=Add_Face)
	addBtn.place(x=100, y=150)

	#status of add face
	statusLbl = Label(userFrame2, text='', font=('Arial 10'), fg=textColor, bg=background)
	statusLbl.place(x=60, y=190)

	###########################
	####### CHAT SCREEN #######
	###########################
	
	image3 = Image.open('images/back.jpg')
	defaultImg3 = ImageTk.PhotoImage(image3)

	dataFrame3 = Frame(root3, bd=10, bg=background)
	dataFrame3.pack()
	img = Label(dataFrame3, width=300, height=250, image=defaultImg3)
	img.pack(padx=10, pady=10)

	#welcome label
	Lbl = Label(root3, text="Hi, I'm your personal assistant", font=('Arial', 15), fg=textColor, bg=background)
	Lbl.pack(padx=10, pady=20)
	

	raise_frame(root1)
	root.mainloop()

