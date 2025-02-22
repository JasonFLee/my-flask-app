import requests

# Hardcoded API keys (not recommended for production)
GOOGLE_API_KEY = "AIzaSyB9yEX0j13MD26ZaetGtOzZyiLIc3hquxM"
SERPAPI_KEY = "3bf5dbf320c7931522416ea558ae4c26c7ff9d23bc00476ba80d31ee9bbb0b68"

def get_hidden_gems():
    lat, lon = "40.7128", "-74.0060"  # NYC Coordinates
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=hidden+gem&location={lat},{lon}&radius=20000&key={GOOGLE_API_KEY}"
    response = requests.get(url).json()
    
    places = []
    for place in response.get("results", []):
        name = place.get("name", "Unknown Place")
        address = place.get("formatted_address", "No address available")
        rating = place.get("rating", "No rating")
        total_ratings = place.get("user_ratings_total", 0)
        
        # Build a photo URL if a photo is available
        photo_url = ""
        photos = place.get("photos", [])
        if photos:
            photo_ref = photos[0].get("photo_reference", "")
            if photo_ref:
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_ref}&key={GOOGLE_API_KEY}"
        
        formatted = (
            f"{name}\n"
            f"  Address: {address}\n"
            f"  Rating: ⭐ {rating} ({total_ratings} reviews)"
        )
        if photo_url:
            formatted += f"\n  Photo: {photo_url}"
        places.append(formatted)
    return places

def get_atlas_obscura_places():
    city = "New York"
    url = f"https://serpapi.com/search.json?q=site:atlasobscura.com+unique+places+in+{city}&api_key={SERPAPI_KEY}"
    response = requests.get(url).json()
    
    places = []
    for result in response.get("organic_results", []):
        title = result.get("title", "No title")
        link = result.get("link", "")
        thumbnail = result.get("thumbnail", "")
        
        formatted = f"{title}\n  Link: {link}"
        if thumbnail:
            formatted += f"\n  Thumbnail: {thumbnail}"
        places.append(formatted)
    return places

if __name__ == "__main__":
    print("📍 Testing with Fixed NYC Location: New York (40.7128, -74.0060)\n")
    
    google_places = get_hidden_gems()
    if google_places:
        print("🌍 Hidden Gems from Google Places:")
        for place in google_places:
            print("  -", place, "\n")
    else:
        print("❌ No unique places found on Google Places.\n")
    
    atlas_places = get_atlas_obscura_places()
    if atlas_places:
        print("📜 Unique Places from Atlas Obscura:")
        for place in atlas_places:
            print("  -", place, "\n")
    else:
        print("❌ No results from Atlas Obscura.\n")
