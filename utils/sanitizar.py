import unicodedata

def sanitizar(name):
    """
    Limpia y normaliza el input del usuario: convierte a minúsculas,
    elimina tildes, diéresis, cambia 'ñ' por 'n' y quita prefijos comunes.
    """
    # 1. Convertir a minúsculas, quitar espacios y signos de interrogación
    name = name.lower().strip().replace("?", "").replace("¿", "")
    
    # 2. Reemplazar 'ñ' antes de quitar marcas diacríticas
    name = name.replace("ñ", "n")
    
    # 3. Eliminar tildes y diéresis (normalización NFD)
    name = "".join(
        c for c in unicodedata.normalize("NFD", name)
        if unicodedata.category(c) != "Mn"
    )
    
    # 4. Lista de prefijos a omitir para aislar el sujeto de búsqueda
    prefixes = [
        "dime ", "cual es ", "el ", "la ", "de ", "en ",
        "accion ", "precio de ", "precio ", "stock de ", "stock ",
        "valor de ", "valor ", "clima ", "temperatura ", "tiempo ",
        "actual "
    ]
    
    changed = True
    while changed:
        changed = False
        for p in prefixes:
            if name.startswith(p):
                name = name[len(p):].strip()
                changed = True
                
    return name