# from xml.dom.minidom import parse
# import xml.dom.minidom
# # Tree = xml.dom.minidom.parse('employee.xml')
# # collection = Tree.
# import xml.dom.minidom
# doc = xml.dom.minidom.parse('employee.xml')
# print(doc.firstChild.tagName)
# print(doc.firstChild)
# emails = doc.getElementsByTagName("email")
# print(emails)

import xml.dom.minidom as parser
data = parser.parse('employee.xml')
print(data.nodeName)
print(data.parentNode)
print(data.firstChild.tagName)
element = data.firstChild
print(element.tagName)
print(element.getElementsByTagName('id'))