import re

with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Tab 1 Layout Modification
t1_row_old = """        dbc.Row([
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
            ), width=3),
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
            ), width=6)
        ], className="mb-4"),"""

t1_row_new = """        dbc.Row([
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
        ], className="mb-4"),"""

content = content.replace(t1_row_old, t1_row_new)

# Tab 2 Layout Modification
t2_row_old = """        dbc.Row([
            dbc.Col(dcc.Dropdown(
                id='t2-genre-filter',
                options=[{'label': g, 'value': g} for g in df['genre'].unique()],
                multi=True, placeholder="Select Genres"
            ), width=4),
            dbc.Col(dcc.Dropdown(
                id='t2-platform-filter',
                options=[{'label': p, 'value': p} for p in df['platform'].unique()],
                multi=True, placeholder="Select Platforms"
            ), width=4),
            dbc.Col(dcc.Dropdown(
                id='t2-publisher-filter',
                options=[{'label': p, 'value': p} for p in df['publisher'].unique()],
                multi=True, placeholder="Select Publishers"
            ), width=4)
        ], className="mb-4"),"""

t2_row_new = """        dbc.Row([
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
        ], className="mb-4"),"""

content = content.replace(t2_row_old, t2_row_new)

# Tab 3 Layout Modification
content = re.sub(r"dbc\.Row\(\[\s*dbc\.Col\(dcc\.Dropdown\(\s*id='t3-genre-filter',.*?width=12\)\s*\], className=\"mb-4\"\),", 
"""                dbc.Row([
                    dbc.Col(dcc.Dropdown(
                        id='t3-genre-filter',
                        options=[{'label': g, 'value': g} for g in df['genre'].unique()],
                        multi=True, placeholder="Select Genres"
                    ), width=9),
                    dbc.Col(dbc.Button("Reset Filters", id="t3-reset-btn", color="danger", className="w-100"), width=3)
                ], className="mb-4"),""", content, flags=re.DOTALL)

# Remove t3-esrb-line from render_tab_3
content = re.sub(r"\s*dbc\.Row\(\[\s*dbc\.Col\(dcc\.Graph\(id='t3-esrb-line'\), width=12\)\s*\]\)", "", content)

# Remove t3-esrb-line from update_tab_3 Outputs
content = content.replace("Output('t3-esrb-regional-bar', 'figure'), Output('t3-esrb-heatmap', 'figure'),\n     Output('t3-esrb-line', 'figure')", "Output('t3-esrb-regional-bar', 'figure'), Output('t3-esrb-heatmap', 'figure')")

# Remove t3-esrb-line logic from update_tab_3
esrb_line_logic = """    esrb_genre_sales = f_df.groupby(['genre', 'esrb_rating'])['global_sales'].sum().reset_index()
    fig_esrb_line = px.line(
        esrb_genre_sales, x='genre', y='global_sales', color='esrb_rating', markers=True,
        title=f'ESRB Content Rating Sales Dynamics across Genres{click_label}<br><sup style="font-size:12px; color:gray">เปรียบเทียบระดับความสูงของยอดขายรวม ($M USD) ในแต่ละแนวเกม (Genre) แยกตามเส้นระดับเรตติ้งเนื้อหา (ESRB Rating)</sup>',
        labels={'global_sales': 'Global Sales ($M USD)', 'genre': 'Genre', 'esrb_rating': 'ESRB Rating'}
    )
    fig_esrb_line.update_layout(margin=dict(t=80))
    
    return avg_critic, avg_user, hit_count, fig_tiers, fig_top_rated, fig_compare, fig_esrb_regional, fig_esrb_heatmap, fig_esrb_line"""

esrb_line_replacement = """    return avg_critic, avg_user, hit_count, fig_tiers, fig_top_rated, fig_compare, fig_esrb_regional, fig_esrb_heatmap"""

content = content.replace(esrb_line_logic, esrb_line_replacement)


# Append Reset Callbacks
reset_callbacks = """
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
"""

content = content.replace("if __name__ == '__main__':", reset_callbacks + "\nif __name__ == '__main__':")


with open("app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Patch round 7 applied!")
