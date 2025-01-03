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
        insertions, deletions, or substitutions 
        
$$ D(i, j) = \begin{cases} j & \text{if } i = 0 \ i & \text{if } j = 0 \ D(i-1, j-1) & \text{if } s[i] = t[j] \ 1 + \min {D(i-1, j), D(i, j-1), D(i-1, j-1)} & \text{if } s[i] \neq t[j] \end{cases} $$

For example:

Consider these strings:

    s = 'kitten'
    t = 'sitting'

Find the Levenshteain Distance

    Substitude k with s in kitten -> sitten (1 substitution)
    Substitude e with i in sitten -> sittin (1 substitution)
    Insert g at the end of sittin -> sitting (1 insertion)

Result is 3 edits, so the distances is $ = 3$

```python
# see
def knn_levenshtein_title()
```

### KNN Cosine Similarity Distance
It is used to measure the cosine of the angle between two vectors in a multi-dimensionality space. This is commonly used in text analysis to measure similarities between documents.

$$
\text{Cosine Similarity} = \cos(\theta)\\
= \frac{A \cdot B}{|A| |B|}
= \frac{\sum_{i=1}^{n} A_i B_i} { \sqrt{\sum_{i=1}^{n} A_i^2} \cdot \sqrt{\sum_{i=1}^{n} B_i^2}}
$$

where
- $ A \cdot B$ is the dot product of vectors $A$ and $B$
- $|A|$ and $|B|$ are magnitude (or Euclidean norms) of vectors $A$ and $B$

### KNN Combining Metrics and Filtering Conditions

Two main concerns with `filtering`:
- Make too complicated (hard SQL queries)
- Too strick (end up with no results)
    - Adding filters gradually

Combine `metrics` to generate `one` results:
- Weight each metric
    - Should metric contribute equally? (50/50,80/20)
- Normalization of the combined metric
    - Make sure they have the same range

For our example we will use:
- `Cosine`: use 20% of the `plot`
- `Weighted Jaccard`: use 80% of `genre`

```python
# See cosine_and_weighted_jaccard()
```

### Prediction Metrics
A `prediction` is a simple guess about what is going to transpire. One prediction is `yes` or `no`.

How do we measure `accuracy` of the prediction?

```python
accuracy_metric.py
```
### Confusion Matrix
It is performed to measure how well you classification model is. The model could be binary or multi-class. Each entry in confusion matrix represents specific combination of predicted vs actual classes.

For binary classification, you have `four` parts:
- `True positive (TP)`: Correctly predicted positive observations
- `True negatives (TN)`: Correctly predicted negative observations
- `False positives (FP)`: Incorrectly predicted positive, `Type 1 error`
- `False negatives (FN)`: Incorrectly predicted negatives, `Type 2 error`

The structure of the matrix is as follows:
|       |Predicted Positives| Predicted Negatives|
|-------|-------------------|--------------------|
|Actual positive| True Positive (TP)|False Negative (FN)|
|Actual Negative|

Key metrics:
- `Accuracy` = $\frac{TP + TN}{TP+ TN + FP + FN}$
- `Precision` = $\frac{{TP}}{{TP+FP}}$ (useful for imbalanced classes)
- `Recall` (or Sensitivity) = $\frac{{TP}}{{TP+FN}}$
- `F1 Score` = $ 2 \times \frac{{Precision \times Recall}}{{Precision+Recall}}$ (harmonic mean of Precision and recall)

```python
# see
confusion_matrix.py
```
