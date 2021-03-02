# Autorriculum

A tool based on python to automate the generation of curriculums using a template filled with data. The template has to use [jinja2](https://jinja.palletsprojects.com/en/2.11.x/templates/) syntax.

The template used must be a Microsoft Word Document file and the information to print on the template must follow the JSON standard.

If the template and the information are both valid, the script will output as much information as it can from the information file on the template and save it to the specified file.

## Requirements
This script depends on the following python packages:
- Jinja2
- DocxTpl

For the script to work you need to have both installed through pip or conda.

## Usage

To have a demo file of the script, just run `main.py` as is.

The script accepts some optional arguments, detailed in the following:
- `templatePath`: Specifies the template to use by the script.
- `informationFile`: Specifies the information file (in JSON format) to use by the script.
- `resultPath`: Specifies the path where the script will save its result.

This script can be used to generate any kind of document given you follow Jinja 2 syntax in your document for all the information that can vary. Keep in mind any member you attempt to access in the template must be informed in the template, otherwise it will not appear in the result file and might lead to empty section titles.
