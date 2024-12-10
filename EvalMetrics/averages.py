import pandas as pd

df = pd.read_csv('survey_results.csv')
print(df)

metrics = df[['novel_score', 'feasibility_score', 'effective_score', 'excited_score', 'overall_score']]

# Print to check data
print('Metrics: ', metrics)

raters = df['rater'].unique()

# Print to check data
print('\nRaters:')
print(raters)


df_h = df[df['story'].str.contains('human')]
df_g = df[df['story'].str.contains('gen')]

print('\nHuman-created Stories and Generated Stories: ')
print(df_h.head())
print(df_g.head())

strings = ['Human-created', 'Generated']

# Calculate averages for each metric, for each rater
rater_averages = metrics.groupby(df['rater']).mean()
print('\nRater Averages:')
print(rater_averages)

# Calculate averages for each metric, for each rater with separate averages for human-made and generated stories
rater_averages_human = df_h.groupby('rater')[['novel_score', 'feasibility_score', 'effective_score', 'excited_score', 'overall_score']].mean()
rater_averages_generated = df_g.groupby('rater')[['novel_score', 'feasibility_score', 'effective_score', 'excited_score', 'overall_score']].mean()

print('\nRater Averages for Human-created Stories:')
print(rater_averages_human)

print('\nRater Averages for Generated Stories:')
print(rater_averages_generated)

# Calculate averages for each metric, for human-made and generated stories
human_averages = df_h[['novel_score', 'feasibility_score', 'effective_score', 'excited_score', 'overall_score']].mean()
generated_averages = df_g[['novel_score', 'feasibility_score', 'effective_score', 'excited_score', 'overall_score']].mean()

print('\nHuman-created Story Averages:')
print(human_averages)

print('\nGenerated Story Averages:')
print(generated_averages)