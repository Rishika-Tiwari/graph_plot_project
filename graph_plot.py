import plotly.graph_objects as go

def plot_user_graph():
    # Get input from the user for x-values
    x_values_input = input("Enter a list of x-values separated by spaces: ")
    x_values = [float(x) for x in x_values_input.split()]

    # Get input from the user for y-values
    y_values_input = input("Enter a list of y-values separated by spaces: ")
    y_values = [float(y) for y in y_values_input.split()]

    # Create a scatter plot
    fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='markers+lines'))

    # Update layout
    fig.update_layout(
        title="User-Defined Graph",
        xaxis_title="X-axis",
        yaxis_title="Y-axis",
        showlegend=False
    )

    # Show the plot
    fig.show()

if __name__ == "__main__":
    plot_user_graph()


