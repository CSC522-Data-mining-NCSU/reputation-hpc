import csv
import pickle
from WeightFinder import WeightFinder
import time
from mpi4py import MPI
import pickle
from demos import cmd

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
finder = WeightFinder()

def get_movie_grade(movie_id):
	try:
		f = open('../training_set/mv_'+str(movie_id).zfill(7)+'.txt','r')
	except: return 0
	reader = csv.reader(f)
	reader.next()
	score = 0
	sum_w = 0
	for row in reader:
		a = int(row[0])
		rate = float(row[1])
		foo, weight = finder.get_user_weight(a)
		score = score + weight * rate
		sum_w += weight
	#ground = pickle.load(open('movie_ground'))
	#ground[movie_id] = score/sum_w
	#pickle.dump(ground,open('movie_ground','w'))
	#print movie_id
	f.close()
	return score/sum_w

def run(q):
	processors = 4
	era = 0
	r = {}
	while True:
		k = era * processors + rank
		if k >= 1000: break
		if k%100 == 0: print k
		#if rank==0: print k
		k = k + int(q)*1000
		if k > 17770: break		
		r[str(k)] =  get_movie_grade(k)
		era += 1

	if rank == 0:
		for i in range(1,processors):
			temp = comm.recv(source=i)
			r.update(temp)
		with open('temgrade/'+str(q)+'_tem_grade','wb') as teg:
			pickle.dump(r, teg)
	else:
	        comm.send(r,dest=0)

if __name__ == '__main__':
	eval(cmd())
