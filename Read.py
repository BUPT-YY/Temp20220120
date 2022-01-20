import sys
filename = "./rawlog.txt"


doprint = [0,0,0,0,1,1,1,1,0,1,1,0]
chdic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'A':7}
strs = ["","","","","A501","A502","A503","A504","","A601","A602",""]
matrix = [ [0] * 12 for i in range(9)]
for i in range(12):
	matrix[7][i] = 1
matrix[0][2] = 3
matrix[0][8] = 11
matrix[5][1] = 2
matrix[6][1] = 8
matrix[1][11] = 9
matrix[2][11] = 10
for i in range(1,5):
	matrix[i][3] = (i+3)
state = 0
laststr = ""
cnt = 1
with open(filename, 'r') as sys.stdin:
	while 1:
		str1 = sys.stdin.readline().strip().upper()
		if str1:
			N = len(str1)
			for i in range(N):
				if(chdic.has_key(str1[i])):
					j = chdic[str1[i]]
				else:
					j = 8
				state = matrix[j][state]
				if doprint[state]:
					if laststr==strs[state]:
						cnt = cnt + 1
						#print strs[state],
					else:
						printstr = str(laststr) + ": " + str(cnt+1) + "time(s)"
						if(cnt+1>=4):
							print '\033[0;31m' + printstr + '\033[0m'
						else:
							print printstr
						cnt = 0
						#print strs[state],
					laststr = strs[state]

