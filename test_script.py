import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('video_game_sales.csv')
df['clean_title'] = df['title'].str.replace(r'^Game\s*\d*\s*-\s*', '', regex=True)

score_range = [0, 100]
genres = []
year_range = [df['release_year'].min(), df['release_year'].max()]
tier_click = None

f_df = df[(df['critic_score'] >= score_range[0]) & (df['critic_score'] <= score_range[1]) &
          (df['release_year'] >= year_range[0]) & (df['release_year'] <= year_range[1])].copy()
if genres: f_df = f_df[f_df['genre'].isin(genres)]

conditions = [
    (f_df['critic_score'] >= 90),
    (f_df['critic_score'] >= 80) & (f_df['critic_score'] < 90),
    (f_df['critic_score'] >= 70) & (f_df['critic_score'] < 80),
    (f_df['critic_score'] < 70)
]
choices = ['90-100 (Masterpiece)', '80-89 (Great)', '70-79 (Good)', 'Under 70 (Average/Poor)']
f_df['score_tier'] = np.select(conditions, choices, default='Unknown')

tier_sales = f_df.groupby('score_tier')['global_sales'].mean().reset_index()
category_order = ['90-100 (Masterpiece)', '80-89 (Great)', '70-79 (Good)', 'Under 70 (Average/Poor)']

fig_tiers = px.bar(
    tier_sales, x='score_tier', y='global_sales',
    title='Average Sales by Review Score Tiers',
    labels={'global_sales': 'Avg Sales per Title ( USD)', 'score_tier': 'Review Score Tier'}
)
fig_tiers.update_layout(xaxis={'categoryorder':'array', 'categoryarray': category_order}, margin=dict(t=80))

if tier_click:
    clicked_tier = tier_click['points'][0]['x']
    f_df = f_df[f_df['score_tier'] == clicked_tier]

avg_critic = f\"{f_df['critic_score'].mean():.1f} Points\" if not f_df.empty else 'N/A'
avg_user = f\"{f_df['user_score'].mean():.1f} Points\" if not f_df.empty else 'N/A'
hit_count = f\"{len(f_df[f_df['global_sales'] > 1]):,} Titles\"

grouped_df = f_df.groupby('clean_title').agg({'critic_score': 'mean', 'global_sales': 'sum'}).reset_index()

top_rated = grouped_df.nlargest(10, 'critic_score')
top_selling = grouped_df.nlargest(10, 'global_sales')

fig_top_rated = px.bar(
    top_rated, x='critic_score', y='clean_title', orientation='h', range_x=[0, 100],
    title='Top 10 Best Rated Games'
)

fig_top_selling = px.bar(
    top_selling, x='global_sales', y='clean_title', orientation='h',
    title='Top 10 Best Selling Games'
)

f_df['scaled_user_score'] = f_df['user_score'] * 10
genre_scores = f_df.groupby('genre')[['critic_score', 'scaled_user_score']].mean().reset_index()
genre_scores['Score Gap'] = genre_scores['critic_score'] - genre_scores['scaled_user_score']
genre_scores['color'] = np.where(genre_scores['Score Gap'] > 0, 'Critics Liked More (+)', 'Users Liked More (-)')

fig_compare = px.bar(
    genre_scores, x='genre', y='Score Gap', color='color'
)
print('SUCCESS')
