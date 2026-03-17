"""
ZIP Code Lookup Tool
Returns the ZIP code(s) for a U.S. town given its name and 2-letter state abbreviation.
Uses the free Zippopotam.us API — no API key required.
"""

import urllib.request
import json
import sys


def get_zip_codes(city: str, state: str) -> list[str]:
    """
    Fetch ZIP code(s) for a given city and state abbreviation.

    Args:
        city:  City/town name (e.g. "Boston")
        state: 2-letter state abbreviation (e.g. "MA")

    Returns:
        A list of ZIP code strings, or raises an exception if not found.
    """
    # Normalize inputs
    city_encoded = urllib.parse.quote(city.strip())
    state_upper = state.strip().upper()

    url = f"https://api.zippopotam.us/us/{state_upper}/{city_encoded}"

    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                return [place["post code"] for place in data.get("places", [])]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise ValueError(
                f"No ZIP codes found for '{city}, {state_upper}'. "
                "Check the city name and state abbreviation."
            )
        raise RuntimeError(f"HTTP error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error: {e.reason}")

    return []


def main():
    import urllib.parse  # ensure it's available inside main too

    # --- Interactive mode ---
    if len(sys.argv) == 1:
        print("=== U.S. ZIP Code Lookup ===")
        city = input("Enter city/town name : ").strip()
        state = input("Enter 2-letter state  : ").strip()

    # --- Command-line mode: python zip_lookup.py "Boston" "MA" ---
    elif len(sys.argv) == 3:
        city = sys.argv[1]
        state = sys.argv[2]

    else:
        print("Usage: python zip_lookup.py <city> <state>")
        print("   or: python zip_lookup.py          (interactive)")
        sys.exit(1)

    try:
        zips = get_zip_codes(city, state)
        if zips:
            print(f"\nZIP code(s) for {city.title()}, {state.upper()}:")
            for z in zips:
                print(f"  {z}")
        else:
            print("No ZIP codes returned.")
    except (ValueError, RuntimeError) as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    import urllib.parse
    main()
