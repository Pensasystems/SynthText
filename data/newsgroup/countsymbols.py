import sys
fname = 'newsgroup.txt'
with open(fname) as f:
	lines = f.readlines()
symbols = set()
for line in lines:
	for word in line:
		for ch in word:
			symbols.add(ch)
print(len(symbols))
print(symbols)	
