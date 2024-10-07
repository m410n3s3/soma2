
def Comissaosalario():
    Nome = input("Entre com o nome do vendedor: ")
    SalarioFixo = float(input("Informe o salário: "))
    Vendas = float(input("Informe o valor em vendas: "))
    Comissao = 0.15*Vendas
    PagamentoEsperado = SalarioFixo+Comissao

    return Nome,  Comissao, PagamentoEsperado

if __name__=="__main__":
    Nome, Comissao, PagamentoEsperado = Comissaosalario()
    strg = "{0} obteve R$: {1:.2f} de comissão e vai receber: {2:.2f}".format(Nome,Comissao,PagamentoEsperado)
    print(strg)







#     import math as m

# def eq2grau(a,b,c):
#     delta = m.pow(b,2)-4*a*c
#     if (delta>0):

#         x1= (-b-pow(delta,0.5))/(2*a)
#         x2= (-b+pow(delta,0.5))/(2*a)

#         return x1 , x2
#     elif (delta==0):
#         print("")








# if __name__=="__main__":
#     x1, x2 = eq2grau(1,4,3)
#     print(f"as raízes são {x1} e {x2}")