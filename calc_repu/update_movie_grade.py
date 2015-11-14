import pickle

mv_grade = [0]*17771

for i in range(18):
	with open('temgrade/'+str(i)+'_tem_grade', 'rb') as tf:
		c = pickle.load(tf)
	for (mi, grade) in c.items():
		mv_grade[int(mi)] = float(grade)
	print str(i)+ " DONE!"

with open('movie_grade.list', 'wb') as mg:
	pickle.dump(mv_grade, mg)
