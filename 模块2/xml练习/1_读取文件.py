from xml.etree import ElementTree

"""方式一"""
tree = ElementTree.parse('my.xml')
print(tree.getroot().tag)

for group in tree.getroot():
    print(group.tag, group.attrib)  # 根标签名，属性键值对
    print(group.items())  # 属性键和值（列表套元组）
    print(group.find('year').text)  # 值

for option in tree.iter('year'):
    print(option.tag, option.text)

print(tree.findall('year'))  # []
print(tree.find('year'))  # None

"""方式二"""
# content = """
# <data>
#     <country name="Liechtenstein">
#         <rank updated="yes">2</rank>
#         <year>2023</year>
#         <gdppc>141100</gdppc>
#         <neighbor direction="E" name="Austria" />
#         <neighbor direction="W" name="Switzerland" />
#     </country>
#      <country name="Panama">
#         <rank updated="yes">69</rank>
#         <year>2026</year>
#         <gdppc>13600</gdppc>
#         <neighbor direction="W" name="Costa Rica" />
#         <neighbor direction="E" name="Colombia" />
#     </country>
# </data>
# """
#
# root = ElementTree.XML(content)
# print(root.tag)


content = """
<data>
    <country name="Liechtenstein">
        <rank>2</rank>
        <year>2023</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
     <country name="Panama">
        <rank>69</rank>
        <year>2026</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
"""

# root = ElementTree.XML(content)
#
# # 删除节点
# root.remove(root.find('country'))
# print(root.findall('country'))
#
# ############ 保存文件 ############
# tree = ElementTree.ElementTree(root)  # 要执行这一句
# tree.write("newnew.xml", encoding='utf-8')

