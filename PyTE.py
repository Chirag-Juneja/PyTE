from tkinter import *
import os

class Window:
    
	_root=Tk()
	_thisWidth = 600
	_thisHeight = 480
	_thisMenu = Menu(_root)
	_thisFileMenu = Menu(_thisMenu,tearoff=0)
	_thisEditMenu =  Menu(_thisMenu,tearoff=0)
	_thisAboutMenu = Menu(_thisMenu,tearoff=0)
	_thisText = Text(_root)
	_thisScrollBar = Scrollbar(_thisText)


	def __init__(self):
		#set window title
		self._root.title("PyTE")
		
        #set window position to center of the screen
		screenWigth = self._root.winfo_screenwidth()
		screenHeight = self._root.winfo_screenheight()
		xpos=(screenWigth / 2) - (self._thisWidth / 2)
		ypos=(screenHeight / 2) - (self._thisHeight / 2)
		self._root.geometry('%dx%d+%d+%d' %(self._thisWidth,self._thisHeight,xpos,ypos))
		self._root.grid_rowconfigure(0,weight=1)
		self._root.grid_columnconfigure(0,weight=1)
		self._thisText.grid(sticky=N+E+S+W)

        #create file menu
		self._thisFileMenu.add_command(label="New",command=self._new_file)
		self._thisFileMenu.add_command(label="Open",command=self._open_file)
		self._thisFileMenu.add_command(label="Save",command=self._save_file)
		self._thisFileMenu.add_command(label="Exit",command=self._exit)
		
        #create edit menu
		self._thisEditMenu.add_command(label="Copy",command=self._copy)
		self._thisEditMenu.add_command(label="Cut",command=self._cut)
		self._thisEditMenu.add_command(label="Paste",command=self._paste)
		
        #create about menu
		self._thisAboutMenu.add_command(label="About",command=self._about)
		
        #add main menu options
		self._thisMenu.add_cascade(label="File",menu=self._thisFileMenu)
		self._thisMenu.add_cascade(label="Edit",menu=self._thisEditMenu)
		self._thisMenu.add_cascade(label="About",menu=self._thisAboutMenu)
		
        #add main menu to the window
		self._root.config(menu=self._thisMenu)
		self._thisScrollBar.pack(side=RIGHT,fill=Y)
		self._thisScrollBar.config(command=self._thisText.yview)
		self._thisText.config(yscrollcommand=self._thisScrollBar.set)

	# file menu commands

	def _new_file(self):
			pass
	
	def _open_file(self):
       		pass

	def _save_file(self):
    		pass

	def _exit(self):
    		self._root.destroy()

	#edit menu commands

	def _copy(self):
			pass

	def _cut(self):
			pass

	def _paste(self):
    		pass

	#about menu commands
    
	def _about(self):
    		pass

	def run(self):
		self._root.mainloop()
    		
def main():
	PyTE = Window()
	PyTE.run()

if __name__ == '__main__':
	main()