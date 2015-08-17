from xml.dom import minidom

def svgPaths(filepath):
    doc = minidom.parse(filepath)
    path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
    doc.unlink()
    return path_strings
