def maior_numero(num1, num2, num3):
    maior = num1  
    
    if num2 > maior:
        maior = num2
    
    
    if num3 > maior:
        maior = num3
    
    return maior


resultado = maior_numero(10, 25, 15) 
print("O maior número é:", resultado)
