import pickle
import csv
import pdb
#import linecache

with open('movie_grade.list', 'rb') as f:
	movie_current_grade = pickle.load(f)

report = open('buggy_user_id.csv','w')

um = open('user_movie.csv', 'rb')
ums = csv.reader(um)
next(ums) #ignore the first line

u = 0
for i,line in enumerate(ums):
	if line[1][-1]==',':
		report.write(line[0]+'\n')
	#user_id = int(line[0])
	#movies  = map(int, line[1][:-1].split(','))
um.close()
