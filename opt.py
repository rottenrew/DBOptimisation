import csv
from random import randint
from random import random
from random import shuffle

print "***********************************************"
print "Database Query Optimisation"
print "\t\t\t\tShubham Chauhan"
print "\t\t\t\t2012JE0641"
print "***********************************************"

print ""
print "Default chromosome size : 5"
print "Default Mutation Rate : 1.0"
print "Default Crossover Rate : 1.0\n"

max_generations = input("Enter maximum number of Generations : ")
population_size = input("Enter Population Size : ")

chromosome_size = 5
mutation_rate = 1
crossover_rate = 1

#Functions

#Mutate function
def mutate(parent):

	child = list(parent)

	index1 = randint(0,chromosome_size-1)
	index2 = randint(0,chromosome_size-1)

	while (index2 == index1) :
		index2 = randint(0,chromosome_size-1)

	temp = child[index1]
	child[index1] = child[index2]
	child[index2] = temp

	return child
#end mutate

def crossover(parent1 , parent2):

	child = list()

	child.append(parent1[0])
	child.append(parent1[1])

	j=2
	for i in range(2, chromosome_size):

		while (child.count(parent2[j]) != 0):
			j=(j+1)%chromosome_size

		child.append(parent2[j])

	return child
#end crossover

def cost(query):

	count = 0
	
	#Distributed Databases
	DB1 = csv.DictReader(open('DB/DB1.csv','rb'))
	DB2 = csv.DictReader(open('DB/DB2.csv','rb'))
	DB3 = csv.DictReader(open('DB/DB3.csv','rb'))
	DB4 = csv.DictReader(open('DB/DB4.csv','rb'))
	DB5 = csv.DictReader(open('DB/DB5.csv','rb'))

	for row in DB1:
		if (int(row['ID'])!=query[0]):
			count=count+1;
		else:
			break

	for row in DB2:
		if (int(row['ID'])!=query[1]):
			count=count+1;
		else:
			break

	for row in DB3:
		if (int(row['ID'])!=query[2]):
			count=count+1;
		else:
			break

	for row in DB4:
		if (int(row['ID'])!=query[3]):
			count=count+1;
		else:
			break

	for row in DB5:
		if (int(row['ID'])!=query[4]):
			count=count+1;
		else:
			break

	return count
	
#end cost

chromosome = []
population = []

print "\n\nGenerating random initial population... "
print "***********************************************"

#Random Population Generation
for i in range(0,chromosome_size):
	chromosome.append(randint(1,200))

for i in range(0,population_size):
	shuffle(chromosome)
	population.append(list(chromosome))

print population
new_population = []

#Iterate for needed number of generations
for i in range(0,max_generations):
	
	print "\nComputing Generation : ", i+1 , "... "
	print "***********************************************"


	#Crossover / Mutate each chromosome with given probaility
	j=0
	while (j < population_size) :

		parent1 = population[j]
		print "\t Parent",j+1,": ",parent1, "Cost :" , cost(parent1)

		if (j+1 == population_size):

			child = mutate(parent1)
		
			if(cost(child)<cost(parent1)):
				population[j]=child

			print "\t\t After Mutation, Child",j+1,": ",population[j], "Cost :",cost(population[j])
			break

		parent2 = population[j+1]
		print "\t Parent",j+2,": ",parent2, "Cost :", cost(parent2)

		#crossover each chromosome with next one
		if(random() <= crossover_rate) :
			
			pcost1 = cost(parent1)
			pcost2 = cost(parent2)

			child1 = crossover(parent1,parent2)
			child2 = crossover(parent2,parent1)
			
			ccost1 = cost(child1)
			ccost2 = cost(child2)

			if(ccost1<pcost1):
				parent1 = child1
			if(ccost2<pcost2):
				parent2 = child2

			print "\t\t After Crossover, Child",j+1,parent1,"Cost :",cost(parent1)
			print "\t\t After Crossover, Child",j+2,parent2,"Cost :",cost(parent2)


		if(random()<=mutation_rate):

			pcost1 = cost(parent1)
			pcost2 = cost(parent2)

			child1 = mutate(parent1)
			child2 = mutate(parent2)
			
			#print parent1, child1
			#print parent2, child2

			ccost1 = cost(child1)
			ccost2 = cost(child2)

			#print "\t\t\t",pcost1,pcost2,ccost1,ccost2

			if(ccost1<pcost1):
				parent1 = child1
			#else:
				#print "\t\t\t Mutation child",j+1,"discarded!"

			if(ccost2<pcost2):
				parent2 = child2
			#else:
				#print "\t\t\t Mutation child",j+2,"discarded!"

			print "\t\t\t After Mutation, Child",j+1,parent1,"Cost :",cost(parent1)
			print "\t\t\t After Mutation, Child",j+2,parent2,"Cost :",cost(parent2)

		population[j]=parent1
		population[j+1]=parent2

		j=j+2
	#end of while

	print "... done!"
	shuffle(population)

#end of for
print ""
print "COMPLETED!"
print "***********************************************"
print "Final Population : "
print population
print "***********************************************"

min_cost = cost(population[0])
min_index = 0

for i in range(1,population_size):
	temp = cost(population[i])
	if (temp<min_cost):
		min_cost = temp
		min_index = i

print "Optimised Query :",population[min_index]
print "Optimised Cost :",min_cost
print "***********************************************"



			



	






