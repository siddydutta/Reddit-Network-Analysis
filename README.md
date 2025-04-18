# Reddit Network Analysis
> COMPSCI5107 Web Science MSc - 2024–25  

This coursework analyses user interaction patterns and discussion dynamics within the [`r/InvestmentClub`](https://www.reddit.com/r/InvestmentClub/) subreddit using network analysis techniques. Spanning a decade (2012–2022) of activity, it combines data engineering, graph theory, statistical metrics, and topic modeling to provide a structural overview of an online financial discussion community.

## Assignment Overview

- **Data Processing and Object Modeling**:
  - Cleaned and parsed Reddit JSON files (submissions + comments).
  - Created schema maps and dataclasses to model objects as Python DTOs.
  - Reconstructed hierarchical post-comment trees using BFS.

- **Graph Visualisation**:
  - **Author Interaction Graph**: Directed, weighted graph showing comment relationships between users.
  - **Post Discussion Graph**: Tree-like graph showing nested comment structure for individual submissions.

- **Network Metrics and Analysis**:
  - **Superuser Influence**: Evaluated network cohesion using connected components and rich club coefficient.
  - **Z-Score Roles**: Classified users as questioners or answerers based on posting behavior.
  - **Virality Score**: Combined cascade size and comment lifespan to score post popularity.

- **Additional Research**:
  - **Temporal Trends**: Submission and upvote activity across days, weeks, and years.
  - **User Engagement**: Submission timelines of top users, identifying consistent vs. burst participation.
  - **Topic Clustering**: KMeans clustering of submission titles using TF-IDF and PCA for 2D visualisation.

## Repository Contents

| Folder/File | Description |
|-------------|-------------|
| [`Web-Science-Coursework.pdf`](/Web-Science-Coursework.pdf) | Original coursework specification. |
| [`Reddit-Network-Analysis-Report.pdf`](/Reddit-Network-Analysis-Report.pdf) | Technical report summarising the entire coursework. |
| [`Reddit-Network-Analysis-Notebook.ipynb`](/Reddit-Network-Analysis-Notebook.ipynb) | Full data pipeline and analysis notebook. |
| [`charts/`](/charts/) | Interactive charts (z-score, virality, superuser metrics). |
| [`graphs/`](/graphs/) | HTML graph visualisations of author and post interactions. |
| [`schemas/`](/schemas/) | Scripts to infer and generate JSON schema definitions. |
| [`dtos/`](/dtos/) | Data Transfer Objects used to map Reddit JSON to Python classes. |
| [`objects/`](/objects/) | Pickled post/comment structures for reuse. |

## Selected Outputs

<details open>
<summary>Superuser Influence Graph</summary>

- Reveals the centrality of user `Zurevu`, whose removal significantly fragments the network.
- Secondary rich clubs emerge when the top user is removed, indicating hierarchical influence.

![Superuser Influence Graph](/charts/Superuser-Influence.png)

</details>

<details open>
<summary>Modified Z-Score Chart</summary>

- Power-law distribution of questions and answers by users.
- Behaviour of "bot" accounts to post more answers than questions.
- Increased participation correlates with more questioning behaviour.

![Z-Score Chart](/charts/Z-Score.png)

</details>

<details open>
<summary>Topic Clustering (TF-IDF + KMeans)</summary>

- 20 distinct topic clusters identified from ~19k submission titles.
- Themes included tech stocks, macroeconomics, oil prices, and transaction strategies.

![KMeans Topic Clusters Chart](/charts/KMeans-Topic-Clusters.png)

</details>

## Feedback

The goal of this coursework was to investigate the structure and behaviour of online communities through a combination of data processing, graph visualisation, and analytical techniques — using Python, NetworkX, Vega-Altair, and scikit-learn within a Jupyter Notebook environment.


- Process explained, irrelevant users not removed, and Data is summarised sufficiently (4/5)
- Thorough Analysis conducted and the data interpreted well (20/20)
- Three analyses conducted, data is processed and graphs are drawn. However, it is no clear what are your objectives? What research questions you were trying to answer?[12 each 36/45]
- Analysis conducted creatively – especially looking form multiple perspectives (20/20)
- 8/10 (some limitations in addressing multiple RQs in task 3)

**Grade: 88/100**
