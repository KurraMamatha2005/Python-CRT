dicu={101:'python',102:'java',103:'sql',104:'java'}
typ={"rahul":2000, "raj":3000, "sonam":8000}
print(dicu)
print(type(dict))
print(dicu[101])
print(typ["raj"])
#updating or modifying an element
eventcode={101:"hachathon",102:"coding",103:"project"}
print(eventcode)
eventcode[102]="coding challange"
print(eventcode)
#adding items to ditnary
job={101:"full stack developer",102:"data engineer",103:"data analyst",104:"data scientist"}
print(job)
job[105]="cloud engeenier"
print(job)
#3 more job roles
job[106]="web developer"
job[107]="mechanical"
print(job)
# to delete elements in dictonary we use pop
job.pop(102)
print(job)
#removing using del keyword
del job[101]
print(job)
# len in dictonary returns number of key value pairs
print(len(job))
#key returns list of all keys in dictionary
print(job.keys())
#values method returns list of values
print(job.values())
#items in python returns key value pairs(tuple) in the dict
print(job.items())
# copy returns the copy of dicctonary
b=job.copy()
print(b)
#update method adds dictonary To change the value of a key, like updating a user's profile info.
dict1={1:"a",2:"b",3:"c"}
dict2={4:"r",5:"g",6:"h"}
print(dict1)
print(dict2)
dict1.update(dict2)
print(dict1)
#if key in dict returns value if not present it inserts the key and returns default value
#fromkeys it createsa dict with sequence of keys
#input a dna sequence of bases and count how many time  each base appears in a string and print it in dictonary format
# Input DNA sequence
dna_sequence = input("Enter a DNA sequence: ").upper()
# Initialize dictionary to store counts
base_counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
# Count each base
for base in dna_sequence:
    if base in base_counts:
        base_counts[base] += 1
# Print the dictionary
print(base_counts)
# based on value analyze wether the gene is expressed or unexpressed
count_data=int(input("enter the count of data:"))
enter_list=[]
for i in range(count_data):
    value=int(input(f"enter the elements in list{i+1}:"))
    enter_list.append(value)
print(enter_list)
for value in enter_list:
  if value < 5:
    print("under expressed")
  elif value in range(5,15):
    print("normal")
  elif value>15:
    print("over expressed")

#cpmparing two dna sequencesfrom different patients to find mutationS
seq1 = input("Enter sequence 1: ")
seq2 = input("Enter sequence 2: ")

# Ensure sequences are of equal length
if len(seq1) != len(seq2):
    print("Sequences are not of equal length.")
else:
    mutation_positions = []

    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mutation_positions.append(i)

    print("Mutation positions:", mutation_positions)

#sequence classification basd on gc content
dna_seq=input("enter the dna sequence:")
g_count=dna_seq.count('G')
c_count=dna_seq.count('C')
a_count=dna_seq.count('A')
t_count=dna_seq.count('T')
gc_content=(g_count+c_count)/len(dna_seq) *100
print(gc_content)
if gc_content<40:
  print("low gc content")
elif gc_content>=40 and gc_content<=60:
  print("moderate gc content")
else:
  print("high gc content")








