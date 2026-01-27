import requests
import urllib.parse

def geocoding(location, key):
    if location.strip() == "":
        print("Empty location.")
        return None

    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})

    r = requests.get(url)
    if r.status_code != 200:
        print("Geocoding error (check API key).")
        return None

    data = r.json()
    if len(data.get("hits", [])) == 0:
        print("No geocoding results for:", location)
        return None

    hit = data["hits"][0]
    lat = hit["point"]["lat"]
    lng = hit["point"]["lng"]
    name = hit.get("name", "")
    state = hit.get("state", "")
    country = hit.get("country", "")
    print(f"{name}, {state}, {country}")
    return (lat, lng)

def route_with_instructions(start_coords, dest_coords, vehicle, key):
    route_url = "https://graphhopper.com/api/1/route?"
    params = {
        "point": [f"{start_coords[0]},{start_coords[1]}", f"{dest_coords[0]},{dest_coords[1]}"],
        "vehicle": vehicle,
        "locale": "en",
        "instructions": "true",
        "key": key
    }

    url = route_url + urllib.parse.urlencode(params, doseq=True)
    r = requests.get(url)

    if r.status_code != 200:
        print("Route error:")
        print(r.text)
        return

    data = r.json()
    distance_km = data["paths"][0]["distance"] / 1000
    time_min = data["paths"][0]["time"] / 1000 / 60

    print(f"\nVehicle: {vehicle}")
    print(f"Distance: {distance_km:.2f} km")
    print(f"Travel time: {time_min:.2f} minutes\n")

    print("Directions:")
    instructions = data["paths"][0]["instructions"]
    for i, ins in enumerate(instructions, start=1):
        text = ins.get("text", "")
        dist_m = ins.get("distance", 0)
        time_s = ins.get("time", 0)
        print(f"{i}. {text} ({dist_m:.0f} m, {time_s/60:.1f} min)")

def choose_vehicle():
    while True:
        v = input("Vehicle (car/bike/foot) [car]: ").strip().lower()
        if v == "":
            return "car"
        if v in ["car", "bike", "foot"]:
            return v
        print("Invalid vehicle. Choose car, bike, or foot.")

# ===== MAIN =====
key = "e80044c5-d279-47c1-9b6e-b189ff1d7f09"

while True:
    start = input("Starting Location (or 'q' to quit): ")
    if start.lower() == "q":
        break

    dest = input("Destination (or 'q' to quit): ")
    if dest.lower() == "q":
        break

    vehicle = choose_vehicle()

    print("\nGeocoding start:")
    start_coords = geocoding(start, key)

    print("\nGeocoding destination:")
    dest_coords = geocoding(dest, key)

    if start_coords and dest_coords:
        route_with_instructions(start_coords, dest_coords, vehicle, key)

    print("\n---\n")
