# Список транзакций, полученных от платежного шлюза  
raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"]  

# Реализация фильтрации сумм успешных и положительных операций в одну строку List Comprehension 
filtered_transactions = [int(x.split(":")[1]) for x in raw_transactions if int(x.split(":")[1]) > 0 and x.split(":")[0] == "SUCCESS"]

# Вывод результата на экран
print(f"Очищенные транзакции: {filtered_transactions}")
