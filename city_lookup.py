"""
City Lookup Tool
Returns the city/town name and state for a U.S. ZIP code.
Uses the free Zippopotam.us API — no API key required.
"""

import urllib.request
import urllib.error
import json
import sys


def get_city_from_zip(zip_code: str) -> dict:
    """
    Fetch city/town info for a given U.S. ZIP code.

    Args:
        zip_code: 5-digit U.S. ZIP code (e.g. "02101")

    Returns:
        A dict with keys: 'zip', 'city', 'state', 'state_abbr', 'country'
        Raises ValueError if not found, RuntimeError on network issues.
    """
    zip_code = zip_code.strip()

    if not zip_code.isdigit() or len(zip_code) != 5:
        raise ValueError(f"'{zip_code}' is not a valid 5-digit ZIP code.")

    url = f"https://api.zippopotam.us/us/{zip_code}"

    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                places = data.get("places", [])
                if not places:
                    raise ValueError(f"No city found for ZIP code {zip_code}.")
                place = places[0]
                return {
                    "zip":        data.get("post code"),
                    "city":       place.get("place name"),
                    "state":      place.get("state"),
                    "state_abbr": place.get("state abbreviation"),
                    "country":    data.get("country"),
                }
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise ValueError(
                f"No city found for ZIP code '{zip_code}'. "
                "Make sure it's a valid U.S. ZIP code."
            )
        raise RuntimeError(f"HTTP error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error: {e.reason}")


def main():
    # --- Interactive mode ---
    if len(sys.argv) == 1:
        print("=== U.S. City Lookup by ZIP Code ===")
        zip_code = input("Enter 5-digit ZIP code: ").strip()

    # --- Command-line mode: python city_lookup.py 02101 ---
    elif len(sys.argv) == 2:
        zip_code = sys.argv[1]

    else:
        print("Usage: python city_lookup.py <zip_code>")
        print("   or: python city_lookup.py          (interactive)")
        sys.exit(1)

    try:
        result = get_city_from_zip(zip_code)
        print(f"\nZIP Code : {result['zip']}")
        print(f"City     : {result['city']}")
        print(f"State    : {result['state']} ({result['state_abbr']})")
        print(f"Country  : {result['country']}")
    except (ValueError, RuntimeError) as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
