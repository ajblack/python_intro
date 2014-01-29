import Tkinter
import sys
import urllib
from PIL import Image
import subprocess

class paradigms(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()
		self.entryVariable1 = Tkinter.StringVar()
		self.entryVariable2 = Tkinter.StringVar()
		self.entryVariable3 = Tkinter.StringVar()
		self.entryVariable4 = Tkinter.StringVar()


		self.entry1 = Tkinter.Entry(self,textvariable = self.entryVariable1)
		self.entry2 = Tkinter.Entry(self,textvariable = self.entryVariable2)
		self.entry3 = Tkinter.Entry(self,textvariable = self.entryVariable3)
		self.entry4 = Tkinter.Entry(self,textvariable = self.entryVariable4)

		self.entry1.grid(column=0,row=0)
		self.entry2.grid(column=0,row=1)
		self.entry3.grid(column=0,row=2)
		self.entry4.grid(column=0,row=3)

		self.entryVariable1.set(u"enter first num here")
		self.entryVariable2.set(u"enter second num here")
		self.entryVariable3.set(u"enter third num here")
		self.entryVariable4.set(u"enter fourth num here")



		button = Tkinter.Button(self,text=u"perform addition",command=self.button_press)
		button.grid(column=1,row=0)
		self.labelVariable = Tkinter.StringVar()
		label = Tkinter.Label(self,textvariable=self.labelVariable,anchor="w")
		label.grid(column=2,row=2,columnspan=2)

		

	def button_press(self):
		self.labelVariable.set(int(self.entryVariable1.get())+int(self.entryVariable2.get())+int(self.entryVariable3.get())+int(self.entryVariable4.get()))


		
if __name__ == "__main__":
	app = paradigms(None)
	app.title('simple python app')
	app.mainloop()
