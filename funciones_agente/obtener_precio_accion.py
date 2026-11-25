import requests
from utils.sanitizar import sanitizar

COMPANY_TICKERS = {
    "microsoft": "MSFT",
    "apple": "AAPL",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "amazon": "AMZN",
    "tesla": "TSLA",
    "meta": "META",
    "facebook": "META",
    "netflix": "NFLX",
    "nvidia": "NVDA",
    "apple inc": "AAPL",
    "microsoft corp": "MSFT",
    "tesla motors": "TSLA"
}

def obtener_precio_accion(driver, user_input):
    """
    Consulta el precio actual y la divisa de una acción usando la API pública de Yahoo Finance.
    Compatible con driver=None o con una instancia de Selenium.
    """
    company_name = sanitizar(user_input)
    ticker = COMPANY_TICKERS.get(company_name, company_name.upper())

    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return f"No se pudo obtener información para el ticker '{ticker}'."

        data = response.json()
        result = data.get("chart", {}).get("result")

        if not result:
            return f"No se encontraron datos de cotización para '{ticker}'."

        meta = result[0].get("meta", {})
        price = meta.get("regularMarketPrice")
        currency = meta.get("currency", "USD")

        if price is not None:
            return f"El precio actual de {ticker} es ${price:.2f} {currency}"
        else:
            return f"Precio no disponible en este momento para {ticker}."

    except Exception as e:
        return f"Error al consultar el precio de la acción: {e}"