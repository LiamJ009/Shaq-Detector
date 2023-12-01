a = ([[[[1.0000000e+00, 2.2869939e-11]]], [[[9.9987149e-01, 1.2844359e-04]]]])

print(a[0][0][0][1])

print(a[1][0][0][1])

# print(a)

max_score = 0
index = 0

for i in a:

    if i[0][0][1] > max_score:
        max_score = i[0][0][1]
        index = a.index(i)

print(a[index][0][0])
print(a)
