q = 10

bin_rep = []
while q > 0 :
    bin_rep.append(q % 2)
    q = q / 2

bin_rep = bin_rep[::-1]
print bin_rep
