
def main():
	w = 50
	h = 30
	getBounds(w, h)
	lost("Ann Arbor")

def getBounds(width, height):
	name = "Map"
	dimensions = width * height;
	map(name)
	return dimensions

def map(name):
	x = "This is " + name
	destination = [0, 2]
	directions(destination)
	return x

def directions(dest):
	print "You're moving to dest"
	return

def lost(home):
	print "Help!"
	num = 1394923
	callNum(num)
	found(False)
	return

def callNum(num):
	print "Calling: %d" % num
	dialAC(737)
	dialDigits(291)
	dialPerson("Denard")
	return

def found(happy):
	happy = True
	return getBounds(900, 100)

def dialAC(x):
	return

def dialDigits(x):
	return

def dialPerson(name):
	return name





