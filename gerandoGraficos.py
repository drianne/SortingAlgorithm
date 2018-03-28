import matplotlib.pyplot as plt

#dados em segundos contando com o caso de cem mil dados

condicoes = [10,50,100,500,1000,5000,10000,50000,100000]

dados = [08.09, 10.84, 11.02, 12, 12.93, 13.13, 15.3, 17.76, 31.86 ]


#Escalas 10,100,1000,10000,100000,1000000

#dados_real = [0.061,1.622,2.208,2.633,2.546,1265.742]

#dados_user = [0.044, 0.000, 0.008, 0.248, 0.836, 1263.86]

#dados_sys = [0.016, 0.000, 0.000, 0.000, 0.052]


#Grafico com os valores do estado real

plt.title("Dados tempo gravado com cronômetro, incluindo tempo de encerramento")
plt.plot(condicoes, dados)
plt.show()
