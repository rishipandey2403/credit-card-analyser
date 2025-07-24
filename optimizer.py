# optimizer.py

import pandas as pd

def load_cards_data(csv_path='cards_data.csv'):
    df = pd.read_csv(csv_path)
    return df

def recommend_cards(spend_dict, top_n=3):
    df = load_cards_data()
    
    card_results = []

    for index, row in df.iterrows():
        reward = 0
        for category in spend_dict:
            reward_rate = row.get(f"{category}_reward", 0)
            reward += reward_rate * spend_dict[category]
        
        card_results.append({
            "Card Name": row["Card_Name"],
            "Total Rewards (₹)": round(reward, 2),
            "Annual Fee (₹)": row["Annual_Fee"],
            "Notes": row["Notes"]
        })

    results_df = pd.DataFrame(card_results)
    results_df.sort_values(by="Total Rewards (₹)", ascending=False, inplace=True)
    
    return results_df.head(top_n)
