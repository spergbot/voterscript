import requests

file = open('Michigan_registered_voters_old_index.txt', 'r')
dead = open("dead.txt", 'w')
alive = open("alive.txt", 'w')
file.readline()
dead_count = 0 
alive_count = 0
line = file.readline()
while line:
    [firstname, lastname, year, zipcode] = line.split(',')
    url = "https://obits.mlive.com/obituaries/annarbor/obituary-search.aspx?daterange=99999&firstname=%s&lastname=%s&keyword=%s&countryid=1&stateid=26&affiliateid=all"%(firstname,lastname,year)
    response = requests.get(url)
    while (response.status_code != 200):
        response = requests.get(url)
    content = str(response.content)
    if "did not find any obituaries in this newspaper." not in content:
        print(firstname, lastname + " IS DEAD.")
        dead.write("%s %s\n"%(firstname, lastname))
        dead_count += 1
    else:
        print(firstname, lastname + " IS ALIVE.")
        alive.write("%s %s\n"%(firstname, lastname))
        alive_count += 1
    line = file.readline()
dead.write(str(dead_count))
alive.write(str(alive_count))
print()
print("{} DEAD, {} ALIVE".format(dead_count, alive_count))

file.close()
dead.close()
alive.close()