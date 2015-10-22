import random

def readfile():
	line = f.readline()
	line = line.split(',', line.count(','))
	line[len(line) -1] = line[len(line) -1][:-1]
	
	#print line
	return line

def response(userinput, words, resp):
	for x in range(0,len(words)):
		if words[x] in userinput:
			rand_response = random.choice(resp)
			print rand_response
			return True
	return False

def writetofile(words):
	userinput = raw_input('ME<#>:  ').lower()
	f = open('DATA.txt', 'w')
	words.append(userinput)
	f.write(','.join(greet) + '\n')
	f.write(','.join(quest) + '\n')
	f.write(','.join(bwords) + '\n')
	f.write(','.join(gwords) + '\n')
	f.write(','.join(bresp) + '\n')
	f.write(','.join(gresp) + '\n')
	f.write(','.join(gyes) + '\n')
	f.write(','.join(bno) + '\n')
	f.write(','.join(thanks) + '\n')
	f.write(','.join(bthanks) + '\n')
	f.close()

conversation = True

while conversation:
	f = open('DATA.txt', 'r')
	
	greet = readfile()
	quest = readfile()
	bwords = readfile()
	gwords = readfile()
	bresp = readfile()
	gresp = readfile()
	gyes = readfile()
	bno = readfile()
	thanks = readfile()
	bthanks = readfile()
		
	f.close()

	print('Hello')
	userinput = raw_input('ME<#>:  ').lower()
	didnt = 'Did not understand, learnt, retry...'
	if userinput not in greet:
		#response(userinput,greet,didnt)
		writetofile(greet)
		
	else:
		rand_greetings = random.choice(greet)
		print rand_greetings
		rand_questions = random.choice(quest)
		print rand_questions
		
		userinput = raw_input('ME<#>:  ').lower()
		if not response(userinput, bwords, bresp):
			if not response(userinput, gwords, gresp):
				print 'I dont recognise this response, are you feeling good or bad?'
				userinput = raw_input('ME<#>:  ').lower()
				if userinput == 'good':
					print('What word made your sentence positive?')			
					writetofile(gwords)
				elif userinput == 'bad':
					print('What word made your sentence negative?')
					writetofile(bwords)
				else:
					print('Something went wrong')
		
		print('Did you enjoy our conversation? Yes/No?')
		userinput = raw_input('ME<#>:  ').lower()
		if not response(userinput, gyes, thanks):	
			rand_thanks = random.choice(bthanks)
			print rand_thanks
			
	conversation = False