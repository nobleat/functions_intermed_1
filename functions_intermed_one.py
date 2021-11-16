x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]= 15
# print(x)

students[0]['last_name'] = 'Bryant'
# print(students)

sports_directory['soccer'][0]= 'Andres'
# print(sports_directory)

z[0]['y']=30
# print(z)


# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
	{'first_name':  'Michael', 'last_name' : 'Jordan'},
	{'first_name' : 'John', 'last_name' : 'Rosales'},
	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
	{'first_name' : 'KB', 'last_name' : 'Tonel'}
]



def iterateDictionary(students):
    for i in range(0,len(students)):
        name = ""
        for key, value in students[i].items():
            name += f"{key}, {value}"
        print(name)

iterateDictionary(students)

def iterateDict2(value, students):
    for i in range(0,len(students)):
        name=""
        for key, value in students[i].value():
            name +=f"{key}, {value}"
        print(name)
iterateDict2('first_name', students)