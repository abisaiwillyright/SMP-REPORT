# Code Challenge 1 — Project Delivery Risk
def predict_deliver_risk(crew_size, days_remaining, task_left):
    effeciency = task_left / (crew_size*days_remaining)
    if effeciency > 1.5:
        return "High risk"
    elif effeciency > 0.8:
        return "Medium risk"
    else:
        return "Low risk"
# data
project = [
    ('tilling', 3, 5, 25),
    ('plastering', 4, 10, 18),
    ('painting',2, 4, 8),
]

for name, crew, days, task in project:
    risk = predict_deliver_risk(crew, days, task)
    print(risk)
print(f"{'-'*20}\n")



# Code Challenge 2 — The Simp Detector
def simp_alert(spent, texted, replied, request, accepted):
    text_rates = replied/texted
    date_rates = accepted/request
    scores = (text_rates+date_rates)/2

    if scores > 0.5:
        return "She likes you"
    elif scores > 0.2:
        return "Lukewarm"
    else:
        return "You are simping"

# data
days = [
    ("Monday", 45000, 80, 2, 10, 0),
    ("Tuesday", 8000, 20, 15, 4, 2),
    ("Wednesday", 18000, 20, 6, 5, 1),
]

for day, money_spend, txt_send, txt_rply, dates, dates_acptd in days:
    responce = simp_alert(money_spend, txt_send, txt_rply, dates, dates_acptd)
    print(responce)