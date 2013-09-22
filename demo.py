
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
	x = 737
	dialAC(x)
	
	person = "Denard"
	dialPerson(person)
	return

def found(happy):
	happy = True
	return getBounds(900, 100)

def dialAC(x):
	y = 291
	dialDigits(y)
	return

def dialDigits(x):
	return map("Dora")

def dialPerson(name):
	return name





