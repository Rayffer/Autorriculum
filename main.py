from docxtpl import DocxTemplate
import json
import argparse

parser = argparse.ArgumentParser("A program to generate customised curriculums from a template")
parser.add_argument("templatePath", nargs='?', help="The path to the template to use (default: %(default)s)", 
    type=str, default="curriculumTemplate.docx")
parser.add_argument("informationFile", nargs='?', help="The path to the file containing the information to use in a json format (default: %(default)s)", 
    type=str, default="information.json")
parser.add_argument("resultPath", nargs='?', help="The path to write the result file in (default: %(default)s)", 
    type=str, default="result.docx")

args = parser.parse_args()

print("Loading template from: " + args.templatePath)
doc = DocxTemplate(args.templatePath)

print("Loading and parsing JSON from: " + args.informationFile)
with open(args.informationFile, "r", encoding='utf8') as infile:
    templateInfo = json.loads(infile.read())
print("Printing information on the template")
doc.render(templateInfo)

try:
    print("Attempting to save the result in the document: " + args.resultPath)
    doc.save(args.resultPath)
except PermissionError:
    print("Cannot access the file, please close it and try again")
    exit()

print("Document saved successfully")