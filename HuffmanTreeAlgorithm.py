# coding=utf-8
import Queue
import string
from Tkinter import *
import threading



tkInput = ""


root = Tk()
def quit():
    global root
    root.quit()
def getTkInput():
    global tkInput
    tkInput = text1.get('1.0', END)
    quit()
root.title('tree maker')
text1= Text(root,height=4,width=7,font='Arial 14')
text1.pack(side=TOP, expand=YES, fill=X)


button = Button(root,text='Create Tree',width=25,height=4,bg='yellow',fg='red',font='arial 14',command=getTkInput)
button.pack(side=BOTTOM, expand=YES, fill=X)

root.mainloop()


def LetterCount(str):
    str = str.lower().strip()
    str = str.replace(" ","")
    #str = str.strip(string.punctuation)
    list1 = list(str)
    lcDict = {}
    for l in list1:

            if l in lcDict:
                lcDict[l] += 1
            else:
                lcDict[l] = 1
    return lcDict



class HuffmanNode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root     # Why?  Not needed for anything.

    def children(self):
        return ((self.left, self.right))

tkInput = tkInput.lower()
new_str = tkInput
new_str = tkInput.replace(" ","").replace("\n","").replace(",","").replace(".","").replace("!","").replace("?","").replace(":","").replace("\"","").replace("\'","").replace("`","") #.encode(encoding="UTF-8")
print(new_str)
freqnew  = LetterCount(new_str)
freq = []
for k in freqnew:
    freq.append((round(freqnew[k]*1.0/(len(new_str)-1),5),k))
    print(k+" : "+str(round(freqnew[k]*1.0/(len(new_str)-1),5)))


print(len(freq))
for i in range(len(freq)):
    freq[i] = (freq[i][0], freq[i][1], 0)


def create_tree(frequencies):
    p = Queue.PriorityQueue()
    for value in frequencies:
        p.put(value)             #
    while p.qsize() > 1:         #
        l, r = p.get(), p.get()  #
        if (l[0] >= r[0]):
            l = (l[0], l[1], 1)
        else:
            r = (r[0], r[1], 1)
        node = HuffmanNode(l, r) #
        p.put((l[0] + r[0], node, 0)) #
    return p.get()               #


node = create_tree(freq)



for i in sorted(freq, reverse=True):
    print(i[1], i[0]) #'{:6.2f}'.format(i[0]), code[i[1]])

code = []
freqWithCode = [] #висячие вершины
vertices = {} #словарь вершин с индексами
edges = [] #список ребер c вероятностями
edgesLabels = [] #список ребер с индексами
id = 0


def Obhad(node):
    global id
    if node[1].__class__ == str or node[1].__class__ == unicode:
        code.append(str(node[2]))
        freqWithCode.append((node[0], node[1], ''.join(code))) #добавление вершины с кодом
        vertices[id] = (''.join(code), round(node[0], 3))
        id += 1
        code.pop()
        return
    (left, right) = node[1].children()
    code.append(str(node[2])) #формирование кода символа
    if left:
        edges.append((''.join(code), ''.join(code) + str(left[2]), left[2]))
    if right:
        edges.append((''.join(code), ''.join(code) + str(right[2]), right[2]))
    vertices[id] = (''.join(code), round(node[0], 3))
    id += 1
    Obhad(left)
    Obhad(right)
    code.pop()


Obhad(node)


def getKey(list, searchItem):
    for id, item in list.iteritems():
        if item[0] == searchItem:
            return id


def makeEdgesList(list):
    newList = []
    for i in range(len(list)):
        newList.append((getKey(vertices, list[i][0]), getKey(vertices, list[i][1])))
        edgesLabels.append(str(list[i][2]))
    return newList


edges_new = []

for i in makeEdgesList(edges):
    print i
    edges_new.append(i)

es = []
vs = []
for i in edgesLabels:
    print i
    es.append(i)
for i in vertices:
    print vertices[i][1]
    vs.append(str(round(vertices[i][1], 6)))
for i, obj in enumerate(freqWithCode):
    freqWithCode[i]  = (freqWithCode[i] [0], freqWithCode[i] [1], freqWithCode[i] [2][1:])
    print(freqWithCode[i][0], freqWithCode[i][1], freqWithCode[i][2])
