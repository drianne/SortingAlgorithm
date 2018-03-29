import matplotlib.pyplot as plt

#Tempo de execucao do Insertion Sort em segundos para cada qtd de elementos

condicoes = [10,25,50,75,100,250,500,750,1000,2500,5000,7500,10000,25000,50000,75000,100000]

dados_Insertion = [0.000002,0.000003,0.000015,0.000029,0.000056,0.000214,
         0.000665,0.001416,0.002529,0.017243,0.056830,0.125450,
         0.226864,1.381288,5.432714,12.330618,22.930238]

dados_bubble = [0.000006, 0.000020, 0.000057, 0.000094, 0.000237, 0.001510,
         0.004262, 0.008453, 0.014843, 0.040041, 0.128084, 0.290784,
         0.526207, 3.337507, 13.393707, 30.671931, 54.459569]

#Criando grafico Geral insertionSort

plt.rcParams['figure.figsize'] = (10,8)
plt.xlabel('n')
plt.ylabel('s')
plt.xlim(0,100000)
plt.ylim(0,25)
plt.title("Insertion Sort : Tempo decorrido na ordenacao")
plt.plot(condicoes, dados_Insertion, 'r')
plt.show()

#Criando grafico Geral bubbleSort

plt.rcParams['figure.figsize'] = (10,8)
plt.xlabel('n')
plt.ylabel('s')
plt.xlim(0,100000)
plt.ylim(0,25)
plt.title("Bubble Sort : Tempo decorrido na ordenacao")
plt.plot(condicoes, dados_bubble)
plt.show()

# Gráficos sobrepostos

plt.rcParams['figure.figsize'] = (10,8)
plt.xlabel('n')
plt.ylabel('s')
plt.xlim(0,100000)
plt.ylim(0,25)
plt.title("Insertion Sort versus Bubble Sort")
plt.plot(condicoes, dados_Insertion)
plt.plot(condicoes, dados_bubble)
plt.show()
