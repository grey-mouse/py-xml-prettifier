import sys
from xml.dom.minidom import parseString

def prettify_xml(file_path):
    with open(file_path, 'r') as file:
        xml_content = file.read()

    dom = parseString(xml_content)
    pretty_xml = dom.toprettyxml()

    with open(file_path, 'w') as file:
        file.write(pretty_xml)

if __name__ == "__main__":
    for file_path in sys.argv[1:]:
        prettify_xml(file_path)
