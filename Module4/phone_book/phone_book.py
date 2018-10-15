# python2


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(raw_input())
    return [Query(raw_input().split()) for i in range(n)]

def write_responses(result):

    print('\n'.join(result))

def hash_num(phone_number):
    # implement hash function
    p = 10000019    # prime number exceeding number of combinations
    global m        # size of hash table
    a = 14          # hash function parameter
    b = 93

    return ((a*phone_number + b) % p) % m

def process_queries(queries):
    global m
    result = []
    contacts = [None]*m


    for cur_query in queries:
        hash_val = hash_num(cur_query.number)

        if cur_query.type == 'add':
            if contacts[hash_val] is None:
                contacts[hash_val] = {cur_query.number: cur_query.name}
            else:
                contacts[hash_val].update({cur_query.number: cur_query.name})

        elif cur_query.type == 'del':
            if contacts[hash_val] is not None:
                if cur_query.number in contacts[hash_val]:
                    contacts[hash_val].pop(cur_query.number)
                    if len(contacts[hash_val]) == 0:
                        contacts[hash_val] = None

        else:
            if (contacts[hash_val] is None) or (cur_query.number not in contacts[hash_val]):
                result.append('not found')
            else:
                result.append(contacts[hash_val][cur_query.number])

    return result


if __name__ == '__main__':
    m = 1000
    write_responses(process_queries(read_queries()))
    # process = psutil.Process(os.getpid())
    # print(process.get_memory_info()[0])
