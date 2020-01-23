

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
print(list(x)[0])
print(list(x)[1])
print(x[list(x)[2]])	
