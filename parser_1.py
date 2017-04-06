#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET

tree = ET.parse('tester.xml')
root = tree.getroot()

for child in root:
	#print(child.tag, child.attrib)
	for item in child:
		if item.tag == "polygon":
			print("mapList.append(['" + child.attrib["title"] + "'"+ ", [" + item.attrib["points"].replace(","," ").replace(" ",", ").replace(", ,","") + "], '#99FF99'])")
			print("\n")
