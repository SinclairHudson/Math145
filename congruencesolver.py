ring=26
solutions = []
for x in range(ring):
    if((x**2)%ring==10):
        solutions.append(x)
print(solutions)
