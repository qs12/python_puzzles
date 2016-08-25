#! /usr/bin/python
# mcb.pyw - Saves and loads pieces of text to the clipboard
#Usage : python mcb.pyw save <keyword> - Saves clipboad to keyword
#        python mcd.pyw <keyword> - Loads keyword to clipboard
#        python mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcdShelf = shelve.open('mcd.txt')

# Save clipboard content

if len(sys.argv)==3 and sys.argv[1].lower()=='save':
	mcdShelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
	#List keywords and load content.
	if sys.argv[1].lower()=='list':
		pyperclip.copy(str(list(mcdShelf.keys())))
	elif sys.argv[1] in mcdShelf:
		pyperclip.copy(mcdShelf[sys.argv[1]])

mcdShelf.close()
