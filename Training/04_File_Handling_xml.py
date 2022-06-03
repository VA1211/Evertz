# import xml.etree.ElementTree as ET       #ET is an alias
#
# #parsing an xml file
# mytree = ET.parse("employee.xml")
# myroot = mytree.getroot()               #getting root element of xml file
# print(myroot)
# print(myroot.tag)                       #returns tag
# print(myroot[0].tag)                    #returns first child element
# print(myroot[0].attrib)                 #returns dictionary with attributes
#
# for x in myroot[0]:
#     print(x.tag,x.attrib)
#
# for x in myroot[0]:
#     print(x.text)

# for x in myroot.findall('row'):
#     id = x.find('id').text
#     name = x.find('name').text
#     print(id,name)


#parsing a xmlstring
# data = '''<?xml version="1.0" encoding="UTF-8" ?>
# <root>
#   <row>
#     <id>4051</id>
#     <name>manoj</name>
#     <email>manoj@gmail.com</email>
#     <password>Test@123</password>
#   </row>
# </root>'''
# myroot = ET.fromstring(data)
# print(myroot.tag)
#

#creating xml file
import xml.etree.ElementTree as ET
root = ET.Element('Company')
root.tag = 'Employee'
root.attrib = {}

child = ET.Element("Employee1")

root.append(child)

name = ET.SubElement(child,'name')
name.text = 'vidhi'
id = ET.SubElement(child,'id')
id.text = '102'

tree= ET.ElementTree(root)

with open('new1xml.xml','wb') as new:
    tree.write(new)


# import xml.etree.ElementTree as et
# root=et.Element('data')
# child=et.Element('sdata')
# root.append(child)
#
# ids=et.SubElement(child,'id')
# ids.text='2001'
#
# names=et.SubElement(child,'name')
# names.text='parag'
#
# tree=et.ElementTree(root)
# with open("newxml.xml",'wb') as d:
#     tree.write(d)
