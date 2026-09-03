# Список ролей, переданный в запросе на авторизацию (содержит повторы) 
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]

# Набор обязательных ролей для выполнения административных функций 
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# Преобразуем список запрошенных ролей во множество для удаления дубликатов
unique_roles = set(requested_roles)

# Определяем роли, которые одновременно в списке уникальных и обязательных
same_roles = unique_roles.intersection(required_admin_roles)

# Вычисляем недостающие административные роли, которых нет в уникальных
different_roles = required_admin_roles.difference(unique_roles)

# наличие роли security_officer в дедуплицированном множестве
sec_officer_exist = "security_officer" in unique_roles

# Вывод результатов
print(f"Уникальные запрошенные роли: {unique_roles}")
print(f"Общие административные роли: {same_roles}")
print(f"Недостающие административные роли: {different_roles}")
print(f"Наличие роли security_officer в запросе: {sec_officer_exist}")
