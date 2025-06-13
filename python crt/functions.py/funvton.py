#function decleration
def Dispaly_prog():
    #function definition
    print("programming languages")
    print("pyhton")
    print("sql")
#function call
Dispaly_prog()
Dispaly_prog()
Dispaly_prog()
Dispaly_prog()
Dispaly_prog()

#understanding return statment
def dispaly():
    return "hello "
#function call while in return we have to store it in another variable to pri t
res=dispaly()
print(res)#output:hello

# with arguments
def namedfunction(name):
    return f"hello{name}"
re=namedfunction("mamu")
print(re)
#even or odd
def even_odd(num):
    if (num%2==0):
        print(f"the {num} is even")
    else:
        print(f"the {num} is odd")
even_odd(10)
even_odd(35)

#prime number program using return
def is_prime(Num):
    if (Num==2 and 3 and 5 and 7 and 11):
        print(f"{Num} is a prime number")
    elif (Num%2 and 3 and 5 and 7 and 11!=0):
        print(f"{Num} is a PRIME NUMBER")
    else:
        print(f"{Num} is not a PRIME NUMBER")
is_prime(17)

#multiplication table of n
def multiplication_table(n):
    for i in range(1, 11):
        ans = n*i
        print(f"{n} * {i} = {ans}")
multiplication_table(2)

#multiplication table from 1 to n
def multiplication_tablerange(n):
    for i in range(1, n+1):
        for j in range(1, 11):
            an=i*j
            print(f"{i} * {j} = {an}")
multiplication_tablerange(3)

#function to find matches in the sequence
def query_seq_match(str,db,list):
    matches=[]
    for seq_id, sequence in db.items():
        if query in sequence:
            matches.append(seq_id)
    return matches
db = {
    "seq001": "ATGCGGAATT",
    "seq002": "CGTACGTAGC",
    "seq003": "TTATGCATTA",
    "seq004": "GGAATCCGTA",
    "seq005": "CATGCCGTAGC",
    "seq006": "GGGCGTGCAT",
    "seq007": "AATGCTAGCTA",
    "seq008": "CGCGATGCGC",
    "seq009": "TATATATATA",
    "seq010": "ATGCGGATGCA"
}

query = "ATGCGG"
result = query_seq_match(query, db)
print("Matched Sequences:", result)


    

    




    
        

