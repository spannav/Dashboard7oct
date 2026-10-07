import re

with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace render_tab_3
render_tab_3_new = """def render_tab_3():
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
                    ), width=12)
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
        
        dbc.Row([
            dbc.Col(dcc.Graph(id='t3-esrb-line'), width=12)
        ])
    ])"""

content = re.sub(r'def render_tab_3\(\):.*?@app\.callback', render_tab_3_new + '\n\n@app.callback', content, flags=re.DOTALL)


update_tab_3_new = """@app.callback(
    [Output('t3-kpi-critic', 'children'), Output('t3-kpi-user', 'children'),
     Output('t3-kpi-hit', 'children'), Output('t3-score-tiers-bar', 'figure'),
     Output('t3-top-rated-bar', 'figure'), Output('t3-score-compare-bar', 'figure'),
     Output('t3-esrb-regional-bar', 'figure'), Output('t3-esrb-heatmap', 'figure'),
     Output('t3-esrb-line', 'figure')],
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
    
    esrb_genre_sales = f_df.groupby(['genre', 'esrb_rating'])['global_sales'].sum().reset_index()
    fig_esrb_line = px.line(
        esrb_genre_sales, x='genre', y='global_sales', color='esrb_rating', markers=True,
        title=f'ESRB Content Rating Sales Dynamics across Genres{click_label}<br><sup style="font-size:12px; color:gray">เปรียบเทียบระดับความสูงของยอดขายรวม ($M USD) ในแต่ละแนวเกม (Genre) แยกตามเส้นระดับเรตติ้งเนื้อหา (ESRB Rating)</sup>',
        labels={'global_sales': 'Global Sales ($M USD)', 'genre': 'Genre', 'esrb_rating': 'ESRB Rating'}
    )
    fig_esrb_line.update_layout(margin=dict(t=80))
    
    return avg_critic, avg_user, hit_count, fig_tiers, fig_top_rated, fig_compare, fig_esrb_regional, fig_esrb_heatmap, fig_esrb_line

if __name__ == '__main__':"""

content = re.sub(r'@app\.callback\(\n\s*\[Output\(\'t3-kpi-critic\'.*?if __name__ == \'__main__\':', update_tab_3_new + '\n    app.run(debug=True)\n', content, flags=re.DOTALL)

with open("app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Patch successful!")
