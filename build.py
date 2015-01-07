#!/usr/bin/python

import glob
import re
from subprocess import call

path = "/home/jumblesale/twine/"
basetwee = "%sbase.twee" % path

out = open(basetwee,'w')

userPattern = r'^\/home\/([^\/]+)\/.*'
filePattern    = r'.*\/(.*)\.twee$'

users = {}
twees = []
inits = {}

out.write(':: Start\n')

for twee in glob.glob("/home/*/ttitt/*.twee"):
	userMatches = re.match(userPattern, twee)
	fileMatches = re.match(filePattern, twee)
	if not userMatches or not fileMatches:
		print 'no user / no filename found in %s' % twee
		continue
	
	user     = userMatches.group(1)
	fileName = fileMatches.group(1)
	
	print('including %s (%s) from %s' % (twee, fileName, user))
	users[user] = 1
	twees.append(twee)

	if fileName == 'globals.twee':
		inits[user] = 1

out.write("\n\n")

for user in inits.keys():
	out.write('<<display "%s-globals" >>' % user)

out.write("\n")

# Macros
out.write('<<Init>> <<Starts>>')

out.write("\n\n:: StoryAuthor\n")

for user in users.keys():
	out.write('<a href="http://tilde.town/~%s">~%s</a>' % (user, user))

out.write("\n\n")

for twee in twees:
	with open(twee) as tweeFile:
		contents = tweeFile.read()
		out.write("%s\n" % contents)

out.write("\n\n")

out.close()

command = "python %stwee/twee %s > %sindex.html" % (path, basetwee, path)

print "running %s" % command

call(command, shell=True)
