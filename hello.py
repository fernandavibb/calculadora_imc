
#print("hello world")
#a = 8
#b = 1 
#c = 2
#calculo = a % c
#print(calculo)


#def calculo(a,c):
#    print(a / c)


#calculo(8,2)
#calculo(5,3) 
#calculo(10,5) 

#se o número for maior que 5 ele tem que estar verde, se ele for menor vai ser vermelho
#def semaforo (valor) :
    #if valor > 5:
    #    print ("verde")
    #elif valor == 5 :   
     #   print ("amarelo") 
    #else:
     #   print ("vermelho")


#semaforo (5)









def massa () :
    print ("Calculadora de IMC")

    nome = input ("Qual e seu nome?")
    peso = float (input ("Qual seu peso( em KG)" ))
    altura = float (input ( "Qual sua altura (em metros e usando ponto"))
    imc = ( peso / ( altura * altura))
    

    
    if imc < 24.9 :
        print (f"{nome},seu imc foi {imc} de acordo com a faixa e considerado normal") 
    elif imc >= 25.0 and imc <= 39.9:
        print (f"{nome}),seu imc for {imc} de acordo com a faixa e considerado sobrepeso")
    else :
      print (f"{nome}seu imc for {imc} de acordo com a faixa e considerado obesidade grave")

massa()




