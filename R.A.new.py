data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
WC = {}
for d in data:
	words = d.strip().split(' ')
	for word in words:
		if word in WC:
			WC[word] += 1
		else:
			WC[word] = 1
for word in WC:
	if WC[word] > 1000000:
		print(word, WC[word])

while True:
	vocab = input('你要查的英文單字: ')
	if vocab in WC:
		print(WC[vocab])
	elif vocab == 'qq':
		break
	else:
		print('沒有，滾開!')
print('世界再見')
































#print('算完了，共有', len(data), '筆資料')
#sum_data = 0
#for d in data:
#	sum_data += len(d)
#print('平均長度是', sum_data / len(data))#