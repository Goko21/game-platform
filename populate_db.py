from pymongo import MongoClient

client = MongoClient('mongodb+srv://gorkemerrr55:rSli7CuYAF9h0Dx2@gameplatform.ik3xjkw.mongodb.net/?retryWrites=true&w=majority&appName=GamePlatform')
db = client['game_platform']
users_col = db['users']
games_col = db['games']

# 10 User ekleyelim
usernames = [f"User{i}" for i in range(1, 11)]
for name in usernames:
    users_col.insert_one({
        "name": name,
        "total_play_time": 0,
        "average_rating": 0,
        "most_played_game": None,
        "played_games": {},
        "ratings": {},
        "comments": {}
    })

# 10 Game ekleyelim
games = [
    {"name": "Game A", "genres": ["Action", "Adventure"], "photo": "https://via.placeholder.com/150", "optional": {"release_date": "2021"}},
    {"name": "Game B", "genres": ["Puzzle"], "photo": "https://via.placeholder.com/150", "optional": {"developer": "DevB"}},
    {"name": "Game C", "genres": ["RPG"], "photo": "https://via.placeholder.com/150", "optional": {"requirements": "8GB RAM"}},
    {"name": "Game D", "genres": ["Shooter"], "photo": "https://via.placeholder.com/150"},
    {"name": "Game E", "genres": ["Sports"], "photo": "https://via.placeholder.com/150"},
    {"name": "Game F", "genres": ["Strategy"], "photo": "https://via.placeholder.com/150"},
    {"name": "Game G", "genres": ["Adventure"], "photo": "https://via.placeholder.com/150"},
    {"name": "Game H", "genres": ["Action"], "photo": "https://via.placeholder.com/150"},
    {"name": "Game I", "genres": ["RPG", "Adventure"], "photo": "https://via.placeholder.com/150"},
    {"name": "Game J", "genres": ["Racing"], "photo": "https://via.placeholder.com/150"},
]

for g in games:
    games_col.insert_one({
        "name": g["name"],
        "genres": g["genres"],
        "photo": g["photo"],
        "play_time": 0,
        "rating": 0,
        "rating_count": 0,
        "comments": [],
        "rating_enabled": True,
        "optional": g.get("optional", {})
    })

print("Başarıyla 10 kullanıcı ve 10 oyun eklendi!")
