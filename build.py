#!/usr/bin/python

import glob
from subprocess import call

path = "/home/jumblesale/twine/"
basetwee = "%sbase.twee" % path

out = open(basetwee,'w')

out.write(":: StoryIncludes\n")

for twee in glob.glob("/home/*/ttitt/*.twee"):
	print('including %s' % twee)
	out.write("%s\n" % twee)

call("python %stwee/twee %s > %sindex.html" % (path, basetwee, path), shell=True)

out.close()