import matplotlib.pyplot as plt

#Tempo de execucao do Insertion Sort em segundos para cada qtd de elementos

condicoes = [10,25,50,75,100,250,500,750,1000,2500,5000,7500,10000,25000,50000,75000,100000]

dados = [0.000002,0.000003,0.000015,0.000029,0.000056,0.000214,
         0.000665,0.001416,0.002529,0.017243,0.056830,0.125450,
         0.226864,1.381288,5.432714,12.330618,22.930238]

#Criando grafico mais geral
plt.rcParams['figure.figsize'] = (10,8)
plt.xlabel('n')
plt.ylabel('s')
plt.xlim(0,100000)
plt.ylim(0,25)
plt.title("Tempo decorrido na ordenacao")
plt.plot(condicoes, dados)
plt.show()
