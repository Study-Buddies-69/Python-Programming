import random

def random_walk(n):
	x,y = 0,0

	for i in range(n):
		(dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
		#print("******",i)
		#print((dx,dy))
		x +=dx
		y +=dy
		#print(x)
		#print(y)
		#print("@@@@")

	return (x,y)

number_of_walks = 10 #10 random walks for each walk size
#  walk_len = walks of length 1 30 blocks
for walk_len in range(1,31):
	no_transport = 0
	#print("Step 1:Loops 3 times",walk_len)
	for walk_steps in range(number_of_walks):
		#print("Step 2: walk_step:",walk_steps)
		(x,y) = random_walk(walk_len)
		print(x,y)
		distance = abs(x)+abs(y)
		print("{} Distance covered for the no of walk step:{} ".format(distance,walk_steps))
		if distance <=4:
			no_transport +=1
	no_trans_per = float(no_transport)/number_of_walks
	print("****************")
	print("walk size = ",walk_len, " per of no transp",100*no_trans_per)
print("Complete")