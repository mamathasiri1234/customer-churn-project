import csv
import random

rows = []

for i in range(500):

    age = random.randint(18, 60)
    tenure = random.randint(1, 60)          # months
    charge = random.randint(20, 120)        # monthly bill
    complaints = random.randint(0, 10)

    # Realistic churn rule
    if complaints > 5 and charge > 80 and tenure < 12:
        churn = 1
    else:
        churn = 0

    rows.append([age, tenure, charge, complaints, churn])


with open("customer_churn.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Age","Tenure","MonthlyCharge","Complaints","Churn"])
    writer.writerows(rows)

print("Realistic artificial churn dataset created ✅")
