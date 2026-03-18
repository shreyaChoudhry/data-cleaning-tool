
import pandas as pd
from utils import remove_duplicates, fill_missing, drop_missing, summary
from visualize import plot_missing
print("=== DATA CLEANING TOOL ===")

file_path = input("Enter CSV file name: ")

try:
    df = pd.read_csv(file_path)
    print("\nOriginal Data:\n", df)

    print("\nOptions:")
    print("1. Remove duplicates")
    print("2. Fill missing")
    print("3. Drop missing")
    print("4. All")

    choice = input("Enter choice: ")

    if choice == "1":
        df = remove_duplicates(df)

    elif choice == "2":
        method = input("Method (ffill/bfill): ")
        df = fill_missing(df, method)

    elif choice == "3":
        df = drop_missing(df)

    elif choice == "4":
        df = remove_duplicates(df)
        df = fill_missing(df)

    else:
        print("Invalid choice")

    print("\nCleaned Data:\n", df)

    summary(df)
    plot_missing(df) 

    df.to_csv("cleaned_data.csv", index=False)

    print("\n✅ File saved as cleaned_data.csv")

except FileNotFoundError:
    print("❌ File not found")