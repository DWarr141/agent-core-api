"""Weather services for the application."""
import httpx


async def get_weather() -> str:
    """Fetch the current weather for Salt lake city."""
    url = "https://wttr.in/Salt+Lake+City?format=3"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.text.strip()
        except httpx.HTTPError as e:
            return f"Error fetching weather: {e}"