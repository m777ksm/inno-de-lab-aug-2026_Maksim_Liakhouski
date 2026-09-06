# Поток данных телеметрии от серверов кластера 
system_telemetry = [ 
("srv_01", 12.5, 64, "online"), 
("srv_02", 85.0, 92, "online"), 
("srv_03", 0.0, 0, "offline"), 
("srv_04", 45.2, 78, "online"), 
("srv_05", 95.1, 99, "online") 
] 
# Реализация конвейера агрегации метрик 
# Распаковываем на node_name, cpu_load, ram_usage, status и только для активных
nodes = [node_name for node_name, cpu_load, ram_usage, status in system_telemetry if status != "offline"]
cpus = [cpu_load for node_name, cpu_load, ram_usage, status in system_telemetry if status != "offline"]
rams = [ram_usage for node_name, cpu_load, ram_usage, status in system_telemetry if status != "offline"]
statuses = [status for node_name, cpu_load, ram_usage, status in system_telemetry if status != "offline"]

# общее количество работающих серверов
active_nodes_count = len(nodes)

# средняя загрузка CPU с округлением до двух знаков
average_cpu = round(sum(cpus) / active_nodes_count, 2)

# пиковое значение использования оперативной памяти RAM
max_ram = max(rams)

# помещаем рассчитанные метрики в итоговый вложенный словарь
report = {
    'active_nodes_count': active_nodes_count,
    'metrics': {
        'average_cpu': average_cpu,
        'max_ram': max_ram}
}

# вывод результата
print(f"Активные узлы в сети: {nodes}")
print(f"Итоговый отчет телеметрии:")
print(report)
