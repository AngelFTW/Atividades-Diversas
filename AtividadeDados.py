1)
lista = [] 
  
n = 6 

for i in range(0, n): 
    element = int(input()) 
  
    lista.append(element)
      
print(lista)



2)
lista = [] 
  
n = 10 

for i in range(0, n): 
    element = int(input()) 
  
    lista.append(element)
      
print('A lista possui',len(lista),'valores')




lista = [] 
  
n = 10  

for i in range(0, n): 
    element = int(input()) 
  
    lista.append(element)
lista.sort(reverse=True)     
print(lista) 




lista = [] 
  
n = 15  

for i in range(0, n): 
    element = int(input()) 
  
    lista.append(element)
Media = sum(lista)/len(lista)    
print("Media:",round(Media,2))  