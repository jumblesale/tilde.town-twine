#!/usr/bin/python

import argparse
import glob
import os
import re
from subprocess import call

parser = argparse.ArgumentParser()
parser.add_argument('base_dir', type=str, nargs='?', help='The base directory '
                    'of the twine. The base.twee and output index.html file '
                    'will be written here.')
args = parser.parse_args()
print args.base_dir

path = os.path.abspath(args.base_dir or '/home/jumblesale/twine/')
exe_path = os.path.join(path, 'twee/twee')
basetwee = os.path.join(path, 'base.twee')
macrotwee = os.path.join(path, 'macros.twee')
index_path = os.path.join(path, 'index.html')

RE_TWEE = re.compile(r'^/home/([^/]+)/ttitt/(.*)\.twee$')
RE_MACRO = re.compile(r'macro')

users = {}
twees = []
macros = []
inits = {}

out = open(basetwee,'w')
out.write(':: Start\n')
out.write('<h2>Choose your fate</h2>')

for twee in glob.glob("/home/*/ttitt/*.twee"):
	match_data = RE_TWEE.match(twee)
	if not match_data:
		print 'no user / no filename found in %s' % twee
		continue

	user     = match_data.group(1)
	fileName = match_data.group(2)

        print('including %s (%s) from %s' % (twee, fileName, user))
        users[user] = True

        if RE_MACRO.search(fileName):
	    macros.append(twee)
        else:   
	    twees.append(twee)

	if fileName == 'globals.twee':
		inits[user] = True

for user in inits.keys():
	out.write('<<display "%s-globals" >>' % user)

out.write("\n")

# Macros
out.write('<<Init>> <<Starts>>')

out.write("\n\n:: StoryAuthor\n")

for user in users.keys():
	out.write('<a href="http://tilde.town/~%s">~%s</a><br />' % (user, user))

out.write("\n\n")

out.write(':: StoryTitle\n')
out.write('Team Twine in Tilde Town Tale')
out.write('\n\n')

for twee in twees:
	with open(twee) as tweeFile:
		contents = tweeFile.read()
		out.write("%s\n" % contents)
out.write("\n\n")
out.close()

outmacro = open(macrotwee, 'w')
for macro in macros:
	with open(macro) as macro_file:
		contents = macro_file.read()
		outmacro.write("%s\n" % contents)
outmacro.write("\n\n")
outmacro.close()

command = "python %(exe)s %(base)s %(macro)s > %(index)s" % {
  'exe': exe_path,
  'base': basetwee,
  'macro': macrotwee,
  'index': index_path,
}

print "running `%s'" % command
call(command, shell=True)
