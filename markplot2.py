import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1) Read CSV
# -----------------------------
df = pd.read_csv("student_marks.csv")

# -----------------------------
# 2) Quick look at the data
# -----------------------------
print("\nFirst 5 rows:\n")
print(df.head())

print("\nShape of data (rows, columns):", df.shape)
print("\nColumn names:", list(df.columns))

# -----------------------------
# 3) Summary statistics (Pandas)
# -----------------------------
print("\nSummary statistics:\n")
print(df.describe())

# -----------------------------
# 4) Top 5 students by Total marks
# -----------------------------
df["Total"] = df["Maths"] + df["Science"] + df["English"]
top5 = df.sort_values(by="Total", ascending=False).head(5)

print("\nTop 5 students by Total marks:\n")
print(top5[["Student_Name", "Total"]])

# -----------------------------
# 5) Subject-wise mean, min, max (NumPy)
# -----------------------------
marks = df[["Maths", "Science", "English"]].to_numpy()

mean_marks = np.mean(marks, axis=0)
min_marks = np.min(marks, axis=0)
max_marks = np.max(marks, axis=0)

subjects = ["Maths", "Science", "English"]

print("\nSubject-wise statistics (NumPy):")
for i, sub in enumerate(subjects):
    print(f"{sub} -> Mean: {mean_marks[i]:.2f}, Min: {min_marks[i]}, Max: {max_marks[i]}")

# -----------------------------
# 6) Plot average marks vs subject
# -----------------------------
plt.bar(subjects, mean_marks)
plt.title("Average Marks per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()