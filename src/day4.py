#task1
contact = {"abc":4561,"xyz":4125,"mba":1436}
contact["ads"]= 6789
for name,number in contact.items():
    print(name,number)
print("\n\n",contact.get("ads"))
    
   #task2
raw_logs = ["ID01","ID02","ID03","ID04"]
unique_users =set(raw_logs)
print(unique_users)
print("IDO5"in unique_users)
print("ID10"in unique_users)
print(len(unique_users))
         
   #task3
friend_a = {"python", "cooking","hiking","movies"}
friend_b = {"hiking", "gaming","photography","python"}
print (friend_a | friend_b)
print(friend_a & friend_b)
print(friend_a - friend_b) 
