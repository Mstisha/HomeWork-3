eng = 'qwertyuiopasdfghjklzxcvbnm'
rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'
points_eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
points_rus ={1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
word = input("Введите слово: ")
count = 0
if word[0].lower() in eng:
    for elem in word:
        for key, value in points_eng.items():
            if elem.upper() in value:
                count += key
    print(f'стоимость введенного английского слова = {count}')
else:
    if word[0].lower() in rus:
        for elem in word:
            for key, value in points_rus.items():
                if elem.upper() in value:
                    count += key
    print(f'стоимость введенного русского слова = {count}')