#Iteración por índice


my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

for index in range(0, len(my_favorite_records)):
	record = my_favorite_records[index]
	print(f'Record {index}: {record}')


#También se puede utilizar el ciclo while
my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

index = 0
while (index < len(my_favorite_records)):
	record = my_favorite_records[index]
	print(f'Record {index}: {record}')
	index += 1


my_favorite_records = [
	'Dark Side Of The Moon',
	'Fear of a Blank Planet',
	'Signify',
]

for index, record in enumerate(my_favorite_records):
	print(f'Record {index}: {record}')