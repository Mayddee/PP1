import re
str = "snake_case"
#убирает нижние пробелы превращая в список, затем перепиcывает их с заглавной буквы и объединяет обратно
pattern7 = "".join(x.capitalize() or "_" for x in str.split("_"))
print(pattern7)