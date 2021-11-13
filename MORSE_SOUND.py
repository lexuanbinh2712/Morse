#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import winsound


# In[ ]:


frequency = 2000
dot = 200
dash = dot*3
frequency1 = 37
space = 300
frequency2 = 400
slash = 100


# In[ ]:


morse = {'A':'._',
		'B':'...',
		'C':'._.',
		'D':'..',
		'E':'.',
		'F':'...',
		'G':'_.',
		'H':'....',
		'I':'..',
		'J':'.__',
		'K':'.',
		'L':'._..',
		'M':'_',
		'N':'.',
		'O':'_',
		'P':'.__.',
		'Q':'_.',
		'R':'._.',
		'S':'...',
		'T':'',
		'U':'..',
		'V':'..._',
		'W':'.__',
		'X':'..',
		'Y':'._',
		'Z':'__..',' ':'/','1':'.____','2':'..___','3':'...__','4':'...._','5':'.....','6':'_....','7':'__...','8':'___..','9':'____.','0':'_____'}
def xb ():
    print('nhập kí tự: ')
    lst = input()
    lst1=('')
    for x in lst: 
        b = morse[x]
        lst1 += b + " "
    print("Giải Mã Morse: \t",lst1)
    for b in lst1:
        if b == '.': winsound.Beep(frequency,dot)
        elif b == ' ': winsound.Beep(frequency1,space)
        elif b == '/' : winsound.Beep(frequency2,slash)
        else : winsound.Beep(frequency,dash)


# In[ ]:


xb()

