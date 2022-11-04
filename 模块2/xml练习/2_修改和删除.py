from xml.etree import ElementTree

# 修改
# tree = ElementTree.parse('my.xml')
# year = tree.find('country').find('year')
# year.text = '2022'  # 更改值
# year.set('update', '2022-10-12')  # 添加属性键值对，有就修改
# print(year.text, year.attrib)
# tree.write('my_new.xml', encoding='utf-8')

# 删除
tree = ElementTree.parse('my_new.xml')
# country = tree.find('country')
# country.remove(country.find('year'))
data = tree.getroot()
print(data.tag)
data.remove(data.find('country'))
tree.write('my_new.xml', encoding='utf-8')






