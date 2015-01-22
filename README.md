tilde.town-twine
================
# What is this?
http://tilde.town/~jumblesale/twine/

It's a collaborative twine game for tilde.town. Anyone can contribute with the minimum possible barrier to entry.

# So how can I get involved
## 1. Are you a member of tilde.town?
* **No?**
Sign up for your account [here](http://goo.gl/forms/8IvQFTDjlo)!
* **Yep!**
Proceed to step 2

## 2. Creating your story file
The game works by searching every home directory for .twee files in your 'ttitt' subdirectory. so to start off,

    mkdir ~/ttitt

Great! Now we have somewhere for our .twee files to live.

## 3. Creating .twee files

There's a few ways we can do this based on what platform you're on and how you'd like to edit your story.

0. I'm on Mac / Windows and I'd like to use a GUI

    No problem! Just head over [here](http://twinery.org/downloads/) and get the most recent version for your platform

0. I'm on Linux but I still want to use a GUI

    Ok! It's not as neat as being on Mac / Windows but we still have you covered. Check out [this](http://wiki.doubleunion.org/index.php?title=Twine_for_Linux) amazing guide for details on getting set up and let us know in irc if you have any problems!
    
0. I care not for your GUI contrivances! All I need is a magnet and a steady hand!

    Alright that's cool too. If you're familiar with the .twee format (which is pretty straightforward), you can just edit the file directly on the server with your favourite text editor.
    
Whatever you choose, you have to be aware of a couple of things:

0. Your starting passage will be yourusername-start. So for me it's jumblesale-start. *Don't* use the :: Start passage because it will overwrite the default!
0. *Don't* set story title, story author or any other special passages! It's really rude.
0. Try to name your passages as username-passage so that the names don't conflict.

You can read up on creating twine stories [on the official site](http://twinery.org/wiki/).

## 4. Exporting your story

Exporting your story is really easy. If you're using the GUI, go to:

    File > Export > Twee Source Code...
    
And save your file somewhere handy.

If you've been editing your .twee file directly then proceed to the next step:

## 5. Uploading your story

Use whatever tool you have for connecting to your tilde.town account to copy your .twee file from where you saved it to the ttitt directory you created earlier.

## 6. Building your story

Now your .twee file is in place, it needs to be built along with all the other stories! Run the following command:

    /home/jumblesale/twine/build.py
    
Then checkout out your work at the [tilde.town twine url](http://tilde.town/~jumblesale/twine/)!


# Something went wrong

Let us know on irc or drop an email through alpine!


# What's the deal with ttitt?

Tass Times in Tilde Town comes from a [somewhat-obscure adventure game](https://www.youtube.com/watch?v=hUGOaSqhyzQ) from the Apple II.


# What kind of stuff should my story contain?

Really anything you want. The more unique the better.

A few themes of tilde.town that would be cool to see includes are:

* collaboration - using as many scripts or other resources other people have built on the server as much as possible
* exploration - sharing stuff you're interested in
* onion games which slowly reveal themselves like [candy box!](http://candies.aniwey.net/) or [a dark room](http://adarkroom.doublespeakgames.com/)


# How do I generate my own version of the twine?

By default, if you git clone this repo and run build.py, it will update the
global twine at /home/jumblesale. If instead you want to experiment with the
build process and generate your own twine, you can do the following:

0. `$ git clone https://github.com/jumblesale/tilde.town-twine twine && cd twine`
0. `./build.py -h` to get help or just `./build.py .` to generate the twine in
   the current working directory.

Have fun!

~jumblesale
