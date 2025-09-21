def status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "unknown status"
        case _:
            return "unknown status"
        
print(status(404))