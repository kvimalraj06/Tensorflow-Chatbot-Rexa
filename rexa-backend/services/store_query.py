"""To save the new queries"""

def save(data):
    with open('queries.txt', 'a') as file:
        file.writelines("%s\n" % data)
    return