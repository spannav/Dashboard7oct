import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Load Data
df = pd.read_csv('video_game_sales.csv')
if 'coritic_scre' in df.columns:
    df.rename(columns={'coritic_scre': 'critic_score'}, inplace=True)

# Clean title: remove Prefix/ID like "Game___" or "Game X - "
df['clean_title'] = df['title'].str.replace(r'^Game\s*\d*\s*-\s*', '', regex=True)

# Initialize App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Global Video Game Sales & Market Analytics"

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Global Video Game Sales Analytics Dashboard"), className="mb-4 mt-4 text-center")
    ]),
    
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Executive Overview', value='tab-1'),
        dcc.Tab(label='Genre & Platform', value='tab-2'),
        dcc.Tab(label='Reviews vs Sales', value='tab-3'),
    ]),
    
    html.Div(id='tabs-content', className="mt-4")
], fluid=True)

def render_tab_1():
    return html.Div([
        dbc.Row([
            dbc.Col(dcc.Dropdown(
                id='t1-region-filter',
                options=[
                    {'label': 'Global', 'value': 'global_sales'},
                    {'label': 'North America', 'value': 'na_sales'},
                    {'label': 'Europe', 'value': 'eu_sales'},
                    {'label': 'Japan', 'value': 'jp_sales'},
                    {'label': 'Other', 'value': 'other_sales'}
                ],
                value='global_sales', clearable=False
            ), width=2),
            dbc.Col(dcc.Dropdown(
                id='t1-platform-filter',
                options=[{'label': p, 'value': p} for p in df['platform'].unique()],
                multi=True, placeholder="Select Platforms"
            ), width=3),
            dbc.Col(dcc.RangeSlider(
                id='t1-year-slider',
                min=df['release_year'].min(), max=df['release_year'].max(),
                value=[df['release_year'].min(), df['release_year'].max()],
                marks={str(year): str(year) for year in df['release_year'].unique()}, step=1
            ), width=5),
            dbc.Col(dbc.Button("Reset Filters", id="t1-reset-btn", color="danger", className="w-100"), width=2)
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardBody([html.H5("Global Total Sales", className="card-title"), html.H2(id='t1-kpi-sales')])), width=3),
            dbc.Col(dbc.Card(dbc.CardBody([html.H5("Total Game Titles", className="card-title"), html.H2(id='t1-kpi-titles')])), width=3),
            dbc.Col(dbc.Card(dbc.CardBody([html.H5("Top-Selling Genre", className="card-title"), html.H2(id='t1-kpi-genre')])), width=3),
            dbc.Col(dbc.Card(dbc.CardBody([html.H5("Top Console/Platform", className="card-title"), html.H2(id='t1-kpi-platform')])), width=3),
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col(dcc.Graph(id='t1-yearly-sales'), width=8),
            dbc.Col(dcc.Graph(id='t1-regional-breakdown'), width=4),
        ]),
        
        dbc.Row([
            dbc.Col(dcc.Graph(id='t1-top-games'), width=12)
        ])
    ])

def render_tab_2():
    return html.Div([
        dbc.Row([
            dbc.Col(dcc.Dropdown(
                id='t2-genre-filter',
                options=[{'label': g, 'value': g} for g in df['genre'].unique()],
                multi=True, placeholder="Select Genres"
            ), width=3),
            dbc.Col(dcc.Dropdown(
                id='t2-platform-filter',
                options=[{'label': p, 'value': p} for p in df['platform'].unique()],
                multi=True, placeholder="Select Platforms"
            ), width=3),
            dbc.Col(dcc.Dropdown(
                id='t2-publisher-filter',
                options=[{'label': p, 'value': p} for p in df['publisher'].unique()],
                multi=True, placeholder="Select Publishers"
            ), width=4),
            dbc.Col(dbc.Button("Reset Filters", id="t2-reset-btn", color="danger", className="w-100"), width=2)
        ], className="mb-4"),
        
        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardBody([
                html.H4("Most Published Genre", className="card-title text-primary"), 
                html.H1(id='t2-kpi-static-genre', className="display-4 font-weight-bold text-primary")
            ]), style={"border": "3px solid #0d6efd", "backgroundColor": "#f8f9fa", "height": "100%"}), width=6),
            dbc.Col(dbc.Card(dbc.CardBody([html.H5("Leading Publisher", className="card-title"), html.H2(id='t2-kpi-publisher')]), style={"height": "100%"}), width=3),
            dbc.Col(dbc.Card(dbc.CardBody([html.H5("Global Market Volume", className="card-title"), html.H2(id='t2-kpi-volume')]), style={"height": "100%"}), width=3),
        ], className="mb-4 align-items-stretch"),
        
        dbc.Row([
            dbc.Col(dcc.Graph(id='t2-heatmap'), width=6),
            dbc.Col(dcc.Graph(id='t2-treemap'), width=6),
        ]),
        
        dbc.Row([
            dbc.Col(dcc.Graph(id='t2-total-sales-bar'), width=12)
        ])
    ])

def render_tab_3():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.P("📌 หมายเหตุ: ตัวกรองช่วงคะแนนวิจารณ์ เพื่อเจาะลึกเฉพาะกลุ่มเกมเกรด A (90+), B (80-89) หรือกลุ่มทั่วไป", className="text-muted small"),
                dcc.RangeSlider(
                    id='t3-score-slider',
                    min=0, max=100, step=1, value=[0, 100],
                    marks={i: str(i) for i in range(0, 101, 10)},
                    vertical=True, verticalHeight=300
                ),
                html.Br(),
                html.P("📌 หมายเหตุ: ตัวกรองเรตติ้งความเหมาะสมเนื้อหา (E, E10+, T, M) เพื่อดูการกระจายตัวตามกลุ่มอายุเป้าหมาย", className="text-muted small"),
                dcc.Checklist(
                    id='t3-esrb-filter',
                    options=[{'label': str(i), 'value': str(i)} for i in df['esrb_rating'].dropna().unique()],
                    value=df['esrb_rating'].dropna().unique().tolist(),
                    inline=False
                )
            ], width=2),
            dbc.Col([
                html.P("📌 หมายเหตุ: ตัวกรองช่วงปีวางจำหน่าย เพื่อวิเคราะห์วิวัฒนาการของคะแนนวิจารณ์และพฤติกรรมผู้เล่นตามยุคสมัย", className="text-muted small"),
                dcc.RangeSlider(
                    id='t3-year-slider',
                    min=df['release_year'].min(), max=df['release_year'].max(),
                    value=[df['release_year'].min(), df['release_year'].max()],
                    marks={str(year): str(year) for year in df['release_year'].unique()}, step=1,
                    vertical=True, verticalHeight=300
                )
            ], width=2),
            dbc.Col([
                                dbc.Row([
                    dbc.Col(dcc.Dropdown(
                        id='t3-genre-filter',
                        options=[{'label': g, 'value': g} for g in df['genre'].unique()],
                        multi=True, placeholder="Select Genres"
                    ), width=9),
                    dbc.Col(dbc.Button("Reset Filters", id="t3-reset-btn", color="danger", className="w-100"), width=3)
                ], className="mb-4"),
                
                dbc.Row([
                    dbc.Col(dbc.Card(dbc.CardBody([html.H5("Avg Critic Score", className="card-title"), html.H2(id='t3-kpi-critic')])), width=4),
                    dbc.Col(dbc.Card(dbc.CardBody([html.H5("Avg User Score", className="card-title"), html.H2(id='t3-kpi-user')])), width=4),
                    dbc.Col(dbc.Card(dbc.CardBody([html.H5("Hit Games Count (>1M)", className="card-title"), html.H2(id='t3-kpi-hit')])), width=4),
                ], className="mb-4"),
                
                dbc.Row([
                    dbc.Col(dcc.Graph(id='t3-score-tiers-bar'), width=12)
                ])
            ], width=8)
        ]),
        
        dbc.Row([
            dbc.Col(dcc.Graph(id='t3-top-rated-bar'), width=12)
        ]),
        
        dbc.Row([
            dbc.Col(dcc.Graph(id='t3-score-compare-bar'), width=12)
        ]),
        
        dbc.Row([
            dbc.Col(dcc.Graph(id='t3-esrb-regional-bar'), width=6),
            dbc.Col(dcc.Graph(id='t3-esrb-heatmap'), width=6)
        ]),
    ])

@app.callback(Output('tabs-content', 'children'), Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1': return render_tab_1()
    elif tab == 'tab-2': return render_tab_2()
    elif tab == 'tab-3': return render_tab_3()

@app.callback(
    [Output('t1-kpi-sales', 'children'), Output('t1-kpi-titles', 'children'),
     Output('t1-kpi-genre', 'children'), Output('t1-kpi-platform', 'children'),
     Output('t1-yearly-sales', 'figure'), Output('t1-regional-breakdown', 'figure'),
     Output('t1-top-games', 'figure')],
    [Input('t1-region-filter', 'value'), Input('t1-platform-filter', 'value'),
     Input('t1-year-slider', 'value'), Input('t1-yearly-sales', 'selectedData')]
)
def update_tab_1(region, platforms, year_range, yearly_selected):
    f_df = df[(df['release_year'] >= year_range[0]) & (df['release_year'] <= year_range[1])].copy()
    if platforms: f_df = f_df[f_df['platform'].isin(platforms)]
    
    yearly_sales = f_df.groupby('release_year')[region].sum().reset_index()
    fig_yearly = px.line(
        yearly_sales, x='release_year', y=region, 
        title=f'Yearly Global Sales Trend<br><sup style="font-size:12px; color:gray">แสดงการเปรียบเทียบระหว่าง ปีที่วางจำหน่าย กับ ยอดขายรวมทั่วโลก ($M USD) เพื่อดูแนวโน้มการเติบโตและยุคทองของอุตสาหกรรมเกม</sup>',
        labels={'release_year': 'Release Year', region: 'Global Sales ($M USD)'}
    )
    fig_yearly.update_traces(mode='lines+markers')
    fig_yearly.update_layout(clickmode='event+select', margin=dict(t=80))
    
    if yearly_selected and yearly_selected['points']:
        selected_years = [p['x'] for p in yearly_selected['points']]
        f_df = f_df[f_df['release_year'].isin(selected_years)]
        year_label = " (Selected Years)"
    else:
        year_label = ""
        
    total_sales = f"${f_df[region].sum():,.2f}M USD"
    total_titles = f"{len(f_df):,} Titles"
    
    if not f_df.empty:
        top_genre_val = f_df.groupby('genre')[region].sum().idxmax()
        top_genre_sales = f_df.groupby('genre')[region].sum().max()
        top_genre = f"{top_genre_val} (${top_genre_sales:,.2f}M USD)"
        
        top_plat_val = f_df.groupby('platform')[region].sum().idxmax()
        top_plat_sales = f_df.groupby('platform')[region].sum().max()
        top_platform = f"{top_plat_val} (${top_plat_sales:,.2f}M USD)"
    else:
        top_genre = "N/A"
        top_platform = "N/A"
    
    regions = ['na_sales', 'eu_sales', 'jp_sales', 'other_sales']
    melted = f_df.melt(id_vars=['genre'], value_vars=regions, var_name='Region', value_name='Sales')
    regional_genre_sums = melted.groupby(['Region', 'genre'])['Sales'].sum().reset_index()
    fig_regional = px.bar(
        regional_genre_sums, x='Region', y='Sales', color='genre', barmode='stack',
        title=f'Regional Sales Breakdown{year_label}<br><sup style="font-size:12px; color:gray">แสดงการเปรียบเทียบระหว่าง ภูมิภาคหลัก ซ้อนทับตาม หมวดหมู่เกม (Genre) เพื่อดูสัดส่วนยอดขายและความนิยม</sup>',
        labels={'Sales': 'Sales ($M USD)', 'genre': 'Genre'}
    )
    fig_regional.update_layout(margin=dict(t=80))
    
    if not f_df.empty:
        top_games = f_df.groupby('clean_title')[regions].sum().sum(axis=1).nlargest(10).index
        top_games_df = f_df[f_df['clean_title'].isin(top_games)].groupby('clean_title')[regions].sum().reset_index()
        top_games_melted = top_games_df.melt(id_vars=['clean_title'], value_vars=regions, var_name='Region', value_name='Sales')
        total_order = top_games_df.set_index('clean_title').sum(axis=1).sort_values(ascending=True).index
    else:
        top_games_melted = pd.DataFrame(columns=['clean_title', 'Region', 'Sales'])
        total_order = []
        
    fig_top_games = px.bar(
        top_games_melted, x='Sales', y='clean_title', color='Region', orientation='h', barmode='stack',
        title=f'Top 10 Best-Selling Games{year_label}<br><sup style="font-size:12px; color:gray">แสดงการเปรียบเทียบระหว่าง 10 อันดับเกมที่ขายดีที่สุด กับ ยอดขายจำแนกตามภูมิภาค เพื่อดูความนิยมของเกมระดับ Blockbuster</sup>',
        labels={'Sales': 'Global Sales ($M USD)', 'clean_title': 'Game Title'}
    )
    fig_top_games.update_layout(yaxis={'categoryorder':'array', 'categoryarray': total_order}, margin=dict(t=80))
    
    return total_sales, total_titles, top_genre, top_platform, fig_yearly, fig_regional, fig_top_games

@app.callback(
    [Output('t2-kpi-static-genre', 'children'), Output('t2-kpi-publisher', 'children'),
     Output('t2-kpi-volume', 'children'), Output('t2-heatmap', 'figure'),
     Output('t2-treemap', 'figure'), Output('t2-total-sales-bar', 'figure')],
    [Input('t2-genre-filter', 'value'), Input('t2-platform-filter', 'value'), Input('t2-publisher-filter', 'value'),
     Input('t2-heatmap', 'clickData')]
)
def update_tab_2(genres, platforms, publishers, heatmap_click):
    f_df = df.copy()
    if not df.empty:
        static_top_genre = df['genre'].value_counts().index[0]
        static_top_count = df['genre'].value_counts().iloc[0]
        static_most_pub_genre = f"{static_top_genre} ({static_top_count:,} Titles)"
    else:
        static_most_pub_genre = "N/A"
    
    if genres: f_df = f_df[f_df['genre'].isin(genres)]
    if platforms: f_df = f_df[f_df['platform'].isin(platforms)]
    if publishers: f_df = f_df[f_df['publisher'].isin(publishers)]
        
    heatmap_data = f_df.pivot_table(index='genre', columns='platform', values='global_sales', aggfunc='sum').fillna(0)
    fig_heatmap = px.imshow(
        heatmap_data, 
        title='Genre vs. Platform Sales (Click to filter)<br><sup style="font-size:12px; color:gray">แสดงการเปรียบเทียบระหว่าง หมวดหมู่เกม กับ แพลตฟอร์มเครื่องเล่น โดยใช้ระดับสีวัด ยอดขายรวม เพื่อหาจุดจับคู่ที่ทำรายได้สูงสุด</sup>',
        labels=dict(x="Platform", y="Genre", color="Global Sales ($M USD)")
    )
    fig_heatmap.update_layout(margin=dict(t=80))
    
    click_label = ""
    if heatmap_click:
        clicked_genre = heatmap_click['points'][0]['y']
        clicked_platform = heatmap_click['points'][0]['x']
        f_df = f_df[(f_df['genre'] == clicked_genre) & (f_df['platform'] == clicked_platform)]
        click_label = f" (Filtered: {clicked_genre} & {clicked_platform})"
        
    if not f_df.empty:
        top_pub = f_df.groupby('publisher')['global_sales'].sum().idxmax()
        top_pub_sales = f_df.groupby('publisher')['global_sales'].sum().max()
        leading_pub = f"{top_pub} (${top_pub_sales:,.2f}M USD)"
    else:
        leading_pub = "N/A"
        
    total_volume = f"${f_df['global_sales'].sum():,.2f}M USD"
    
    fig_treemap = px.treemap(
        f_df, path=[px.Constant("All"), 'publisher', 'genre'], values='global_sales',
        title=f'Publisher Market Share{click_label}<br><sup style="font-size:12px; color:gray">แสดงการเปรียบเทียบสัดส่วน ส่วนแบ่งการตลาดของค่ายผู้พัฒนา กับ ยอดขายรวม ($M USD) เพื่อดูค่ายเกมที่เป็นผู้นำในตลาด</sup>'
    )
    fig_treemap.update_layout(margin=dict(t=80))
    
    sales_by_genre = f_df.groupby('genre').agg(total=('global_sales', 'sum')).reset_index()
    fig_total = px.bar(
        sales_by_genre.sort_values('total', ascending=False), x='genre', y='total',
        title=f'Total Sales by Genre{click_label}<br><sup style="font-size:12px; color:gray">แสดงการเปรียบเทียบระหว่าง หมวดหมู่เกม (Genre) กับ ยอดขายรวม ($M USD) เรียงลำดับจากมากไปน้อย เพื่อดูมูลค่าตลาดของแต่ละประเภทเกม</sup>',
        labels={'total': 'Global Sales ($M USD)', 'genre': 'Genre'}
    )
    fig_total.update_layout(margin=dict(t=80))
    
    return static_most_pub_genre, leading_pub, total_volume, fig_heatmap, fig_treemap, fig_total

@app.callback(
    [Output('t3-kpi-critic', 'children'), Output('t3-kpi-user', 'children'),
     Output('t3-kpi-hit', 'children'), Output('t3-score-tiers-bar', 'figure'),
     Output('t3-top-rated-bar', 'figure'), Output('t3-score-compare-bar', 'figure'),
     Output('t3-esrb-regional-bar', 'figure'), Output('t3-esrb-heatmap', 'figure')],
    [Input('t3-score-slider', 'value'), Input('t3-genre-filter', 'value'), Input('t3-year-slider', 'value'),
     Input('t3-esrb-filter', 'value'), Input('t3-score-tiers-bar', 'clickData')]
)
def update_tab_3(score_range, genres, year_range, esrb_ratings, tier_click):
    f_df = df[(df['critic_score'] >= score_range[0]) & (df['critic_score'] <= score_range[1]) &
              (df['release_year'] >= year_range[0]) & (df['release_year'] <= year_range[1])].copy()
    if genres: f_df = f_df[f_df['genre'].isin(genres)]
    if esrb_ratings: f_df = f_df[f_df['esrb_rating'].isin(esrb_ratings)]
    
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
        title='Average Sales by Review Score Tiers (Click to filter)<br><sup style="font-size:12px; color:gray">แสดงการเปรียบเทียบระหว่าง กลุ่มช่วงคะแนนรีวิว กับ ยอดขายเฉลี่ยต่อเกม ($M USD/Game) เพื่อประเมินว่าเกมคะแนนสูงขายได้ดีกว่าจริงหรือไม่</sup>',
        labels={'global_sales': 'Avg Sales per Title ($M USD)', 'score_tier': 'Review Score Tier'}
    )
    fig_tiers.update_layout(xaxis={'categoryorder':'array', 'categoryarray': category_order}, margin=dict(t=80))
    
    click_label = ""
    if tier_click:
        clicked_tier = tier_click['points'][0]['x']
        f_df = f_df[f_df['score_tier'] == clicked_tier]
        click_label = f" (Tier: {clicked_tier})"
        
    avg_critic = f"{f_df['critic_score'].mean():.1f} Points" if not f_df.empty else "N/A"
    avg_user = f"{f_df['user_score'].mean():.1f} Points" if not f_df.empty else "N/A"
    hit_count = f"{len(f_df[f_df['global_sales'] > 1]):,} Titles"
    
    grouped_df = f_df.groupby('clean_title').agg({'critic_score': 'mean', 'global_sales': 'sum'}).reset_index()
    top_rated = grouped_df.nlargest(10, 'critic_score')
    
    fig_top_rated = px.bar(
        top_rated, x='critic_score', y='clean_title', orientation='h', range_x=[0, 100],
        title=f'Top 10 Best Rated Games{click_label}<br><sup style="font-size:12px; color:gray">แสดง 10 อันดับเกมที่ได้คะแนนนักวิจารณ์สูงสุด เทียบกับ คะแนนรีวิว (Points)</sup>',
        labels={'critic_score': 'Critic Score (Points)', 'clean_title': 'Game Title'}
    )
    fig_top_rated.update_layout(yaxis={'categoryorder':'total ascending'}, margin=dict(t=80))
    
    f_df['scaled_user_score'] = f_df['user_score'] * 10
    genre_scores = f_df.groupby('genre')[['critic_score', 'scaled_user_score']].mean().reset_index()
    genre_scores = genre_scores.rename(columns={'critic_score': 'Critic Score', 'scaled_user_score': 'User Score'})
    
    fig_compare = px.line(
        genre_scores, x='genre', y=['Critic Score', 'User Score'],
        title=f'Critic vs. User Score Comparison Chart by Genre{click_label}<br><sup style="font-size:12px; color:gray">แสดงการเปรียบเทียบระหว่าง คะแนนเฉลี่ยจากนักวิจารณ์ (Critic Score) และ คะแนนเฉลี่ยจากผู้เล่น (User Score) ในแต่ละหมวดหมู่เกม (Genre) เพื่อดูความสอดคล้องของรสนิยม</sup>',
        color_discrete_map={'Critic Score': 'blue', 'User Score': 'red'},
        markers=True,
        labels={'value': 'Average Score (Points)', 'genre': 'Genre', 'variable': 'Score Type'}
    )
    fig_compare.update_layout(yaxis_range=[0, 100], margin=dict(t=80))

    regions = ['na_sales', 'eu_sales', 'jp_sales', 'other_sales']
    esrb_regional = f_df.groupby('esrb_rating')[regions].sum().reset_index()
    esrb_regional_melted = esrb_regional.melt(id_vars=['esrb_rating'], value_vars=regions, var_name='Region', value_name='Sales')
    
    fig_esrb_regional = px.bar(
        esrb_regional_melted, x='esrb_rating', y='Sales', color='Region', barmode='stack',
        title=f'Regional Market Preference by ESRB Rating{click_label}<br><sup style="font-size:12px; color:gray">แสดงสัดส่วนเปอร์เซ็นต์ยอดขายรายภูมิภาค จำแนกตามเรตติ้งความเหมาะสมเนื้อหา (ESRB Rating)</sup>',
        labels={'Sales': 'Percentage Share (%)', 'esrb_rating': 'ESRB Rating'}
    )
    fig_esrb_regional.update_layout(barnorm='percent', margin=dict(t=80))
    
    heatmap_esrb_data = f_df.pivot_table(index='genre', columns='esrb_rating', values='global_sales', aggfunc='sum').fillna(0)
    fig_esrb_heatmap = px.imshow(
        heatmap_esrb_data, 
        title=f'Genre x ESRB Sales Matrix{click_label}<br><sup style="font-size:12px; color:gray">แสดงความเข้มข้นของยอดขายรวม ($M USD) ระหว่างแนวเกม (Genre) เทียบกับเรตติ้งเนื้อหา (ESRB Rating)</sup>',
        labels=dict(x="ESRB Rating", y="Genre", color="Global Sales ($M USD)")
    )
    fig_esrb_heatmap.update_layout(margin=dict(t=80))
    
    return avg_critic, avg_user, hit_count, fig_tiers, fig_top_rated, fig_compare, fig_esrb_regional, fig_esrb_heatmap


@app.callback(
    [Output('t1-region-filter', 'value'), Output('t1-platform-filter', 'value'), Output('t1-year-slider', 'value')],
    Input('t1-reset-btn', 'n_clicks'),
    prevent_initial_call=True
)
def reset_tab1(n_clicks):
    return 'global_sales', [], [df['release_year'].min(), df['release_year'].max()]

@app.callback(
    [Output('t2-genre-filter', 'value'), Output('t2-platform-filter', 'value'), Output('t2-publisher-filter', 'value')],
    Input('t2-reset-btn', 'n_clicks'),
    prevent_initial_call=True
)
def reset_tab2(n_clicks):
    return [], [], []

@app.callback(
    [Output('t3-score-slider', 'value'), Output('t3-esrb-filter', 'value'), 
     Output('t3-year-slider', 'value'), Output('t3-genre-filter', 'value')],
    Input('t3-reset-btn', 'n_clicks'),
    prevent_initial_call=True
)
def reset_tab3(n_clicks):
    return [0, 100], df['esrb_rating'].dropna().unique().tolist(), [df['release_year'].min(), df['release_year'].max()], []

if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)
