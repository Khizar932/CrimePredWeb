import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_count_plots():
    df = pd.read_csv('D:\FYP WEB INTERFACE\serverFlask\data.csv')
    # Generate count plots
    sns.countplot(y=df['Description'])
    plt.savefig('static/count_plots.png')
    plt.close()

def generate_crime_rate_by_month():
    df = pd.read_csv('D:\FYP WEB INTERFACE\serverFlask\data.csv')
    
    df['CrimeTime'] = df['CrimeTime'].str.replace(':', '')

    df['Date'] = df['CrimeDate'] + ' ' + df['CrimeTime']
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %H%M', errors='coerce')

    df['Day'] = df['Date'].dt.day
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df['Weekday'] = df['Date'].dt.weekday + 1
    df['Hour'] = df['Date'].dt.hour

    # Generate crime rate by month plot
    plt.figure(figsize=(8,4), dpi=80)
    sns.countplot(x='Month', data=df)
    plt.savefig('static/crime_rate_by_month.png')
    plt.close()

# Generate the graphs
generate_count_plots()
generate_crime_rate_by_month()
