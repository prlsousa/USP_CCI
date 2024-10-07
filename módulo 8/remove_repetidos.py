def remove_repetidos(lista):
    new = []
    for item in lista:
        if not item in new:
            new.append(item)
    new.sort()
    return new
        
                
                
            
            
