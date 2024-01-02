#sets

#defining an empty set
set_var= set()
type(set_var)

#define set
set_var={1,2,3,4,3}
set_var={"Avengers","IronMan",'Hitman'}
print(set_var)   #{'IronMan', 'Hitman', 'Avengers'}

## Inbuilt function in sets
set_var.add("Hulk") #{'IronMan', 'Hitman', 'Avengers', 'Hulk'}

set2={"Avengers","IronMan",'Hitman','Hulk2'}
set2.intersection_update(set1)
set2 #{'Avengers', 'Hitman', 'IronMan'}

##Difference 
set2.difference(set1)
set2.difference_update(set1)


#Dictionaries
my_dict={"Car1": "Audi", "Car2":"BMW","Car3":"Mercidies Benz"}
type(my_dict)  #dict

##Access the item values based on keys
my_dict['Car1']  #Audi

# We can even loop throught the dictionaries keys
for x in my_dict:
    print(x)      #Car1 Car2 Car3

# We can even loop throught the dictionaries values
for x in my_dict.values():
    print(x)     #Audi BMW Mercidies Benz

# We can also check both keys and values
for x in my_dict.items():
    print(x)     #('Car1', 'Audi') ('Car2', 'BMW') ('Car3', 'Mercidies Benz')

# Adding items in Dictionaries
my_dict['car4']='Audi 2.0'  #{'Car1': 'Audi', 'Car2': 'BMW', 'Car3': 'Mercidies Benz', 'car4': 'Audi 2.0'}

#nested dictinoaries
car1_model={'Mercedes':1960}
car2_model={'Audi':1970}
car3_model={'Ambassador':1980}

car_type={'car1':car1_model,'car2':car2_model,'car3':car3_model}    #{'car1': {'Mercedes': 1960}, 'car2': {'Audi': 1970}, 'car3': {'Ambassador': 1980}}

# Accessing the items in the dictionary
print(car_type['car1'])   #{'Mercedes': 1960}
print(car_type['car1']['Mercedes'])  #1960

#tuples
# create an empty Tuples
my_tuple=tuple()

my_tuple=("Jesse","Peter","Ryan")
print(my_tuple)  #("Jesse","Peter","Ryan")

## Inbuilt function
my_tuple.count('Jesse')  #1







  







