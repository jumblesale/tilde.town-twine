#!/usr/bin/python

import glob
import re
from subprocess import call

path = "/home/jumblesale/twine/"
basetwee = "%sbase.twee" % path

out = open(basetwee,'w')

pattern = r'^\/home\/([^\/]+)\/.*'

users = {}
twees = []

out.write(':: Start\n')

for twee in glob.glob("/home/*/ttitt/*.twee"):
	matches = re.match(pattern, twee)
	if not matches:
		continue
	user = matches.group(1)
	print('including %s from %s' % (twee, user))
	users[user] = 1
	twees.append(twee)

for user in users.keys():
	out.write('[[%s-start]]\n' % user)

out.write("\n\n:: StoryAuthor\n")

for user in users.keys():
	out.write('<a href="http://tilde.town/~%s">~%s</a>' % (user, user))

out.write("\n\n")

for twee in twees:
	with open(twee) as tweeFile:
		contents = tweeFile.read()
		out.write("%s\n" % contents)

out.close()

command = "python %stwee/twee %s > %sindex.html" % (path, basetwee, path)

print "running %s" % command

call(command, shell=True)
