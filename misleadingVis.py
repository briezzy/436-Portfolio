import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def make_misleadingVis(dataset_path):
    # Loading dataset
    df = pd.read_csv(os.path.join(dataset_path, 'books.csv'), quoting=3, on_bad_lines='skip')
    
    # Preview the data
    df.head()
    
    tick_positions = np.arange(1, 5.5, 0.5)
    
    tick_labels = ['' for _ in tick_positions]
    label_map = {4.0: 'Low', 4.5: 'Meh', 5.0: 'Perfect'}
    
    for i, val in enumerate(tick_positions):
        if val in label_map:
            tick_labels[i] = label_map[val]
    
    plt.xticks(tick_positions, tick_labels)
    
    plt.figure(figsize=(12, 6))
    
    plt.scatter(
        df['average_rating'],
        df['text_reviews_count'],
        s=df['ratings_count'] / 500,
        c=df['  num_pages'],
        cmap='plasma',
        alpha=0.9,
        edgecolors='black'
    )
    
    tick_positions = np.arange(1, 5.5, 0.5)
    
    tick_labels = ['' for _ in tick_positions]
    label_map = {4.0: 'Low', 4.5: 'Meh', 5.0: 'Perfect'}
    
    for i, val in enumerate(tick_positions):
        if val in label_map:
            tick_labels[i] = label_map[val]
    
    plt.title("Goodreads Books: Longer Books, Better Reviews", fontsize=16)
    plt.xlabel("Average Rating")
    plt.ylabel("Number of Text Reviews")
    
    plt.yscale('log')
    plt.xticks(np.arange(1, 5.5, 0.5), labels=['', '', '', 'Low', '', 'Meh', '', 'Perfect', ''])
    plt.yticks([10, 100, 1000, 10000, 100000])
    
    plt.grid(False)
    plt.colorbar(label="Number of Pages")
    
    plt.show()
