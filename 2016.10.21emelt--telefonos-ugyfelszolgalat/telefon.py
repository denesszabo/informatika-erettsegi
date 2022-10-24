# Importáljuk a pprint parancsot szebb print kimenetekért
from pprint import pprint

print('2016. okt. 21 Emelt érettségi: Telefonos ügyfélszolgálat')


# 1. feladat: mbpe() függvény.
def mpbe(o, p, mp: int) -> int:
	### print(o, p, mp, sep='\n')
	return o * 3600 + p * 60 + mp


# 2. feladat: File beolvasás, feldolgozás
calls = []
f = open("hivas.txt", "r")
for row in f:
	# A beolvasott sor végéről a \n levágva, majd ' ' mentén törve.
	row = row.strip().split()  # ['6', '51', '8', '6', '54', '58']
	### pprint(row)
	# Az összes lista elem egésszé konvertálása.
	row = [x for x in row]  # ['6', '51', '8', '6', '54', '58']
	row = [int(x) for x in row]  # [6, 51, 8, 6, 54, 58]
	### pprint(row)
	
	custom_row = {
		'call_start_hour': row[0],
		'call_start': mpbe(*row[:3]),  # [6, 51, 8] => 6, 51, 8
		'call_end': mpbe(*row[3:])
	}
	
	custom_row['call_length'] = custom_row['call_end'] - custom_row['call_start']
	
	calls.append(custom_row)

f.close()

# calls = calls[:50]
pprint(calls, None, 4)

print('3. feladat: óránkénti hívás statisztika')
call_stat = {}
for call in calls:
	print(call)
	hour = call['call_start_hour']
	if hour not in call_stat:
		# Nem volt még az óra a statisztikában, hozzáadjuk
		call_stat[hour] = 1
	else:
		# Volt már az óra, csak növelni kell az értéket
		call_stat[hour] += 1

# Hivas statisztika kiírása.
for hour in call_stat:
	print(f'{hour} ora {call_stat[hour]} hivas')

print('4. feladat: A leghosszabb hívás')
longest_call = -1
longest_call_line = -1
for line in range(0, len(calls)):
	call = calls[line]
	if call['call_length'] > longest_call:
		longest_call = call['call_length']
		longest_call_line = line
		
# Eredmények kiíratása. A sorszámhoz hozzá kell adni egyet, a lista 0-tól számozódik
# de a sorokat 1-től számozzuk.
print(f'A leghosszabb ideig vonalban levo hivo {longest_call_line + 1}. sorban szerepel, a hivas hossza: {longest_call} masodperc.')

print('4. feladat v2: A leghosszabb hívás')
longest_call = max(calls, key=lambda call: call['call_length'])
longest_call_line = calls.index(longest_call) + 1
longest_call = longest_call['call_length']

print(f'A leghosszabb ideig vonalban levö hívó {longest_call_line}. sorban szerepel, a hivas hossza: {longest_call} masodperc.')


print('\n5. feladat: Hányadik hívó\n------')

'''
time = input("Adjon meg egy idöpontot! (ora perc masodperc) :")
'''
# Gyors input, fix érték.
time = '10 11 12'
# time = '8 0 0'  # A varakozok szama: 3 a beszelo a 96. hivo.
# time = '9 14 45'  # Nem volt beszélő.
time = [int(x) for x in time.split()]
time = mpbe(*time)

print('A kérdéses időpont', time, sep=':')

filtered_calls = []
for call in calls:
	# ha a vége van a hívásnak az időpont elott, akkor jöhet a következő hívás
	# ezzel nincs dolog
	if call['call_end'] < time:
		continue;
	
	# Ha a hívás kezdete az idő után van, akkor innentől már csak
	# lényegtelen sorok vannak, bátran kiléphetünk a ciklusból
	if call['call_start'] > time:
		break
	
	# nem kell több vizsgálat, a hívás az időpont kürül van
	filtered_calls.append(call)
	
	# Másik lehetséges megoldás, minden sort átnézünk:
	# if call['call_start'] <= time <= call['call_end']:
	#	filtered_calls.append(call)

if filtered_calls:
	# Megkeressük az időpont körüli hívások legelső elemét a hívások között
	# +1-el korrigálni kell+
	
	line_in_call = calls.index(filtered_calls[0]) + 1
	# A várakozók száma az időpont körüli hívások -1, mert 1 hívásban van.
	print(f'A varakozok szama: {len(filtered_calls) - 1} a beszelo a {line_in_call}. hivo.')
else:
	print('Nem volt beszélő az adott időpontban.')
	
print(filtered_calls)
