import io
import base64
import matplotlib.pyplot as plt
from flask import Flask, render_template, Response
import pandas as pd
import seaborn as sns
import os

app = Flask(__name__)


@app.route("/")
def index():
    # Create a simple matplotlib graph
    df = pd.read_csv("D:\FYP WEB INTERFACE\serverFlask\data.csv")
    # file_path = os.path.join('D:', 'FYP WEB INTERFACE', 'serverFlask', 'data.csv')
    # df = pd.read_csv(file_path)

    df["CrimeTime"] = df["CrimeTime"].str.replace(":", "")

    df["Date"] = df["CrimeDate"] + " " + df["CrimeTime"]
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y %H%M", errors="coerce")

    df["Day"] = df["Date"].dt.day
    df["Month"] = df["Date"].dt.month
    df["Year"] = df["Date"].dt.year
    df["Weekday"] = df["Date"].dt.weekday + 1
    df["Hour"] = df["Date"].dt.hour

    # Generate multiple graphs
    graphs = []

    # Graph 1

    ax = sns.countplot(x="Month", data=df)
    plt.ylabel("Crime Frequency", fontsize=13)
    plt.xlabel("Month", fontsize=13)
    labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    ax.set_xticklabels(labels)
    plt.plot()

    graph1_stream = io.BytesIO()
    plt.savefig(graph1_stream, format="png")
    graph1_stream.seek(0)
    graphs.append(
        {
            "image": base64.b64encode(graph1_stream.getvalue()).decode("utf-8"),
            "des": "Frequency of Crime by Month",
        }
    )
    plt.clf()

    # Graph 2

    ax = sns.countplot(x="Weapon", data=df)
    plt.ylabel(
        "Crime Frequency",
    )
    plt.xlabel(
        "Weapon Used",
    )

    plt.plot()

    graph2_stream = io.BytesIO()
    plt.savefig(graph2_stream, format="png")
    graph2_stream.seek(0)
    graphs.append(
        {
            "image": base64.b64encode(graph2_stream.getvalue()).decode("utf-8"),
            "des": "Frequency of Crime by Weapon Used",
        }
    )

    plt.clf()

    # Graph 3

    ax = sns.countplot(x="District", data=df)
    plt.ylabel(
        "Crime Frequency",
    )
    plt.xlabel(
        "District",
    )
    plt.xticks(rotation=19)
    plt.plot()

    graph3_stream = io.BytesIO()
    plt.savefig(graph3_stream, format="png")
    graph3_stream.seek(0)
    graphs.append(
        {
            "image": base64.b64encode(graph3_stream.getvalue()).decode("utf-8"),
            "des": "Frequency of Crime by District",
        }
    )

    plt.clf()

    # Graph 4
    plt.figure(figsize=(9, 4), dpi=80)

    ax = sns.countplot(x="Year", data=df)
    plt.ylabel("Crime Frequency", fontsize=13)
    plt.xlabel("Year")
    plt.plot()

    graph4_stream = io.BytesIO()
    plt.savefig(graph4_stream, format="png")
    graph4_stream.seek(0)
    graphs.append(
        {
            "image": base64.b64encode(graph4_stream.getvalue()).decode("utf-8"),
            "des": "Frequency of Crime by Year",
        }
    )

    plt.clf()

    # Graph 5
    ax = sns.countplot(x="Weekday", data=df)
    plt.ylabel("Crime Frequency", fontsize=13)
    plt.xlabel("Day of Week", fontsize=13)
    labels = ["Mon", "Tues", "Wed", "Thur", "Fri", " Sat", "Sun"]
    ax.set_xticklabels(labels)
    plt.plot()

    graph5_stream = io.BytesIO()
    plt.savefig(graph5_stream, format="png")
    graph5_stream.seek(0)
    graphs.append(
        {
            "image": base64.b64encode(graph5_stream.getvalue()).decode("utf-8"),
            "des": "Frequency of Crime by Day of Week",
        }
    )

    plt.clf()

    # Graph 6
    ax = sns.countplot(x="Hour", data=df)
    plt.ylabel("Crime Frequency", fontsize=13)
    plt.xlabel("Hour", fontsize=13)
    plt.plot()

    graph6_stream = io.BytesIO()
    plt.savefig(graph6_stream, format="png")
    graph6_stream.seek(0)
    graphs.append(
        {
            "image": base64.b64encode(graph6_stream.getvalue()).decode("utf-8"),
            "des": "Frequency of Crime by Hour of Day",
        }
    )

    plt.clf()

    # Graph 7
    ax = sns.countplot(x="Year", hue="Weapon", data=df)
    plt.ylabel("Crime Frequency", fontsize=13)
    plt.xlabel("Year", fontsize=13)
    plt.plot()

    graph7_stream = io.BytesIO()
    plt.savefig(graph7_stream, format="png")
    graph7_stream.seek(0)
    graphs.append(
        {
            "image": base64.b64encode(graph7_stream.getvalue()).decode("utf-8"),
            "des": "Frequency of Crime per Year Grouped by Weapon Used",
        }
    )

    plt.clf()

    # Pass the base64-encoded image data to the template
    return render_template("index.html", graphs=graphs)


if __name__ == "__main__":
    app.run(debug=True)
    # from werkzeug.serving import run_simple

    # run_simple("localhost", 5000, app)
