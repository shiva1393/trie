import string
import fileinput
import os, sys, string
import re
d={} #for mapping
num_lines = sum(1 for line in open('letters.txt'))
#print(num_lines)
f=open("letters.txt","r")
syl=f.read()
f.close()
s4=syl.replace("\n"," ")
s3=s4.rstrip(" ")
#print(s3)
#print(s3)

num=0
for i in s3.split(" "):
    d[i]=num
    num=num+1

class node:
    count=0
    def __init__(self):
        self.children=[0]*num_lines
        self.val=None
    def increment(self):                   
        self.count=self.count+1
    def showcount(self):
        return(self.count)
    def reverse_string(self,word):
        word1=word+","
        word1=word1.replace(',',',:').split(':')
        word = "".join(reversed(word1)).rstrip(',')
        return(word)

class node1:
    count=0
    def __init__(self):
        self.children=[0]*num_lines
        self.val=None
    def increment(self):                 
        self.count=self.count+1
    def showcount(self):
        return(self.count)
    def reverse_string(self,word):
        word1=word+","
        word1=word1.replace(',',',:').split(':')
        word = "".join(reversed(word1)).rstrip(',')
        return(word)



class trie:
    def __init__(self):
        self.root=node()
        self.root1=node1()
    def insert(self,word1):
        forward=word1
        word=self.root.reverse_string(word1)
        t=self.root
        TB=self.root1
        #print forward
        #print word
        forward_counts = []
        backward_counts = []
        for i,j in zip(word.split(","),forward.split(",")):
            try:
                if t.children[d[i]]!=0:
                        #print('BT')
                        t=t.children[d[i]]
                        t.increment()
                        #print(t.showcount())
                        #print(i)
                        backward_counts.append(str(i))
                        backward_counts.append(str(t.showcount()))

                else:
                        t.children[d[i]]=node()
                        t.children[d[i]].val=i
                        t=t.children[d[i]]
                        t.increment()
                        #print(t.showcount())
                        backward_counts.append(str(i))
                        backward_counts.append(str(t.showcount()))
                        #print(i)
                if TB.children[d[j]]!=0:
                        #print('TB')
                        TB=TB.children[d[j]]
                        TB.increment()
                        #print(TB.showcount())
                        #print(j)
                        forward_counts.append(str(j))
                        forward_counts.append(str(TB.showcount()))
                else:
                        TB.children[d[j]]=node()
                        TB.children[d[j]].val=j
                        TB=TB.children[d[j]]
                        TB.increment()
                        forward_counts.append(str(j))
                        forward_counts.append(str(TB.showcount()))
                        #print(TB.showcount())
                        #print(j)
            except KeyError, e:
                        #print(str(e))
                        print(word1)
        print("TOP DOWN TRIE WITH COUNTS : ",forward_counts)
        print("DOWN TO TOP TRIE WITH COUNTS : ",backward_counts)


Trie=trie()
fil=open('test')
data=fil.read()
fil.close()
s1=data.replace("\n"," ")

s=s1.rstrip(" ")

for i in s.split(" "):
       Trie.insert(i)


