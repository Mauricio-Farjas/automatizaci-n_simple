import requests
from utils.sanitizar import sanitizar

def obtener_clima(driver, user_input):
    """
    Obtiene la temperatura actual de una ciudad utilizando el servicio wttr.in.
    """
    city = sanitizar(user_input)
    
    if not city:
        return "Por favor especifica una ciudad para consultar el clima."

    try:
        response = requests.get(f"https://wttr.in/{city}?format=%t", timeout=10)
        
        if response.status_code == 200:
            temp = response.text.strip()
            return f"La temperatura actual en {city.title()} es {temp}"
        else:
            return f"No se pudo obtener el clima para '{city}'."
            
    except Exception as e:
        return f"Error de red al obtener el clima: {e}"