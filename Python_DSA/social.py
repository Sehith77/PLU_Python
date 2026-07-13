graph = {
    "Snehith": ["Patel", "Kola"],
    "Patel": ["Snehith", "mouli"],
    "Shashi": ["Snehith"],
    "mouli" : ["Patel"],
    "Ravi" : ["Kola"],
}
print("Users and Friends:")
for user in graph:
    
    print(user, "->", graph[user])
    
users = list(graph.keys())

for i in range(1, len(users)):
    key = users[i]
    
    j = i - 1
    while j >= 0 and users[j] > key:
        users[j + 1] = users[j]
        j -= 1
    users[j + 1] = key
    
print(
                     
        
        
  
                

