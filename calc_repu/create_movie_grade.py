import pickle

f = open('movie_ground','w')
ground = [1]*17771
pickle.dump(ground,f)
