
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# -----------------------------------
# 1. Create sample dataset
# -----------------------------------

data = {
    "Awareness_Level": (
        ["High"] * 30 + ["High"] * 10
        + ["Low"] * 10 + ["Low"] * 20
    ),
    "Password_Practice": (
        ["Good"] * 30 + ["Poor"] * 10
        + ["Good"] * 10 + ["Poor"] * 20
    )
}

df = pd.DataFrame(data)

# Save the example data to a CSV file
df.to_csv("cybersecurity_survey.csv", index=False)

print("CYBERSECURITY AWARENESS PROJECT")
print("Total records:", len(df))

# -----------------------------------
# 2. Display the dataset
# -----------------------------------

print("\nFirst five records:")
print(df.head())

# -----------------------------------
# 3. Calculate frequencies
# -----------------------------------

print("\nAwareness level counts:")
print(df["Awareness_Level"].value_counts())

print("\nPassword practice counts:")
print(df["Password_Practice"].value_counts())

# -----------------------------------
# 4. Create observed frequency table
# -----------------------------------

observed = pd.crosstab(
    df["Awareness_Level"],
    df["Password_Practice"]
)

observed = observed.reindex(
    index=["High", "Low"],
    columns=["Good", "Poor"],
    fill_value=0
)

print("\nObserved Frequency Table:")
print(observed)

# -----------------------------------
# 5. Perform Chi-square test
# -----------------------------------

chi2, p_value, dof, expected = chi2_contingency(
    observed,
    correction=False
)

expected_table = pd.DataFrame(
    expected,
    index=observed.index,
    columns=observed.columns
)

print("\nExpected Frequency Table:")
print(expected_table.round(2))

print("\nChi-square statistic:", round(chi2, 4))
print("Degrees of freedom:", dof)
print("P-value:", round(p_value, 6))

# -----------------------------------
# 6. Interpret the result
# -----------------------------------

alpha = 0.05

print("\nHypothesis Testing:")

if p_value < alpha:
    print("Reject the null hypothesis.")
    print(
        "There is a statistically significant association "
        "between awareness level and password practice."
    )
else:
    print("Do not reject the null hypothesis.")
    print(
        "There is insufficient evidence of an association "
        "between awareness level and password practice."
    )

print("\nH0: Awareness and password practice are independent.")
print("H1: Awareness and password practice are associated.")

# -----------------------------------
# 7. Create bar chart
# -----------------------------------

observed.plot(
    kind="bar",
    figsize=(8, 5),
    rot=0
)

plt.title("Cybersecurity Awareness and Password Practice")
plt.xlabel("Awareness Level")
plt.ylabel("Number of Students")
plt.legend(title="Password Practice")
plt.tight_layout()

plt.savefig("cybersecurity_chart.png", dpi=200)

print("\nChart saved as cybersecurity_chart.png")

plt.show()
