import re
import font
import secrets
from dialogTI import dialogTI

def getEmotes(client):
	if(client == "RocketChat"):
		reg = "title=\"(:.*?:)\""
	else:
		print(client + " not supported !")
		return None;

	with open('emotes.html', 'r') as fhtml:
		html=fhtml.read().replace('\n', '')

	p = re.compile(reg)
	return p.findall(html)

def addLetter(el, letter, emote, one=None):
	letter = ord(letter) - ord(' ')
	l=[]
	for i in range(0,5):
		l.append(font.asciiTable[letter*5+i])
	
	if one == None:
		one = secrets.choice(emote)
	zeros = [e for e in emote if ((e != one) and (len(e)<20))]
	
	for i in range(0,6):
		for j in range(0,8):
			if(i < 5):
				if(((l[i]>>j)&1) == 1):
					el[j] += one
				else:
					el[j] += secrets.choice(zeros)
			else:
				el[j] += " "
	
	return el

def texter(d):
	t, e, maxCol, client = d.getResults()
	s = list(t)

	col = 0
	text = ""
	el=["", "", "", "", "", "", "", ""]
	emote = getEmotes(client)

	for chr in s:
		
		if(col >= maxCol):
			text += '\n'.join(el) + "\n"
			el=["", "", "", "", "", "", "", ""]
			col = 0
			
		el = addLetter(el, chr, emote, e)
		
		col+=1
	
	text += '\n'.join(el) + "\n"

	with open('emotes.txt', 'w') as ftext:
			ftext.write(text)


dialogTI(texter)




