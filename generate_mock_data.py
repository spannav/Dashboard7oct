import pandas as pd
import numpy as np
import random

def generate_mock_data(num_records=500):
    np.random.seed(42)
    random.seed(42)
    
    platforms = ['PS4', 'PS5', 'XOne', 'XSX', 'Switch', 'PC']
    genres = ['Action', 'Shooter', 'Role-Playing', 'Sports', 'Misc', 'Racing', 'Platform', 'Simulation']
    publishers = ['Nintendo', 'Electronic Arts', 'Activision', 'Sony Computer Entertainment', 'Ubisoft', 'Take-Two Interactive', 'Square Enix', 'Capcom']
    esrb = ['E', 'T', 'M', 'E10+']
    
    data = []
    for i in range(1, num_records + 1):
        platform = random.choice(platforms)
        genre = random.choice(genres)
        publisher = random.choice(publishers)
        release_year = random.randint(2013, 2024)
        
        # Base sales based on publisher and platform
        base_multiplier = 1.0
        if publisher == 'Nintendo' and platform == 'Switch':
            base_multiplier = 2.5
        elif publisher in ['Sony Computer Entertainment'] and platform in ['PS4', 'PS5']:
            base_multiplier = 2.0
            
        na_sales = max(0.01, np.random.lognormal(mean=0, sigma=1) * base_multiplier)
        eu_sales = max(0.01, np.random.lognormal(mean=-0.2, sigma=1) * base_multiplier)
        jp_sales = max(0.0, np.random.lognormal(mean=-1, sigma=1.2) * (2.0 if publisher == 'Nintendo' else 0.5))
        other_sales = max(0.0, np.random.lognormal(mean=-1, sigma=1) * base_multiplier)
        
        global_sales = na_sales + eu_sales + jp_sales + other_sales
        
        critic_score = np.clip(np.random.normal(loc=70 + (global_sales * 2), scale=12), 20, 99)
        user_score = np.clip(np.random.normal(loc=critic_score / 10, scale=1.5), 2.0, 9.9)
        
        rating = random.choice(esrb)
        if genre in ['Shooter'] and rating == 'E':
            rating = 'M'
            
        data.append({
            'game_id': i,
            'title': f'Game {i} - {genre} {platform}',
            'platform': platform,
            'release_year': release_year,
            'genre': genre,
            'publisher': publisher,
            'na_sales': round(na_sales, 2),
            'eu_sales': round(eu_sales, 2),
            'jp_sales': round(jp_sales, 2),
            'other_sales': round(other_sales, 2),
            'global_sales': round(global_sales, 2),
            'critic_score': round(critic_score, 1),
            'user_score': round(user_score, 1),
            'esrb_rating': rating
        })
        
    df = pd.DataFrame(data)
    df.to_csv('video_game_sales.csv', index=False)
    print("Mock data generated in 'video_game_sales.csv'")

if __name__ == '__main__':
    generate_mock_data()
