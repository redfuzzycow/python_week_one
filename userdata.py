import sys
with open('usernames.txt','r') as file:
	for line in file:
		creds = line.strip().split(':')
		sys.stdout.write('-u '+creds[0]+' -p '+creds[1]+' ')
		sys.stdout.flush()
print
