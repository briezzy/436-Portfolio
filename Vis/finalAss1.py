import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import plotly.express as px
import os

def make_finalAss1(dataset_path):
    # Loading dataset
    df = pd.read_csv(os.path.join(dataset_path, 'Top 500 Movies.csv'))
    
    df.columns = df.columns.str.strip()
    
    df = df.rename(columns={
        'title': 'title',
        'worldwide gross (m)': 'gross'
    })
    
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['gross'] = pd.to_numeric(df['gross'], errors='coerce')
    df = df.dropna(subset=['title', 'year', 'gross', 'decade'])
    palette = {
        "1970's": '#A9A9A9',
        "1980's": '#BDB76B',
        "1990's": '#20B2AA',
        "2000's": '#008B8B',
        "2010's": '#9370DB',
        "2020's": '#00CED1',
    }
    
    
    # Preview the data
    df.head()
    
    
    # Plot setup
    sns.set(style="whitegrid")
    plt.figure(figsize=(16, 9))
    
    sns.scatterplot(
        data=df,
        x='year',
        y='gross',
        hue='decade',
        palette=palette,
        s=80,
        edgecolor='black',
        alpha=0.7
    )
    
    for decade in df['decade'].unique():
        top = df[df['decade'] == decade].sort_values(by='gross', ascending=False).head(1)
        for _, row in top.iterrows():
            plt.text(row['year'], row['gross'] + 50, row['title'],
                     fontsize=9, ha='center', weight='bold')
    
    plt.title('Top 500 Hollywood Movies by Worldwide Box Office Gross', fontsize=20)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Worldwide Gross ($M)', fontsize=14)
    
    plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${int(x):,}')) # Now mticker is defined and can be used
    
    plt.legend(title='Decade', title_fontsize=12, fontsize=10, loc='upper left')
    
    plt.tight_layout()
    plt.show()
  
