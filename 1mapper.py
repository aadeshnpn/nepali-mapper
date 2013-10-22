#!/usr/bin/python2.7
# coding: utf8
"""
@author:Aadesh Neupane
Simple Rules to Map Nepali characters for Speech Processing
"""
"""
Uses: Choose a Nepali Word List as the input from the dialog.
Results: The result after mapping is written to out1.txt
How To Run: ./1mapper.py in Terminal or python 1mapper.py in cmd
Requirements: Tkinter
"""
#Maps the argumets to the set of rules defined and return the mapped word 

from Tkinter import *
from tkFileDialog import askopenfilename
"""def map():
    dict=rules()
    a=open("wordlist.txt","r")
    b=open("out1.txt","w")
    text=a.readlines()
    aa=text[19]
    i=0
    print len(aa)
    b.write(aa+"\t")
    while i <len(aa):
        #print aa[i:i+3]
        chars=aa[i:i+3]
        if chars in dict:
            ab=dict[chars]
            print ab,
            b.write(ab)
        i=i+3
"""
def map(filename):
    dict1=rulessingle()
    a=open(filename,"r")
    b=open("out1.txt","w")
    text=a.readlines()
    ab=''
    #aa=text[19]
    #print "Testing"
    for aa in text:
        aaa=aa.strip("\t\n\r")
        b.write(aaa+'\t\t')
        i=0
        #print len(aa)
        while i <len(aa):
            #print aa[i:i+3]
            chars=aa[i:i+3]
            if chars in dict1:
                ab=dict1[chars]
                #print chars
                if aa[i+3:i+6]=="ँ":
                    ab=ab
                    aC=ab.rstrip()
                    #print aC+'N'
                    b.write(aC+'N ')
                #print ab,
                else:
                    b.write(ab)
            i=i+3
        b.write("\n")    
            #mapExtra("out1.txt")
#Modified Mapping to adjust        
#def modifiedMap(filename):
def mapExtra():
	dict1=rulescomp()
	a=open("out1.txt","r")
	b=open("out12.txt","w")
	text=a.readlines()
	#print dict1
	for aa in text:
		#print aa
		for d in dict1:
			#print d
			if d in aa:
				ab=aa.find(d)
				a1=list(aa)
				#print aa,ab,len(d)
				a1[ab:ab+len(d)]=dict1[d]
				a2=''.join(a1)
				aa=a2
				#print ab,
		b.write(aa)
#Contains the set of rules for mapping
def rulessingle():
    dict1={"ष":"S AH ","श":"S AH ","स":"S AH ","व":"W AH ","ल":"L AH ","र":"R AH ","य":"Y AH ","म":"M AH ","भ":"BA AH ",
    "ब":"B AH ","फ":"PA AH ","प":"P AH ","न":"N AH ","ध":"DHA AH ","द":"DH AH ","थ":"THA AH ","त":"TH AH ","ण":"N AH ",
    "ढ":"DA AH ","ड":"D AH ","ठ":"TA AH ","ट":"T AH ","ञ":"N AH ","झ":"JHA AH ","ज":"JH AH ","छ":"CHA AH ","च":"CH AH ",
    "ङ":"NG AH ","घ":"GA AH ","ग":"G AH ","ख":"KA AH ","क":"K AH ","औ":"AH UN ","ओ":'OH ',"ऐ":"AH IH ","ए":'EH ',"ऋ":"R IH ",
    "ऊ":'UH ',"उ":'UH ',"ई":'IH ',"इ":'IH ',"आ":'AA ',"अ":'AH ',"ौ":"AH UH ","ो":'OH ',"ै":"AH IH ","े":'EH ',"ू":'UH ',
    "ु":'UH ',"ी":'IH ',"ि":'IH ',"ा":'AA ',"ं":"M","ँ":"","ह":"HH AH ","्":" ","ृ":"R "}
    #print dict["ं"]
    #print dict["ष"]
    return dict1

def rulescomp():
    dict1={"UH IH":"UY","IH UH":"IW","EH IH":"EY","EH UH":"EW","OHIH":"OY","OH UH":"OW","AAIH":"AY","AAUH":"AW","AH AA":"AA ","AH IH":"IH ","AH UH":"UH ","AH OH":"OH ","AH EH":"EH " } 
    return dict1
#Main Fuction that takes the file name as the argument and processes the input file to give the results
def main():
    #top=Tkinter.Tk()
    #top.mainloop()
    #rules()
    #map()
    #print dict["ह"]
    #pass
    root=Tk()	
    filename = askopenfilename(filetypes=[("allfiles","*"),("pythonfiles","*.py")])
    map(filename)
    mapExtra()

if __name__=='__main__':
    main()
