# PaperResearcher
Simple Python CLI for managing research papers: add, view, keyword search by abstract frequency, and cosine similarity for top similar papers. Pure stdlib, JSON persistence, sample ML papers included.

I built this simple command line tool to manage a collection of research papers in a JSON file. You can add papers with title, author, year, abstract and keywords. View all of them. Search by keywords in the abstracts, ranked by word count matches. Find top similar papers to any title using cosine similarity on word frequencies from abstracts.

It uses only Python's standard library. No extra packages needed. Sample papers.json comes with nine ML papers on GNNs, NLP, RL, vision, quantum stuff and one emoji junk entry for testing.

What It Does
I made prompts to add papers and it checks for duplicate titles, lets you rewrite or cancel.
View all prints full details for every paper.
Search takes comma separated keywords, counts them in each abstract, sorts from most to least hits.
Similar papers skips the exact title match and gives top three by cosine score. Saves changes right back to JSON.

Files I Wrote
-library.py is the LIBRARY class that loads and saves the JSON, handles search and similarity.
-paper.py is RESEARCHPAPER for single papers, tokenizes text, counts words.
-similarity.py does the math: dot product, magnitude, cosine similarity.
-main.py runs the menu and input loop.
-papers.json starts with my test data.

How I Did the Math
Abstracts get lowercased, punctuation stripped, split to words, frequencies counted. Bag of words style.
Search sums query word hits per paper.
Cosine similarity treats frequencies as vectors: dot product over mag1 times mag2. Between 0 and 1.

Empty file or library just starts fresh.

Run It
python main.py
Enter papers.json
Pick 1 to 5.

Like searching "deep learning" gives:

Deep Learning for Medical Image Analysis (2 matches)

Graph Neural Networks: A Survey (1 match)
