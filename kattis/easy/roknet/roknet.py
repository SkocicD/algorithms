d = {}
for _ in range(int(input())):
    line = input().split()
    match line[0]:
        case "INNTAK":
            d[line[1]] = (line[2] == "SATT")
        case "UTTAK":
            print(line[1], 'SATT' if d[line[1]] else 'OSATT')
        case "OG":
            d[line[3]] = (d[line[1]] and d[line[2]])
        case "EDA":
            d[line[3]] = (d[line[1]] or d[line[2]])
        case "EKKI":
            d[line[2]] = (not d[line[1]])
