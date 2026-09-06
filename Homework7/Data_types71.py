# Исходная необработанная строка из источника данных  
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE " 

# 1. Разбить строку на отдельные элементы по точке с запятой
elements = raw_user_record.split(";")

# 2. Очистить каждый полученный элемент от ведущих и замыкающих пробельных символов. 
user_id = elements[0].strip()
name = elements[1].strip()
city = elements[2].strip()
status = elements[3].strip()

# 3. Применить к идентификатору пользователя префикс UID-
user_id = f"UID-{user_id}"

# 4. В имени пользователя меняем подчеркивание на пробел и каждое слово с заглавной 
name = name.replace("_"," ").title()

# 5. Привести название города к верхнему регистру. 
city = city.upper()

#6. Статус пользователя перевести в нижний регистр. 
status = status.lower()

# 7. Объединить элементы в одну строку с разделителем | и вывести 
new_user_record = " | ".join([user_id, name, city, status])
print(f"Нормализованная запись: {new_user_record}")
