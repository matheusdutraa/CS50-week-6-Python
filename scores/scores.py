from cs50 import get_int

scores = []

# A funcao "append()" Adiciona elementos a lista
# Funcao built-in
for i in range(3):
    score = get_int("Score: ")
    scores.append(score)
    # scores += [score]

# A funcao "sum()" soma os valores do dicionario
# A funcao "len()" conta o numero de elementos do dicionario
average = sum(scores) / len(scores)

print(f"Average: {average}")