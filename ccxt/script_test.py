# project creation aiming to develop crypto strategies 

# get data from binance via ccxt


#structure of the project
# folder data: where are stored for analysis
#  


"""

file header
File: strat_name.py
Author: Farid Bouakline
Date Created: 2024-12-
Last Modified: --
Description: example :use machine learning to detect reversion of price.
"""


import pandas as pd
import matplotlib.pyplot as plt

def plot_combo_chart(df, bar_column, line_column, x_column=None, title='Combined Bar and Line Chart',
                    bar_color='skyblue', line_color='red', figsize=(12, 6)):
    """
    Create a combination of bar and line chart using matplotlib.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Input DataFrame containing the data
    bar_column : str
        Name of the column to be plotted as bars
    line_column : str
        Name of the column to be plotted as line
    x_column : str, optional
        Name of the column to be used for x-axis. If None, uses DataFrame index
    title : str, optional
        Title of the plot
    bar_color : str, optional
        Color for the bars
    line_color : str, optional
        Color for the line
    figsize : tuple, optional
        Figure size as (width, height)
    """
    
    # Create figure and axis objects
    fig, ax1 = plt.subplots(figsize=figsize)
    
    # Define x-axis values
    x = df[x_column] if x_column else df.index
    x_pos = range(len(x))
    
    # Plot bars
    bars = ax1.bar(x_pos, df[bar_column], color=bar_color, alpha=0.7)
    ax1.set_xlabel('Time Period')
    ax1.set_ylabel(bar_column, color=bar_color)
    ax1.tick_params(axis='y', labelcolor=bar_color)
    
    # If x_column is provided, set x-ticks
    if x_column:
        ax1.set_xticks(x_pos)
        ax1.set_xticklabels(x, rotation=45)
    
    # Create second y-axis and plot line
    ax2 = ax1.twinx()
    line = ax2.plot(x_pos, df[line_column], color=line_color, linewidth=2, 
                    marker='o', label=line_column)
    ax2.set_ylabel(line_column, color=line_color)
    ax2.tick_params(axis='y', labelcolor=line_color)
    
    # Add title
    plt.title(title)
    
    # Add legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(bars, [bar_column], loc='upper left')
    ax2.legend(lines2, labels2, loc='upper right')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    return fig, (ax1, ax2)

# Example usage with sample data
if __name__ == "__main__":
    # Create sample data
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
        'Sales': [100, 120, 140, 130, 150, 160, 140, 150, 170, 180, 175, 190],
        'Growth': [5, 8, 12, 9, 11, 13, 8, 10, 15, 16, 14, 18]
    }
    df = pd.DataFrame(data)
    
    # Create the plot
    fig, axes = plot_combo_chart(
        df=df,
        bar_column='Sales',
        line_column='Growth',
        x_column='Date',
        title='Monthly Sales and Growth Rate',
        bar_color='skyblue',
        line_color='red',
        figsize=(12, 6)
    )
    
    # Show the plot
    plt.show()