from jinja2 import Template
from docxtpl import DocxTemplate
import json

doc = DocxTemplate("curriculumTemplate.docx")

with open("information.json", "r") as infile:
    templateInfo = json.loads(infile.read())
doc.render(templateInfo)
doc.save("result.docx")