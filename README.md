# Comprehensive Data Insights: Financial and Election Analysis Tool

## Description
This project consists of two Python scripts designed to perform detailed analysis on large datasets. The first script analyzes financial data to provide insights into budget trends, while the second script analyzes election data to determine voter preferences and election outcomes. This tool is ideal for users needing comprehensive, easy-to-understand financial reports and election results.

## Features
- **Financial Analysis**: Calculates total months, total profits/losses, average changes, and highlights the greatest increases and decreases in profits.
- **Election Analysis**: Computes total votes, percentage of votes per candidate, and identifies the winner of the election.
- **Report Generation**: Outputs detailed analysis to both the console and text files, providing lasting documentation of insights.
- **Data Handling**: Includes robust error handling and data processing capabilities to manage large datasets effectively.

## Technologies Used
- Python
- CSV module for file operations
- OS module for directory and file path management
- List comprehensions and dictionary comprehensions for efficient data manipulation

## Setup and Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/SaadNasir92/Data-Insights-Tool
   ```
2. Navigate to the cloned directory:
    ```bash
    cd Data-Insights-Tool
    ```
3. Run the financial analysis script:
    ```bash
    python financial_analysis.py
    ```
4. Run the election analysis script:
    ```bash
    python election_analysis.py
    ```
## Customization
To analyze different datasets:

- Replace budget_data.csv or election_data.csv in the Resources folder with your data files ensuring the same format.

## Lessons Learned
- Developed advanced techniques in data parsing and analysis using Python's CSV module.
- Enhanced ability to design and implement functions that generate reusable insights.
- Gained experience in handling large datasets and producing comprehensible output formats for various stakeholders.