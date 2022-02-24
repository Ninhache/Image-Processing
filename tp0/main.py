import numpy as np
'''
a = np.array([[1.2,2.5],[3.2,1.8],[1.1,4.3]])


print("Type de a:", type(a))

print("Type de données: (ici float, vu que y'a des float..)", a.dtype)

print("Dimensions mais j'ai pas bien compris:", a.ndim)

print("Tuple X/Y:" , a.shape)

print("Nb d'elements:" , a.size)

print("A:" , a)


a = np . array ([[1 ,2] ,[4 ,7]])
print("type de A:(normalement int, vu que ya que des int)" , a.dtype)

a = np . array ([[1 ,2] ,[4 ,7]] , dtype = float )
print("Nouveau type de A:(normalement float, vu que ya le type de précisé)" , a.dtype)




a = np . arange (0 ,10) . reshape (2 ,5)

a = np . zeros ( shape =(2 ,4) )
'''

# Nouvelle matrices
a = np . array ([[1.2 ,2.5] ,[3.2 ,1.8] ,[1.1 ,4.3]])
b = np . array ([[4.1 ,2.6]])

# Nouvelle matrice à partir des 2 autres : 
# 
c = np . append (a ,b, axis=0)

print ( 'A\n', a )
print ( 'B\n', b )
print ( 'C\n', c )

'''
# ajouter une colonne
d = np . array ([[7.8] ,[6.1] ,[5.4]])
print ( np . append (a ,d , axis =1) )
# insertion
print ( np . insert (a ,1 ,b , axis =0) )

print ( np . delete (a ,1 , axis =0) )
# modifier la dimension d ’ une matrice existante
# parcours les données lignes par ligne
h = np . resize (a , new_shape =(2 ,3) )
print ( h )
'''