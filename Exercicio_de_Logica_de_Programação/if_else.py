
# Exemplo 1
idade = 20
print(f"Idade informada: {idade}")

if idade >= 18:
    print("Acesso permitido. Você é maior de idade.")

#Exemplo 2
idade = 16
print(f"Idade informada: {idade}")

if idade >= 18:
    print("Acesso permitido. Você é maior de idade.")
else:
    print("Acesso negado. Você é menor de idade.")

#Exemplo 3
nota = 75
print(f"Nota do aluno: {nota}")

if nota >= 90:
    print("Conceito: A")
elif nota >= 80:
    print("Conceito: B")
elif nota >= 70:
    print("Conceito: C")
elif nota >= 60:
    print("Conceito: D")
else:
    print("Conceito: F (Reprovado)")

#Exemplo 4
temperatura = 28
chovendo = False
print(f"Condições atuais -> Temperatura: {temperatura}°C, Chovendo: {chovendo}")

if temperatura > 25 and not chovendo:
    print("Sugestão: Ótimo dia para ir à praia!")
elif temperatura < 15 or chovendo:
    print("Sugestão: Que tal um filme em casa?")
else:
    print("Sugestão: O tempo está agradável.")
