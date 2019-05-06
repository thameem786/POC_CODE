# from docx import Document
# from xml.dom.minidom import parseString
#
# document = Document(r'C:\Users\thameem.sakkarai\Desktop\check\AOF edited document.docx')
# sections = document.section
# for i in sections:
#     print(i)
# xml_string = source_document._body._element.xml
# xml = parseString(xml_string)
# contents = xml.getElementsByTagName('w:bookmarkStart')
# # for i in xml:
# #     print(i)
# for i in contents:
#     print(i)



import docx

file_name = r'C:\Users\thameem.sakkarai\Desktop\check\AOF edited document.docx'

document = docx.Document(docx = file_name)

section = document.sections
header = section.header
print(header)
print(dir(document))
print(help(document))
core_properties = document.core_properties
print(core_properties.author)
print(core_properties.created)
print(core_properties.last_modified_by)
print(core_properties.last_printed)
print(core_properties.modified)
print(core_properties.revision)
print(core_properties.title)
print(core_properties.category)
print(core_properties.comments)
print(core_properties.identifier)
print(core_properties.keywords)
print(core_properties.language)
print(core_properties.subject)
print(core_properties.version)
print(core_properties.keywords)
print(core_properties.content_status)