from calendar import c


rule = input("Règle initiale : ")
rule = rule.replace("[i+1]","[(i+1)%size[1]]")
rule = rule.replace("[j+1]","[(j+1)%size[0]]")
rule = rule.replace("[(i+1)%size[0]]","[(i+1)%size[1]]")
rule = rule.replace("[(j+1)%size[1]]","[(j+1)%size[0]]")
print("\n==================\n")
print(rule)


# 000 = 0
# 001 = 1
# 010 = 1
# 011 = 1
# 100 = 0
# 101 = 1
# 110 = 1
# 111 = 0

# c\ab | 00 | 01 | 11 | 10
#   0  | 0  | 1  | 1  | 0
#   1  | 1  | 1  | 0  | 1

# !a . c + b . !c + !b . c
# c . (!a + !b) + b . !c
# (gen[i+1] and (!gen[i-1] or !gen[i])) or (gen[i] and !gen[i+1])
# gen[i-1]^(gen[i]|gen[(i+1)%size[0]])