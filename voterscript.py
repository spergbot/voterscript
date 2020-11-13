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
    while True:
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'})
            if response.status_code == 200:
                break
        except Exception:
            print("Error... trying again")
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