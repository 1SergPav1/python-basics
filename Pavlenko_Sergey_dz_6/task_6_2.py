# Задание № 2

with open('nginx_logs.txt', encoding='utf-8') as f:
    ip_dict = {}
    for line in f:
        ip_dict.setdefault(line.split()[0], 0)
        ip_dict[line.split()[0]] += 1

ip_dict = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)
print(ip_dict[0])
