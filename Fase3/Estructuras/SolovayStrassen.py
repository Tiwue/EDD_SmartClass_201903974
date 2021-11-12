import random  
   
def jacobi(a,n):  
         j = 1                               
         while (a != 0):  

             while (a%2==0):                       
                 j = j * pow(-1,(n*n-1)/8)    
                 a = a/2  
                   
             if not ( (a-3)%4 or (n-3)%4 ):  
                 j = -j  
                   
             a,n = n,a                        
             a = a % n                                  
         return j  
   
def solovay_strassen(n, k=10):  
     if n == 2 or n == 3:  
         return True  
     if not n & 1:  
         return False  
           
     for i in range(k):  
         a = random.randrange(2, n - 1)         
         x = jacobi(a, n)                      
           
         y = pow(a,int((n-1)/2), n)             
         if y != 1 and y != 0:                          
             y = -1  
         
         if (x == 0) or (y != x):              
             return False         
     return True  

def next_prime(n):
    numero=n+1
    while True:
        if solovay_strassen(numero,10):
            return numero
        else:
            numero += 1
