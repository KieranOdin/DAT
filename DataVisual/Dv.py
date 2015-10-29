from graphics import *
import random, time


line = []

def readfile():
    f = open('data.txt')
    for x in range(0,31):
        line.append(f.readline())
        print line[x] 
    return line 


def main():
    win = GraphWin('Face', 400, 400) # give title and dimensions
	for i in range(0,31):
    	head = Circle(Point(200,200), float(randomMark)) # set center and radius
    	head.setFill("yellow")
    	head.draw(win)

		eye1 = Circle(Point(180, 185), eyediv)
		eye1.setFill('blue')
		eye1.draw(win)

		eye1 = Circle(Point(220, 185), eyediv)
		eye1.setFill('blue')
		eye1.draw(win)

		mouth = Oval(Point(180, 210), Point(220, 220)) # set corners of bounding box
		mouth.setFill("red")
		mouth.draw(win)
	
		label = Text(Point(100, 120), 'A face')
		label.draw(win)

		message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
		message.draw(win)
		
		time.sleep(1)
		
		win.getMouse()
		
    win.close()


	
readfile()

print(' ')
randomMark = random.choice(line)
print('The random mark is  ' + randomMark)

eyediv = (float(randomMark) * 0.25)

	
main()