import pandas as pd

# Load your GSC Export (Free version handles CSVs you download for free)
def find_striking_distance(file_path):
    df = pd.read_csv(file_path)
    
    # Filter for keywords on Page 2 (Positions 11-20)
    # High impressions mean high potential traffic
    striking_distance = df[(df['Position'] > 10) & (df['Position'] <= 20)]
    
    # Sort by Impressions to find the biggest opportunities
    top_opportunities = striking_distance.sort_values(by='Impressions', ascending=False)
    
    return top_opportunities.head(10)

# This shows a recruiter you understand ROI-focused SEO strategy
print("Top 10 Keywords to Push to Page 1:")
# print(find_striking_distance('gsc_data.csv'))
