
from credit_card_data import credit_cards

def recommend_cards(spend_dict):
    recommendations = []

    for card in credit_cards:
        reward_value = 0
        for category, amount in spend_dict.items():
            benefit = card["category_benefits"].get(category, 0)
            reward_value += (benefit / 100) * amount
        
        net_benefit = reward_value - card["annual_fee"]
        recommendations.append((card["name"], round(net_benefit, 2)))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations
