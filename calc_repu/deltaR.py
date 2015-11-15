import pickle
import csv
import pdb
import linecache
from mpi4py import MPI
from demos import cmd

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


with open('movie_grade.list', 'rb') as f:
	GG = pickle.load(f)

def run(q):
	processors = 4
	urf = '../userRates/'+str(q)+'.csv'
	totalline = 0
	with open(urf,'rb') as ur:
		ur.next()
		totalline = sum(1 for x in ur)

	start = [0]*processors
	with open(urf,'rb') as ur:
		urr = csv.reader(ur)
		urr.next()
		l = [int(float(x)/processors*totalline) for x in range(processors)]
		for i,line in enumerate(urr):
			if i in l:
				start[l.index(i)] = int(line[0])
	
	with open(urf,'rb') as ur:
		ww = {}
		ll = {}
		urr = csv.reader(ur)
		urr.next()
		lastu = 0
		count = 0
		#weight = 0
		leniency = 0
		for line in urr:
			u = int(line[0])
			if u < start[rank]: continue
			if rank < processors - 1:
				if u > start[rank+1]: break
			if u != lastu:
				if lastu != 0: #recording the results for lastu
					#weight = weight/count
					leniency = leniency/count
					if leniency < -1 :leniency = -1
					if leniency > 1: leniency = 1
					ww[lastu] = 1-abs(leniency)
					ll[lastu] = leniency
					print lastu
					#if abs(leniency) > 0.8: print lastu,leniency
				lastu = u
				count = 0
				weight = 0
				leniency = 0
			m = int(line[1])
			g = float(line[2])
			G = GG[m]
			count += 1
			#weight = (g-G)**2
			leniency += (g-G)/g
		
		leniency = leniency/count
		if leniency < -1: leniency = -1
		if leniency > 1 : leniency = 1
		ww[lastu] = 1-abs(leniency)
		ll[lastu] = leniency
	
	if rank == 0:
		for i in range(1,processors):
			temp = comm.recv(source=i)
			ww.update(temp[0])
			ll.update(temp[1])
		with open('temweight/'+str(q)+'_tem_weight','wb') as tew:
			pickle.dump(ww,tew)
		with open('temleniency/'+str(q)+'_tem_leniency','wb') as tel:
			pickle.dump(ll,tel)
	else:
		ttt = [ww,ll]
		comm.send(ttt,dest=0)


if __name__ == '__main__':
	eval(cmd())
	#run(0)



