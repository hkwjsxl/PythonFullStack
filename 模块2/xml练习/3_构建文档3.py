from xml.etree import ElementTree

# 创建节点
home = ElementTree.Element('home')
son_1 = ElementTree.SubElement(home, 'son1', {'son': '1'})
son_2 = ElementTree.SubElement(home, 'son2', {'son': '2'})
inner_1 = ElementTree.SubElement(son_1, 'inner1', {'inner': '1'})
inner_2 = ElementTree.SubElement(son_2, 'inner2', {'inner': '2'})
inner_1.text = 'inner_1'
# 写入文件
tree = ElementTree.ElementTree(home)
# tree.write('home.xml', encoding='utf-8')  # 短标签
tree.write('home_new_2.xml', encoding='utf-8', short_empty_elements=False)
