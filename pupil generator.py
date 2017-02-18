
import random

firstNames=["Angus","Greg","Jack","Ben","Same","Tom","Gabby","James","Daniel","Alex","Charlie","Ryan","Tommy","Brad"]
secondNames=["Goody","Jones","Smith","New","James","Bush"]
grades=["A*","A","B","C","D","E","F","G"]

pupils=[]
for x in range(1000):
	first=random.choice(firstNames)
	second=random.choice(secondNames)
	grade=random.choice(grades)
	temp=[first,second,grade]
	pupils.append(temp)
	
	
file=open("pupils.txt","a")

for pupil in pupils:
	file.write("\n")
	file.write("=======================")
	for item in pupil:
		file.write("\n")
		file.write(str(item))
		
file.close()

print("Complete")
	
	
	