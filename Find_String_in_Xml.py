#！/bin/bash/python3
#coding=utf-8
#给定链接，寻找其中的xml文件，并搜索字符串，并递归搜索子目录下的xml文件
import  xml.dom.minidom
import urllib
#打开xml文档
dom = xml.dom.minidom.parse('DiscoveryTree.xml')

#得到文档元素对象
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)
Chilid_Element_List1=[]   #子结点列表
Chilid_Element_List2=[]   #子结点列表
Chilid_Element_List=[]   #子结点列表
Chilid_Element_List1 = root.getElementsByTagName("ledm:SupportedTree") 
Chilid_Element_List2 = root.getElementsByTagName("ledm:SupportedIfc") 
Chilid_Element_List=Chilid_Element_List1+Chilid_Element_List2
collection_List=[]
for child in Chilid_Element_List:
     collection_List.append("http://15.96.136.163" + child.childNodes[0].childNodes[0].nodeValue)

def FindKeyValue(s,data):
    return data.find(s)

#keyvalue1='Duplex'
#keyvalue2='duplex'
keyvalue1='Two-sided'
keyvalue2='two-Sided'

Xml_List_Context=[]#xml列表中内容
for xml_list in collection_List:
    try:
        resu = urllib.request.urlopen(xml_list, data=None, timeout=3)
        data=resu.read().decode()
        index1 = FindKeyValue(keyvalue1,data)
        index2 = FindKeyValue(keyvalue2,data)
        index= (index1 if (index1>index2) else index2)
    except:
        fo = open("解析出错的xml列表.txt",'a+',encoding = 'utf-8') # 打开文件 这里网络数据流的编码需要和写入的文件编码一致
        fo.write(xml_list+"解析出错\n")   # 写入文件
        fo.close()       # 关闭文件
        continue
    #打开文件
    #print(type(xml_list))
    if(index>-1):
        fo = open(xml_list.split('/')[-1]+"关键字index"+str(index),'a+',encoding = 'utf-8') # 打开文件 这里网络数据流的编码需要和写入的文件编码一致
        fo.write(data)   # 写入文件
        fo.close()       # 关闭文件
    Xml_List_Context.append(data)
print("hello")