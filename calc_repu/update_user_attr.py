import pickle
import pdb
import csv

all_len = {}
all_wei = {}
for i in range(27):
	with open('temleniency/'+str(i)+'_tem_leniency', 'rb') as tl:
		c = pickle.load(tl)
		all_len.update(c)

for i in range(27):
	with open('temweight/'+str(i)+'_tem_weight','rb') as tw:
		c = pickle.load(tw)
		all_wei.update(c)

w = all_len.keys()
w=sorted(w)

with open('user_attr.csv','wb') as out:
	out.write('id'+',weight'+',leniency\n')
	qq = 0
	for x in w:
		out.write(str(x))
		out.write(',')
		out.write(str(all_wei[x]))
		out.write(',')
		out.write(str(all_len[x]))
		out.write('\n')
		if qq > 10: break
		qq += 1
