from tkinter import *

class dialogTI():

	text=""
	eText=None
	emote=""
	eEmote=None
	col=""
	eCol=None
	client=""
	eClient=None

	def __init__(self, callable):
		self.callable = callable
	
		root = Tk()
		root.title("EMOTESS")
		Label(root, text="Text to Emotes !").grid(row=0, columnspan=2)
		
		self.eText = StringVar(root)
		Label(root, text="Text: ").grid(row=1, column=0, sticky=W)
		Entry(root, textvariable=self.eText).grid(row=1, column=1, sticky=W)
		
		self.eEmote = StringVar(root)
		Label(root, text="Emote: ").grid(row=2, column=0, sticky=W)
		Entry(root, textvariable=self.eEmote).grid(row=2, column=1, sticky=W)
		
		self.eCol = StringVar(root)
		Label(root, text="Multiple columns: ").grid(row=3, column=0, sticky=W)
		Spinbox(root, textvariable=self.eCol, from_=1, to=100).grid(row=3, column=1, sticky=W)
		
		clients = ["RocketChat", "Slack"]
		self.eClient = StringVar(root)
		self.eClient.set(clients[0])
		OptionMenu(root, self.eClient, *clients).grid(row=4, columnspan=2)
		
		Button(root, text="Go !", command=self._go).grid(row=5, column=0)
		Button(root, text="Quitter", command=root.quit).grid(row=5, column=1)
		
		root.mainloop()

	def _go(self):
		self.text = self.eText.get()
		self.emote = self.eEmote.get() if self.eEmote.get() != "" else None
		self.col = int(self.eCol.get())
		self.client = self.eClient.get()
		
		self.callable(self)
		
	def getResults(self):
		return self.text, self.emote, self.col, self.client

	
	