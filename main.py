import re


with open("server.log.2018-04-05") as file:
    for line in file:
        line = file.readline()
        result = re.search("WFLYSRV"
                           ".*OS signal", line)
        if result:
            print(line)
