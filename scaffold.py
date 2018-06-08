# scaffold for CRA 1.0
import sys
import os, errno

from lxml import html
import requests

import subprocess

## ----------------------------------
## HELPERS
## ----------------------------------
def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

def renameReplaceFile(output, original):
    silentremove(original)
    os.rename(output, original)

## ----------------------------------

print('Starting... scaffold')
fileName = sys.argv[1]

## ----------------------------------
print('removing... files')

pathSrc = './{0}/src'.format(fileName)
path = './{0}'.format(fileName)

silentremove(pathSrc + '/App.test.js')
silentremove(pathSrc + '/logo.svg')
silentremove(pathSrc + '/App.css')

print("Files removed!")
## ----------------------------------


## ----------------------------------
print('modifying... files')

# Modify index.js
fileToMod = pathSrc + '/index.js'
fileModDelim = '__'
with open(fileToMod, 'r') as input_file, open(fileToMod+fileModDelim, 'w') as output_file:
    for line in input_file:
        if line.strip() == "import registerServiceWorker from './registerServiceWorker';":
            output_file.write("//import registerServiceWorker from './registerServiceWorker';"+'\n')
        elif line.strip() == "registerServiceWorker();":
            output_file.write("//registerServiceWorker();"+'\n')
        else:
            output_file.write(line)
    renameReplaceFile(fileToMod+fileModDelim, fileToMod)

# Modify index.css
# https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.0/normalize.min.css
CDN_URL = 'https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.0/normalize.min.css'

page = requests.get(CDN_URL)
tree = html.fromstring(page.content)

fileToMod = pathSrc + '/index.css'
fileModDelim = '__'
file = open(fileToMod+fileModDelim,'w+')
file.write(page.content.decode('utf8')+'\n')
file.close()

renameReplaceFile(fileToMod+fileModDelim, fileToMod)

#rename it to a scss
os.rename(fileToMod, pathSrc + '/index.scss')

# Modify package.json
print('npm installing... ')
subprocess.check_call('yarn add node-sass-chokidar npm-run-all --prefix '+fileName, shell=True)

print('npm install done!')
fileToMod = path + '/package.json'
fileModDelim = '__'
with open(fileToMod, 'r') as input_file, open(fileToMod+fileModDelim, 'w') as output_file:
    for line in input_file:
        if line.strip() == '"start": "react-scripts start",':
            output_file.write('    "start": "npm-run-all -p watch-css start-js",\n')
            output_file.write('    "start-js": "react-scripts start",\n')
        elif line.strip() == '"build": "react-scripts build",':
            output_file.write('    "build": "npm run build-css && react-scripts build",\n')
            output_file.write('    "deploy": "node deploy",\n')
            output_file.write('    "build-css": "node-sass-chokidar --include-path ./src --include-path ./node_modules src/ -o src/",\n')
            output_file.write('    "watch-css": "npm run build-css && node-sass-chokidar --include-path ./src --include-path ./node_modules src/ -o src/ --watch --recursive",\n')
        else:
            output_file.write(line)
    renameReplaceFile(fileToMod+fileModDelim, fileToMod)

# Modify App.js
fileToMod = pathSrc + '/App.js'
fileModDelim = '__'
with open(fileToMod, 'r') as input_file, open(fileToMod+fileModDelim, 'w') as output_file:
    for line in input_file:
        if line.strip() == "import logo from './logo.svg';":
            output_file.write("")
        elif line.strip() == '<header className="App-header">':
            output_file.write('')
        elif line.strip() == '</header>':
            output_file.write('')
        elif line.strip() == '<img src={logo} className="App-logo" alt="logo" />':
            output_file.write('')
        elif line.strip() == '<h1 className="App-title">Welcome to React</h1>':
            output_file.write('')
        elif line.strip() == '<p className="App-intro">':
            output_file.write('')
        elif line.strip() == 'To get started, edit <code>src/App.js</code> and save to reload.':
            output_file.write('')
        elif line.strip() == '</p>':
            output_file.write('w00t')
        else:
            output_file.write(line)
    renameReplaceFile(fileToMod+fileModDelim, fileToMod)

print("Files Modified!")
## ----------------------------------


## ----------------------------------
print('generating... folders')

file_path = pathSrc + '/config/_blank'
directory = os.path.dirname(file_path)

try:
    os.makedirs(directory)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# Making colors.scss
fileToMake = pathSrc + '/config/colors.scss'
with open(fileToMake, 'w') as output_file:
    output_file.write('// DO NOT USE THESE VALUES\n')
    output_file.write('$COLOR_CRIMSON: #C6426E;\n')
    output_file.write('$COLOR_WHITE: #FFFFFF;\n')
    output_file.write('$COLOR_FROST: #e9e9e9;\n')
    output_file.write('$COLOR_SUBTLE: #484848;\n')
    output_file.write('$COLOR_LIGHTGRAPHITE: #676767;\n')
    output_file.write('$COLOR_GRAPHITE: #282B2D;\n')

# Making colors.scss
fileToMake = pathSrc + '/config/colors.scss'
with open(fileToMake, 'w') as output_file:
    output_file.write('// DO NOT USE THESE VALUES\n')
    output_file.write('$COLOR_CRIMSON: #C6426E;\n')
    output_file.write('$COLOR_WHITE: #FFFFFF;\n')
    output_file.write('$COLOR_FROST: #e9e9e9;\n')
    output_file.write('$COLOR_SUBTLE: #484848;\n')
    output_file.write('$COLOR_LIGHTGRAPHITE: #676767;\n')
    output_file.write('$COLOR_GRAPHITE: #282B2D;\n')

# Making media.scss
fileToMake = pathSrc + '/config/media.scss'
with open(fileToMake, 'w') as output_file:
    output_file.write('// @media #{$bsDesktop} {\n')
    output_file.write('// }\n')
    output_file.write('// @media #{$bsTablet} {\n')
    output_file.write('// }\n')
    output_file.write('// @media #{$mobile} {\n')
    output_file.write('// }\n\n')
    output_file.write('$mobile: "(max-width: 767px)";\n')
    output_file.write('$tablet: "(min-width: 768px) and (max-width: 1023px)";\n')
    output_file.write('$laptop: "(min-width: 1024px) and (max-width: 1439px)";\n')
    output_file.write('$desktop: "(min-width: 1440px)";\n\n')
    output_file.write('$notDesktop: "(max-width: 1023px)";\n')
    output_file.write('$notMobile: "(min-width: 768px)";\n\n')
    output_file.write('$aboveTablet: "(min-width: 1023px)";\n')

# Making shared.scss
fileToMake = pathSrc + '/config/shared.scss'
with open(fileToMake, 'w') as output_file:
    output_file.write("@import './colors.scss';\n")
    output_file.write("@import './media.scss';\n")

# Making u-responsive.scss
fileToMake = pathSrc + '/config/u-responsive.scss'
with open(fileToMake, 'w') as output_file:
    output_file.write('@import \'./media.scss\';\n\n')
    output_file.write('.container {\n')
    output_file.write('    width: 100%;\n')
    output_file.write('    margin: 0 auto;\n')
    output_file.write('    transition: width ease .2s;\n\n')
    output_file.write('    @media #{$desktop} {\n')
    output_file.write('        width: 1200px;\n')
    output_file.write('    }\n\n')
    output_file.write('    @media #{$laptop} {\n')
    output_file.write('        width: 970px;\n')
    output_file.write('    }\n\n')
    output_file.write('    @media #{$tablet} {\n')
    output_file.write('        width: 730px;\n')
    output_file.write('    }\n')
    output_file.write('}\n')

# Making App.scss
fileToMake = pathSrc + '/App.scss'
with open(fileToMake, 'w') as output_file:
    output_file.write('@import \'./config/u-responsive.scss\';')

print('Files all generated! Happy CRApy!')
## ----------------------------------
