# Netflix-Content-Analysis

Netflix has transformed how people consume entertainment, supplying thousands of movies and tv shows across a long range of genres. Understanding patterns within Netflix's catalog can provide insight into trends, viewer preferences, and content evolution over time. In this project some questions i explored were

1. Does Netflix offer more movies or TV shows?
2. How has the number of titles released each year changed over time?
3. What are the most common genres on Netflix?
4. Have Netflix movie durations increased or decreased over time.

The dataset I used for this project is a curated Netflix titles file (NetFlix.csv). It contained 7,788 rows. Each column represented a single movie or TV show. These columns include: 

- type- Movie or TV show
- title- Name of the film/show
- release_year- when the title originally released
- duration- how long the movie ran for or number of seasons
- genres- which genres said title fall under

For data cleaning I removed unused columns like description, cast, director, converted duration to duration_num so I can have just the digits instead of "120 min", removed any null durations for regression analysis, and split multi-genre strings into individual genre labels for accurate counting. I used pandas for data handling, matplotlib for the graphs, and scikit-learn for linear regression.


When analyzing the data for each question, here's what I found:

Question 1: Movies vs TV Shows

Netflix contains significantly more movies (5377) than TV shows (2410) in this dataset. This suggests that while Netflix is well-known for original series like Wednesday or Stranger Things, its overall catalog leans towards movies.
<img width="424" height="280" alt="image" src="https://github.com/user-attachments/assets/4af600d1-09b2-4317-a25d-630b69b12576" />

Question 2: Titles Released Over Time

The number of titles over the years show just how much more film has gotten produced over the years. The older decades have fewer entries and more recent decades are expanding significantly. This aligns with the growth of global film production and Netflix acquiring a broader library of content.
<img width="712" height="352" alt="image" src="https://github.com/user-attachments/assets/b747023f-a563-46ca-ab5b-0571ae52509e" />

Question 3: Most Common Genres
The top 10 most common genres gathered from the dataset were:
- International Movies:       2437
- Dramas:                     2106
- Comedies:                   1471
- International TV Shows:     1199
- Documentaries:                786
- Action & Adventure:          721
- TV Dramas:                   704
- Independent Movies:           673
- Children & Family Movies:     532
- Romantic Movies:            531

The top genres show that Netflix heavily emphasizes international and story-driven content. International Movies and Dramas dominate the platform, indicating Netflix’s global reach and focus on emotionally centered narratives. Comedies and International TV Shows also appear frequently, showing that Netflix balances light hearted entertainment and worldwide programming. The fact that there's still other genres beneath those show that Netflix offers a wide variety of media to choose from.
<img width="712" height="352" alt="image" src="https://github.com/user-attachments/assets/4214ddce-7ced-45f3-9491-9671400b7387" />

Regression Analysis of Movie Duration Over Time

A big question I had while analyzing this data was to see if complaints I've seen on social media that movies over the years have gotten shorter and shorter. This has been a constant debate that I have seen online for a little while now, so I wanted to use this database to see if there's any truth to it. The regression results show that Netflix movies have become slightly shorter over time but it's small. The negative slope (–0.60) means that, on average, movie lengths decrease by a little more than half a minute per year. The correlation (–0.20) also shows a weak downward trend, meaning the relationship exists but it's not very strong. The intercept is just part of the math and does not have any practical meaning. Overall, this means newer movies tend to be somewhat shorter than older ones, but the difference is minimal.
<img width="712" height="424" alt="image" src="https://github.com/user-attachments/assets/8cf542f8-fea8-4d7c-9ec4-706cb6931b25" />

This analysis reveals several patterns in Netflix’s content offerings:

- Netflix has more movies than TV shows, suggesting films still dominate the platform’s catalog.
- Release-year data shows strong growth over recent decades, reflecting global increases in production and distribution.
- The dominance of drama, comedy, and international titles shows Netflix’s focus on emotionally-driven narratives and globally diverse content.
- Regression findings suggest that modern movies are becoming slightly shorter, which may reflect changes in audience preferences or production trends.

These patterns show just how Netflix curates and acquires its content, and how entertainment trends evolve over time.
