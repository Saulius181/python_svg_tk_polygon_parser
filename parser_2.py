#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET

tree = ET.parse('tester2.xml')
root = tree.getroot()

count = 1
for child in root:
#	print(child.tag, child.attrib)
#	for item in child:
	if child.tag == "polygon":
		test = "mapList.append(['" + "Test" + "'"+ ", [" + child.attrib["points"].replace(","," ").replace(" ",", ").replace(", ,","") + "], '#99FF99'])"
		test = test.replace("[, ","[")
		print( test)
		count+=1
		print("\n")
