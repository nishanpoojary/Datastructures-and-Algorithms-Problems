class Query:
    def __init__(self, query):
        self.request = query[0]
        self.number = query[1]
        if self.request == "add":
            self.name = query[2]

def process_query(query, phone_book):
    if query.request == "add":
        phone_book[query.number] = query.name
    elif query.request == "del":
        if phone_book.__contains__(query.number):
            del phone_book[query.number]
    else:
        response = "not found"
        if phone_book.__contains__(query.number):
            return phone_book[query.number]
        return response
    

def main():
    n_requests = int(input())
    phone_book = {}
    results = []
    
    for _ in range(n_requests):
        query = Query(input().split())
        result = process_query(query, phone_book)
        if result:
            results.append(result)
            
    print(*results, sep="\n")
        
if __name__ == "__main__":
    main()