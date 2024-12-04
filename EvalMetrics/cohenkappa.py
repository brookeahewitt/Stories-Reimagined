import pandas as pd
from sklearn.metrics import cohen_kappa_score
from itertools import combinations

df = pd.read_csv('survey_results.csv')
print(df)

metrics = df[['novel_score', 'feasibility_score', 'effective_score', 'excited_score', 'overall_score']]

# Print to check data
print(metrics)

raters = df['rater'].unique()

# Print to check data
print('\n')
print(raters)


# Calculate Cohen's Kappa for each pair of raters
def calculate_kappas(df, metric):
    pairs = combinations(raters, 2)
    kappa_scores = []

    for rater1, rater2 in pairs:
        r1_scores = df[df['rater'] == rater1][metric]
        r2_scores = df[df['rater'] == rater2][metric]
        kappa = cohen_kappa_score(r1_scores, r2_scores)
        kappa_scores.append((rater1, rater2, kappa))

    return kappa_scores


# Compute and display Kappa scores for each metric
all_metric_kappas = {}

for metric in metrics:
    print(f"\nMetric: {metric}")

    kappas = calculate_kappas(df, metric)
    all_metric_kappas[metric] = kappas

    for rater1, rater2, kappa in kappas:
        print(f"  {rater1} vs {rater2}: Kappa = {kappa:.2f}")


# Global agreement across all metrics
combined_kappas = []
pairs = combinations(raters, 2)

print('\n')

for rater1, rater2 in pairs:
    r1_scores = df[df['rater'] == rater1][['novel_score', 'feasibility_score', 'effective_score', 'excited_score', 'overall_score']].values.flatten()
    r2_scores = df[df['rater'] == rater2][['novel_score', 'feasibility_score', 'effective_score', 'excited_score', 'overall_score']].values.flatten()
    kappa = cohen_kappa_score(r1_scores, r2_scores)
    combined_kappas.append((rater1, rater2, kappa))
    print(f"Global {rater1} vs {rater2}: Kappa = {kappa:.2f}")


# Summary of mean kappa scores
metric_mean_kappas = {metric: sum(k[2] for k in scores) / len(scores) for metric, scores in all_metric_kappas.items()}
global_mean_kappa = sum(k[2] for k in combined_kappas) / len(combined_kappas)

print("\nSummary:")
for metric, mean_kappa in metric_mean_kappas.items():
    print(f"  Mean Kappa for {metric}: {mean_kappa:.2f}")
print(f"  Mean Global Kappa: {global_mean_kappa:.2f}")