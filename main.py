import json

requirements_content = ""

j = None
with open('top-pypi-packages-30-days.json', 'r') as f:
    j = json.load(f)

for row in j['rows']:
    requirements_content += (row['project'] + '\n')

print(requirements_content)