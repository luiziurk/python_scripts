#%%
# Opens a .txt file and collects only the actors name
import os
import random as rnd
#%%
os.chdir(r'C:\Users\iurkl\OneDrive\Treinamentos\Udacity\Python')

with open('camelot.txt', 'w') as f:
    pass
#%%
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

#%%
def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)


    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)

# %%

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

def generate_password():
    count = 0
    password = ""
    while count < 3:
        w = word_list[rnd.randint(0,len(word_list))]
        password = password+w
        count +=1
    return password



    

# TODO: Add your function generate_password below
# It should return a string consisting of three random words 
# concatenated together without spaces



# Now we test the function
print(generate_password())

#%%

with open("flowers.txt") as t:
    lines = t.read().splitlines()

keyslist = []
flowerlist = []
for i in lines:

   j = i.split(":")
   keyslist.append(j[0])
   flowerlist.append(j[1])

flowers_dict = dict( zip(keyslist,flowerlist ))

username = input("What's your First and Last Name? ")

username = username.split()

print('Your Flower is: {0}'.format(flowers_dict[username[0][0]]) )


# %%
