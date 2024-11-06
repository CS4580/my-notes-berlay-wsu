Module 7 Notes: Metrics and Model Development
Metrics

Metrics should be unbiased, universal, and concise.

    A way to obtain similar responses
    A way to measure the performance
    A way to measure prediction.

For our sample analysis we will use KNN K-Nearest Neighbor

    K is an arbitrary pick
    Need a base case
    Compare the neighbors
    Sor the results

Dataset for this analysis:

icarus.cs.weber.edu:~hvalle/cs4580/data/movies.csv

KNN-Euclidean Distance

Note: All code will be in knn_analysis.py

The Euclidean distance is the distance between points in N-dimensional space.

Formula $ d(p, q) = \sqrt{\sum_{i=1}^n (q_i - p_i)^2} $ where:

    p = ( p 1 , p 2 , … , p n )
    q = ( q 1 , q 2 , … , q n )

Task:

Find the distance between these points:

    x = (0,0)
    y = (4,4)

Distance = 5.65685...

# see
def euclidean_distance()

KNN with Jaccard Similarity Index

Compares members of two individual sets to determine which members are shared and which are distinct. The index measures the similarity between the two sets.

J ( A , B ) = | A ∩ B | | A ∪ B |

Ex: A = 1 , 2 , 3 , 4 and B = 3 , 4 , 5 , 6 = 2 6 or 0.33

# see
def jaccard_similarity_normal()

KNN with Weighted Jaccard Similarity Index

The traditional Jaccard works well when doing one-to-one comparisons between a category. It does not work on multiple categories.

One solution is the weighted version.

    Build a dictionary for each genre of the movies in our preferred list

# see
def jaccard_similarity_weighted()

KNN with Levenshtein Distance

This is the most common form of edit-based metric, which generally quantifies to work required to transform a string from an initial sequence to a target sequence.

    It is used to determine the difference between two sequences (strings)
    It is the distance between two words (minimum number of digits edits)
        insertions, deletions, or substitutions $$ D(i, j) = \begin{cases} j & \text{if } i = 0 \ i & \text{if } j = 0 \ D(i-1, j-1) & \text{if } s[i] = t[j] \ 1 + \min {D(i-1, j), D(i, j-1), D(i-1, j-1)} & \text{if } s[i] \neq t[j] \end{cases} $$

For example:

Consider these strings:

    s = 'kitten'
    t = 'sitting'

Find the Levenshteain Distance

    Substitude k with s in kitten -> sitten (1 substitution)
    Substitude e with i in sitten -> sittin (1 substitution)
    Insert g at the end of sittin -> sitting (1 insertion)

Result is 3 edits, so the distances is $ = 3$

# see
def knn_levenshtein_title()

