# from xml.dom import minidom
# xmldoc = minidom.parse("output.xml")
# schools = xmldoc.getElementsByTagName("schools")[0]
# school = schools.getElementsByTagName("school")
# name = school.getElementsByTagName("name").firstChild.data
# print(name)

import os
from xml.etree import ElementTree
file_name = 'output.xml'

dom = ElementTree.parse(file_name)

schools = dom.findall('school')
count = 0

for s in schools:
	name = s.find('name').text
	gradeRange = s.find('gradeRange').text
	lats = s.find('lat').text
	lons = s.find('lon').text

	print(' * {} grades {} [{}] , [{}] '.format(name, gradeRange, lats, lons))
	count+=1
print(count)