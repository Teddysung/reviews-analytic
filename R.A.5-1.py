data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('算完了，共有', len(data), '筆資料')
sum_data = 0
for d in data:
	sum_data += len(d)
print('平均長度是', sum_data / len(data))	