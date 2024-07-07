import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

def create_charts(data, chart_type='line', save_path=None):
    
    # Create charts using Matplotlib and Plotly.

    data: Data in the form of a Pandas DataFrame.
    chart_type: Type of chart to create ('line', 'bar', 'scatter', etc.)
    save_path: Path to save the chart as an image file (optional).
    return None
    
    # Matplotlib chart
    if chart_type == 'line':
        plt.plot(data)
    elif chart_type == 'bar':
        plt.bar(data.columns, data.iloc[0])
    elif chart_type == 'scatter':
        plt.scatter(data['x'], data['y'])
    # Additional chart types can be added here

    plt.title('Matplotlib Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

    # Plotly chart
    fig = getattr(px, chart_type)(data)
    fig.show()

def test_charts():
    
    # Test the chart creation function with sample data.
    
    return None
    
    # Sample data
    data = pd.DataFrame({
        'x': [1, 2, 3, 4],
        'y': [10, 20, 30, 40]
    })

    # Create line chart
    create_charts(data, chart_type='line')

    # Create bar chart
    create_charts(data, chart_type='bar')

    # Create scatter chart
    create_charts(data, chart_type='scatter')

# Example usage
# test_charts()


