# Importáljuk a pprint parancsot szebb print kimenetekért
from pprint import pprint

# 4/1. Adatok beolvasása
files = ['konnyu', 'kozepes', 'nehez']
file_name = files[2]
file_name = files[1]
file_name = files[0]

# Be kellenene kérni az adatokat.
row_num = 1
col_num = 3
# le kell ellenőrizni, hogy a határon belöl van-e. 1-9


# 4/2. feladat, fájl beolvasás, eltárolás
matrix = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
]
fill_data = []
index = 0
f = open(file_name + ".txt", "r")
idx = 1
for row in f:
    row = row.strip().split() # string feldolgozás, listává konvertálás
    row = [int(x) for x in row] # lista elemek integerré konvertálása
    
    if (idx <= 9):
        # a matrix elemeinek elmentese
        # a sor sorszámának beillesztése a sor elejére.
        row.insert(0, idx)
        matrix.append(row)
    else:
        # kitöltés adatok
        fill_data.append(row)
    idx += 1
f.close()

# Tablazat kiírása
print('4. feladat')
print(f'A {file_name}.txt adatok apalján a táblázat elemei:')
print('---------------------')
pprint(matrix)
print('---------------------')
print ('Kitöltés adatok')
pprint(fill_data)
print('---------------------')

print('4/3. feladat: sor, oszlop helyek ellenőrzése')

# Az adott szám - oszlop vagy sor tartomány ellenőrzése
def check_input(num):
    if 0 < num < 10:
        return True
    print(f'{num} tartományon kívül, hibás adat!')
    return False


def get_matrix_element(row, column):
    if (not check_input(row)) or (not check_input(column)):
        print('Hibás mátrix tartomány!')
        return -1
    
    return matrix[row][column]


# a matrix résztáblázat szám kiszámolása
def get_matrix_area_number(row, column):
    # sorok kiszámolása - 0, 1, 2
    crow = ((row-1) // 3)
    # oszlopok kiszámolása: 0, 1, 2
    ccol = ((column-1) // 3)

    # résztáblázat: sorok száma (1 sorban 3) + oszlopok
    # +1 mert nem 0-val kezdjük a számozást
    return crow * 3 + ccol + 1


# Ellenorizni az összes adatot, mi van benn a táblázatban.
for data in fill_data:
    # pprint(data)
    row = data[1]
    column = data[2]
    value = get_matrix_element(row, column)
    area_number = get_matrix_area_number(row, column)
    if value < 0:
        # hibas adat jott vissza
        print(f'A {row}. sor és {column}. oszlop megadott érték hibás')
        # ugrás a következő fill_data-ra, nem kell tovább ellenőrizni semmit
        continue
    
    if value == 0:
        print(f'A {row}. sor és {column}. oszlop helyet még nem töltötték ki.')
    else:
        print(f'A {row}. és {column}. értékének megfelelő hely {value} értéket tartalmaz.')
        
    print(f'A {row}. sor és {column}. oszlop a {area_number} résztáblázathoz tartozik')

print('---------------------')
print('4/4. feladat: táblázat százalékos kitöltésének ellenőrzése')
print('---------------------')
not_filled = 0
for row in range(1, 9):
    # row a sorváltozó
    for column in range(1, 9):
        # column az oszlopváltozó
        value = get_matrix_element(row, column)
        if value == 0:
            # számoljuk a nem kitöltötteket
            not_filled += 1
            
print(f'A táblázatban {not_filled} mező nincs kitöltve.')
szazalek = "{:.1f}".format(not_filled)
print(f'A táblázatban a mezők {szazalek}%-a nincs kitöltve.')

print('---------------------')
print('4/5. feladat: lehetséges lépések ellenőrzése')
print('---------------------')


# Minden sor érték visszaadása
def get_row_values(row):
    # az első, sort jelző érték kivételével a sor értékek visszadása
    values = matrix[row][1:]

    # print('sorok:')
    # print(values)
    
    return values


# Minden oszlop érték visszaadása
def get_column_values(column):
    values = []
    # az első, oszlop sorszámot jelző érték kivételével az oszlop értékek visszadása
    for i in range(1, 9):
        values.append(matrix[i][column])
    # print('oszlopok:')
    # print(values)
    return values


def get_submatrix_values(area_number):
    values = []
    row_start = ((area_number -1) // 3) * 3 + 1
    #print(f'row: {row_start}:{row_start+2}')
    
    col_start = ((area_number -1) % 3) * 3 + 1
    # print(f'col: {col_start} : {col_start + 2}')

    for row in range(row_start, row_start + 3):
        # tesz, soronként hozzáadni
        # values.append(matrix[row][col_start:col_start + 3])
        for col in range(col_start, col_start + 3):
            values.append(matrix[row][col])
    return values


# Ellenorizni az összes adatot, mi van benn a táblázatban.
for data in fill_data:
    # pprint(data)
    new_value = data[0]
    row = data[1]
    column = data[2]
    value = get_matrix_element(row, column)
    area_number = get_matrix_area_number(row, column)
    print(f'{row}. sor és {column}. oszlop ellenőrzése. A szám {new_value}.')
    if value == 0:
        # A hely üres (0)
        print(f'A hely üres, nincs még adat a mezőben, további ellenőrzés szükséges')
        values = get_row_values(row)
        if new_value in values:
            # Az új érték szerepel már a sorban
            print(f'Az adott sorban már szerepel a szám')
        else:
            values = get_column_values(column)
            if new_value in values:
                # Az új érték szerepel már az oszlopban
                print(f'Az adott oszlopban már szerepel a szám')
            else:
                # részmátrix értékek ellenőrzése
                values = get_submatrix_values(area_number)
                if new_value in values:
                    # Az új érték szerepel már az oszlopban
                    print(f'Az adott résztáblázatban már szerepel a szám')
                
                else:
                    print('A lépés megtehető.')
    else:
        msg = 'A helyet már kitöltötték.'
        if value == new_value:
            msg += ' Az adott sorban már szerepel a szám'
        else:
            msg += ' Az adott sorban már szerepel szám.'
        print(msg)
        
        
print('---------------------')
# fills = [
#     [1, 1],
#     [1, 5],
#     [1, 8],
#     [1, 9],
#     [4, 4],
#     [6, 2],
#     [1, 2],
#     [9, 9],
# ]
# for d in fills:
#     row = d[0]
#     column = d[1]
#     print(f'{row}, {column}')
#     area_number = get_matrix_area_number(row, column)
#     values = get_submatrix_values(area_number)
#     pprint(values)