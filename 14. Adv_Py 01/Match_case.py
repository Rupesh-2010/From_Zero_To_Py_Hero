def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not found"
        case 500:
            return "Intrnal Server Error."
        case _:
            return "Unknown"

#Uses
    
# 
    
print(http_status(000000000))
