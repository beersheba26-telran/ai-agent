def get_current_weather(city: str):
    """Get the current weather in a given city."""
    # For the sake of this example, we'll return a hardcoded weather report.
    return f"The current weather in {city} is sunny with a temperature of 25°C."
def get_exchange_rate(currency: str):
    """Get the current exchange rate for a given currency."""
    # For the sake of this example, we'll return a hardcoded exchange rate.
    return f"The current exchange rate for {currency} is 1.2 USD."

TOOLS = {
    "get_current_weather": get_current_weather  
}