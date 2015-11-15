import pickle
import csv
import pdb
from mpi4py import MPI
from demos import cmd

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

oneProcessorWorkload = 2500

with open('movie_grade.list', 'rb') as f:
	G = pickle.load(f)

def fetchRating(user_id, movie_id):
	rating = 0
	with open('../training_set/mv_'+str(movie_id).zfill(7)+'.txt','r') as f:
		reader = csv.reader(f)
		reader.next()
		for row in reader:
			a = int(row[0])
			if a == user_id:
				rating = float(row[1])
				break
	return rating


def startpoint(st):
	r  = {}
	um = open('user_movie.csv', 'rb')
	ums = csv.reader(um)
	next(ums) #ignore the first line
	
	for i,line in enumerate(ums):
		if i < st: continue
		user = int(line[0])
		delta = 0
		if line[1][-1]==',': # TODO BUG RESPONSE
			#movies = map(int, line[1][:-1].split(','))
			continue
		else:
			movies = map(int, line[1].split(','))
		for m in movies:
			delta += (G[m]-fetchRating(user,m))**2
		delta = delta / len(movies)
		print user, delta
		r[str(user)] = float(delta)
		if i >= st+oneProcessorWorkload-1:break
	um.close()
	return r

def run(q):
	processors = 4
	st = int(q) * oneProcessorWorkload * processors
	st += rank*oneProcessorWorkload + 1
	r = startpoint(st)

	if rank == 0:
		for i in range(1,processors):
			temp = comm.recv(source=i)
			r.update(temp)
		with open('temweight/'+str(q)+'_tem_weight','wb') as tew:
			pickle.dump(r,tew)
	else:
		comm.send(r,dest=0)

if __name__ == '__main__':
	eval(cmd())




