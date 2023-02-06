import xml.etree.ElementTree as ET

# Crearem un root per l'xml
a = ET.Element('students')

# Crearem subelements per el nostre root

a1 = ET.SubElement(a,'student')

aa1 = ET.SubElement(a, "Name")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'Antonio')

aa2 = ET.SubElement(a, "Surname")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'Marcos')

aa3 = ET.SubElement(a, "Email")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'Marcos@gmail.com')

aa4 = ET.SubElement(a, "dni")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , '76364924H')


b2 = ET.SubElement(a,'student')
bb1 = ET.SubElement(b2, "Name")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'Roger')

bb2 = ET.SubElement(b2, "Surname")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'Gonzalez')

bb3 = ET.SubElement(b2, "Email")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'rg@gmail.com')

bb4 = ET.SubElement(b2, "dni")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , '76343554H')

c1 = ET.SubElement(a,'student')
cc1 = ET.SubElement(c1, "Name")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'Victor')

cc2 = ET.SubElement(c1, "Surname")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'Maria')

cc3 = ET.SubElement(c1, "Email")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'v@gmail.com')

cc4 = ET.SubElement(c1, "dni")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , '721444D')

d1 = ET.SubElement(a,'student')
dd1 = ET.SubElement(d1, "Name")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'Albert')

dd2 = ET.SubElement(d1, "Surname")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'Penades')

dd3 = ET.SubElement(d1, "Email")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'a@gmail.com')
dd4 = ET.SubElement(d1, "dni")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , '76364924H')

f1 = ET.SubElement(a, 'student')
ff1 = ET.SubElement(f1, "Name")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'Pau')

ff2 = ET.SubElement(f1, "Surname")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'Insa')

ff3 = ET.SubElement(f1, "Email")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , 'insa@gmail.com')
ff4 = ET.SubElement(f1, "dni")
tree = ET.parse('student.xml')
root = tree.getroot()
element = root[0]
element.set('type' , '72345678A')

tree = ET.ElementTree(a)
tree.write("student.xml")

#Imprimir per pantalla el XML
ET.dump(a)

"""
Seguirem creant les classes que ens demanen
"""