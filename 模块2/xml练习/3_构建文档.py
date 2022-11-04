from xml.etree import ElementTree

# 创建节点
home = ElementTree.Element('home')
son_1 = ElementTree.Element('son1', {'son': '1'})
son_2 = ElementTree.Element('son2', {'son': '2'})
inner_1 = ElementTree.Element('inner1', {'inner': '1'})
inner_2 = ElementTree.Element('inner2', {'inner': '2'})
# 添加的内部
son_1.append(inner_1)
son_2.append(inner_2)
home.append(son_1)
home.append(son_2)
# 写入文件
tree = ElementTree.ElementTree(home)
# tree.write('home.xml', encoding='utf-8')  # 短标签
tree.write('home_new.xml', encoding='utf-8', short_empty_elements=False)

