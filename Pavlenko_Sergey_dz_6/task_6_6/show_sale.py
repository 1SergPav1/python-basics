import sys

index = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as f:
	if len(index) == 1:
		start = int(index[0])
		finish = sum(1 for line in f)
		f.seek(0)
	elif len(index) > 1:
		start = int(index[0])
		finish = int(index[1])
		f.seek(0)
	else:
		start = 0
		finish = sum(1 for line in f)
		f.seek(0)

	for i, line in enumerate(f):
		if start <= i+1 <= finish:
			print(line)