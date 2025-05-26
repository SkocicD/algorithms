from collections import defaultdict


class Rule:
    def __init__(self):
        self.ports = set()
        self.ips = set()
        self.limit = 0
        self.action = ""

    def checkip(self, ip):
        return self.ips == set() or ip in self.ips

    def checkport(self, port):
        return self.ports == set() or port in self.ports

    def checklimit(self, ip, ipcounts):
        return ipcounts[ip] >= self.limit


rules = []
for _ in range(int(input())):
    rules.append(Rule())
    conds = input().split()
    rule = rules[-1]
    rule.action = conds[0]

    for cond in conds[1:]:
        if "ip" in cond:
            rule.ips.add(cond[cond.index('=')+1:])
        elif "port" in cond:
            rule.ports.add(cond[cond.index('=')+1:])
        elif "limit" in cond:
            rule.limit = int(cond[cond.index('=')+1:])

last1000 = []
ipcounts = defaultdict(int)
for i in range(1, int(input())+1):
    ip, port = input().split(':')
    last1000.append(ip)
    if len(last1000) > 1000:
        ipremove = last1000.pop(0)
        ipcounts[ipremove] -= 1
    ipcounts[ip] += 1
    for rule in rules:
        if rule.checkip(ip) and rule.checkport(port) and rule.checklimit(ip, ipcounts):
            print(f'{rule.action} {i}')
            if rule.action != "log":
                break
