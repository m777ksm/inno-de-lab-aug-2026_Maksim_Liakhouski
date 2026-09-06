# Конфигурационный словарь, полученный от сервиса инициализации 
db_config = { 
    "connection": { 
        "host": "production-db.internal", 
        "port": 5432, 
        "user": "postgres" 
    } 
} 

# Достаем вложенный словарик
connection_dict = db_config.get("connection", {})

# 1. Извлекаем значения host и port из вложенного словаря connection
host = connection_dict.get("host")
port = connection_dict.get("port")
# или напрямую host = db_config.get("connection", {}).get("host")


# 2. Безопасная проверка ssl_settings и ssl_mode с дефолтным значением verify-full
ssl_mode = db_config.get("ssl_settings", {}).get("ssl_mode", "verify-full")

# 3. Изменяем значения пользователя на admin
connection_dict["user"] = "admin"

# 4. Добавляем новый параметр max_connections со значением 100
connection_dict["max_connections"] = 100

# 5. Вывод обновленного содержимого
print(f"SSL Mode: {ssl_mode}")
print("Параметры соединения:")
for k, v in connection_dict.items():
    print(f"* {k}: {v}")
