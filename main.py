from docxtpl import DocxTemplate
from docxtpl import docx
import json
import argparse

parser = argparse.ArgumentParser("A program to generate customised curriculums from a template")
parser.add_argument("templatePath", nargs='?', help="The path to the template to use (default: %(default)s)", 
    type=str, default="curriculumTemplate.docx")
parser.add_argument("informationFile", nargs='?', help="The path to the file containing the information to use in a json format (default: %(default)s)", 
    type=str, default="information.json")
parser.add_argument("resultPath", nargs='?', help="The path to write the result file in (default: %(default)s)", 
    type=str, default="result")

args = parser.parse_args()

print("Loading template from: " + args.templatePath)

try:
    doc = DocxTemplate(args.templatePath)
except docx.opc.exceptions.PackageNotFoundError:
    print("ERROR: Could not find template file, please make sure the path is valid")
    exit()

print("Loading and parsing JSON from: " + args.informationFile)
try:
    with open(args.informationFile, "r", encoding='utf8') as infile:
        templateInfo = json.loads(infile.read())
except FileNotFoundError:
    print("ERROR: Could not find information file, please make sure the path is valid")
    exit()
except json.decoder.JSONDecodeError as err:
    print("ERROR: The informationFile has JSON errors, review that is has no JSON errors and try again")
    print("    Additional Error Info: parsing failed on position " + str(err.pos) + ", line:" + str(err.lineno) + ", colno:" + str(err.colno))
    exit()

print("Printing information on the template")
doc.render(templateInfo)

try:
    print("Attempting to save the result in the document: " + args.resultPath)
    doc.save(args.resultPath + ".docx")
except PermissionError:
    print("ERROR: Cannot access the file, please close it and try again")
    exit()

print("Document saved successfully")