#websiteRegex.py -- Finds all website domains on the clipboard

import pyperclip, re

#creating the website regex
websiteRegex = re.compile('(?:(?:https?):\/\/)?(?:w{3}\.)?[\w/\-?=%]+\.[a-zA-Z]{2,4}[\w/\-&?=%.]*')

#Finding matches in clipboard text
text = str(pyperclip.paste())

matches = []

for match in websiteRegex.findall(text):
    matches.append(match)

#Copying results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard.')
    print('\n'.join(matches))
else:
    print('No website names found.')
