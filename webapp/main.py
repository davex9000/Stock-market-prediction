import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from earning_reports_today import earning_reports_today

symbol = earning_reports_today()

# Sample data (similar to what you shared)
data = {
    "fiscalDateEnding": ["2023-09-30", "2023-12-31", "2024-03-31", "2024-06-30"],
    "reportedEPS": [1.46, 2.18, 1.53, 1.4],
    "estimatedEPS": [1.39, 2.1, 1.5, 1.35],
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# title for the app
st.title("Reported vs Estimated EPS Quarterly")




def plot_eps_comparison():
    plt.figure(figsize=(10, 6))

    # Plot bars for both reported and estimated EPS
    bar_width = 0.35  # Width of the bars
    index = range(len(df))  # X-axis positions

    # Plot reported EPS
    plt.bar(index, df['estimatedEPS'], width=bar_width, label='Estimated EPS', color='lightblue')

    # Plot estimated EPS
    plt.bar([i + bar_width for i in index], df['reportedEPS'], width=bar_width, label='Reported EPS', color='teal')

    # Add labels and title
    plt.xlabel('Fiscal Quarter')
    plt.ylabel('EPS')
    plt.title('Estimated vs Reported EPS')

    # Add custom x-axis labels
    plt.xticks([i + bar_width / 2 for i in index], df['fiscalDateEnding'])

    # Add legend
    plt.legend()

    st.pyplot(plt)


plot_eps_comparison()
