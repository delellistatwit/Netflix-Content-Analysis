# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load dataset
df = pd.read_csv("NetFlix.csv")

# Basic cleaning
# Drop unused text-heavy columns (ignore if missing)
df = df.drop(columns=["description", "director", "cast"], errors="ignore")


# Extract numeric duration from strings like "90 min" or "3 Seasons"
df["duration_num"] = df["duration"].astype(str).str.extract(r"(\d+)").astype(float)

# Question 1: Movies vs TV Shows
type_counts = df["type"].value_counts()

plt.figure(figsize=(6, 4))
type_counts.plot(kind="bar")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

print("Movies vs TV Shows:")
print(type_counts)
print("\n")

# Question 2: Titles Released Over Time
year_counts = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
year_counts.plot(kind="line")
plt.title("Number of Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

print("Titles per release year (first few):")
print(year_counts.head())
print("\n")

# Question 3: Most Common Genres

genre_series = df["genres"].dropna().str.split(",", expand=True).stack().str.strip() # Split genres into multiple rows

top_genres = genre_series.value_counts().head(10)

plt.figure(figsize=(10, 5))
top_genres.plot(kind="bar")
plt.title("Top 10 Most Common Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

print("Top 10 genres:")
print(top_genres)
print("\n")

# Regression - Movie Duration vs Release Year
from sklearn.linear_model import LinearRegression

# Filter movies with valid duration
movies = df[(df["type"] == "Movie") & df["duration_num"].notna()].copy()

X = movies[["release_year"]]
y = movies["duration_num"]

model = LinearRegression()
model.fit(X, y)

coef = model.coef_[0]
intercept = model.intercept_

print("Regression: duration_num ~ release_year")
print("  Coefficient:", coef)
print("  Intercept:", intercept)

# Correlation
corr = movies["duration_num"].corr(movies["release_year"])
print("  Correlation between release_year and duration_num:", corr)
print("\n")

# Scatter + regression line
plt.figure(figsize=(10, 6))
plt.scatter(movies["release_year"], movies["duration_num"], alpha=0.3, label="Movie durations")
plt.plot(movies["release_year"], model.predict(X), color="red", linewidth=2, label="Regression Line")
plt.title("Movie Duration vs Release Year (Netflix Movies)")
plt.xlabel("Release Year")
plt.ylabel("Duration (Minutes)")
plt.legend()
plt.tight_layout()
plt.show()
