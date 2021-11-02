#!/usr/bin/env python
# coding: utf-8

# In[43]:


import winsound


# In[50]:


frequency = 2000
dot = 200
dash = dot*3
frequency1 = 500
space = 300


# In[53]:


MORSE_CODE = {'A':'._','B':'...','C':'._.','D':'..','E':'.','F':'...','G':'_.','H':'....','I':'..','J':'.__','K':'.','L':'._..','M':'_','N':'.','O':'_','P':'.__.','Q':'_.','R':'._.','S':'...','T':'','U':'..','V':'..._','W':'.__','X':'..','Y':'._','Z':'__..',' ':'/'}
def xb ():
    print('nhập kí tự: ')
    lst = input()
    lst1=('')
    for x in lst: 
        b = MORSE_CODE[x]
        lst1 += b + " "
    print("Giải Mã Morse: \t",lst1)
    for b in lst1:
        if b == '.': winsound.Beep(frequency,dot)
        elif b == ' ': winsound.Beep(frequency1,space)
        else : winsound.Beep(frequency,dash)


# In[54]:


xb()


# In[ ]:




