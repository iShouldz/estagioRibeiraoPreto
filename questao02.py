def fibonacci_sequence(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

numero_procurado = int(input("Digite um número: "))

sequencia = fibonacci_sequence(numero_procurado)

if numero_procurado in sequencia:
    print(f"O número {numero_procurado} pertence à Fibonacci.")
else:
    print(f"O número {numero_procurado} não pertence à Fibonacci.")