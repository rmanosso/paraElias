import numpy as np
from pynfft.nfft import NFFT
plan = NFFT([16, 16], 92)
print(plan.M)

#Domínio do Linograma
def lino_H(M,N):
    x = []
    y = []
    for I in range(-M//2 , M//2):
        for J in range(-N//4 +1, N//4 +1):
            x.append((2*np.pi * I)/M)
            y.append(((2*np.pi*I)/M ) * ((4 * J)/N))
    return(x,y)


def lino_V(M,N):
    x = []
    y = []
    for I in range(-M//2 + 1, M//2 + 1):
        for J in range(-N//4 , N//4):
            y.append((2*np.pi * I)/M)
            x.append(((2*np.pi*I)/M ) * ((4 * J)/N))
    return(x,y)

# Definir o tamanho da matriz m por n
m, n = 4, 4 # Por exemplo, uma matriz 4x4

# Gerar a parte real e a parte imaginária separadamente, com valores aleatórios
parte_real = np.random.rand(m, n)  # Valores reais aleatórios entre 0 e 1
parte_imaginaria = np.random.rand(m, n)  # Valores imaginários aleatórios entre 0 e 1

# Combinar para criar uma matriz complexa
x = np.array(parte_real + 1j * parte_imaginaria)

print('Exibir a matriz')
print(x)

import matplotlib.pyplot as plt

xi_h, nu_h = lino_H(m, n)
xi_v, nu_v = lino_V(m, n)

plt.scatter(xi_h, nu_h)
plt.scatter(xi_v, nu_v)
# Adicionando rótulos aos eixos e título
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Pontos (x, y)')

# Exibindo o gráfico
plt.show()

print('xi_h, nu_v')
print(xi_h, nu_h)
print('xi_v, nu_v')
print(xi_v, nu_v )


xi_h = np.array(xi_h)
nu_h = np.array(nu_h)
xi_v = np.array(xi_v)
nu_v = np.array(nu_v)
print('xi_h, nu_v - em array')
print(xi_h, nu_h)
print('xi_v, nu_v - em array')
print(xi_v, nu_v )

def DTFT(x, xi, nu):
    m, n = x.shape
    x_result = np.zeros(len(xi), dtype=complex)
    for k in range(len(xi)):
        for i in range(m):
            for j in range(n):
                x_result[k] += x[i][j] * np.exp(-1j*(j*xi[k] + i*nu[k]))
    return x_result

print('Aplicando a DTFT no domínio')
print(DTFT(x, xi_h, nu_h))
print(DTFT(x, xi_v, nu_v))

#result_pynfft = pynfft(4, 4, xi_h)

#result_pynfft = pynfft(4, 4, xi_h)