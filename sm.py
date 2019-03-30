import sys
import re

inFile = sys.argv[1]
outFile = sys.argv[2]

fin = open(inFile,'r')
text = fin.read()
fin.close()

bodyStart = text.find('\\begin{document}')
header = text[0:bodyStart]
body = text[bodyStart:]

macroRegex = re.compile(r'\A(\\def|\\newcommand|\\renewcommand)[\s\{]*(\\([a-zA-Z]+|[^a-zA-Z]))')
outputHeader = ''

for line in header.splitlines():
    m = macroRegex.search(line.strip())
    if(m):
        macroName = m.group(2)
        if(macroName in body):
            outputHeader += line + '\n'
    else:
        outputHeader += line + '\n'

  
fout = open(outFile,'w')
fout.write(outputHeader)
fout.write(body)
fout.close()
