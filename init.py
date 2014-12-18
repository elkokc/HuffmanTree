# coding=utf-8
from Tkinter import *
from igraph import *
import huffman

g = Graph()

g.add_vertices(len(huffman.vertices))
#g.add_edges([(0,1),(0,2),(2,3),(2,4),(4,5),(4,6)])
#g.add_edges([(0, 1),(0, 4),(1, 2),(1, 3),(4, 5),(4, 12),(5, 6),(5, 7),(7, 8),(7, 11),(8, 9),(8, 10),(12, 13),(12, 14)])


g.add_edges(huffman.edges_new)
g.vs['label'] = huffman.vs
g.es['label'] = huffman.es
g.vs[2] = "1"


plot(g,"Englis3.png",layout = g.layout_reingold_tilford(root=0),vertex_label_angle=140 ,vertex_label_dist = 1,color="green",vertex_color="blue",bbox = (2000, 2000), margin = 20)


root = Tk()

def getDic(freqDic):
    newDict = {}
    for i in freqDic:
        newDict[i[1]] = i[2]
    return newDict
def getCode(inputString,freqDic):
    code=""
    for i in inputString:

        if freqDic.get(i)!=None:
            code+=freqDic[i]
    return code

def makeText(freqDic):
    text = ""
    for i in freqDic:
        if i.__class__() == ():
          text+=str(i[1].encode('utf-8'))+":"+str(i[0])+" - "+str(i[2])
          text+="\n"
    return text

root.title(u'Словарь')
root.geometry('200x400+400+225')
text1= Text(root,height=4,width=7,font='Arial 14')
text1.insert(0.0,makeText(huffman.freqWithCode))
code = getCode(huffman.tkInput,getDic(huffman.freqWithCode))
text1.insert(END,"Длина исходного сообщения: "+str(len(huffman.tkInput)-1)+" байт \n")
text1.insert(END,"Длинна закодированного сообщениия : "+str(len(code)/8)+" байт \n")
text1.insert(END,"Коэффицент сжатия : "+str((len(huffman.tkInput)-1)/(((len(code)/8)*1.0))))
text1.insert(END,"\nЗакодированное сообщение:\n"+code)
text1.pack(side=TOP,fill=BOTH,expand=YES)

root.mainloop()
