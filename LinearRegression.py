import os
import pandas as pd
import tkinter as tk
from tkinter import messagebox, font
from sklearn.linear_model import LinearRegression
from pymongo import MongoClient
from dotenv import load_dotenv


def run_application():
    load_dotenv()

    # 1. Main Window Setup
    root = tk.Tk()
    root.title("Grade Predictor Pro")
    root.geometry("400x250")
    root.configure(padx=20, pady=20)

    # Custom Font
    app_font = font.Font(family="Helvetica", size=10)

    def process_prediction():
        try:
            # Get input from entry box
            raw_val = hours_entry.get()
            if not raw_val:
                messagebox.showwarning("Input Error", "Please enter hours.")
                return

            hours_input = float(raw_val)
            if hours_input < 0:
                messagebox.showerror("Input Error", "Hours cannot be negative!")
                return

            # 2. Database & Model Logic
            mongo_uri = os.getenv("MONGO_URI")
            client = MongoClient(mongo_uri)
            db = client["universitydb"]
            collection = db["students"]

            data = list(collection.find({}, {"_id": 0}))
            if not data:
                messagebox.showwarning("Error", "No data found in database!")
                return

            df = pd.DataFrame(data)
            df["hours"] = pd.to_numeric(df["hours"], errors="coerce")
            df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
            df = df.dropna(subset=["hours", "marks"])

            X = df[["hours"]]
            Y = df["marks"]

            model = LinearRegression()
            model.fit(X, Y)

            # 3. Prediction
            input_df = pd.DataFrame([[hours_input]], columns=["hours"])
            prediction = round(float(model.predict(input_df)[0]), 2)

            # 4. Save and Show Result
            collection.insert_one({
                "hours": hours_input,
                "predicted_marks": prediction,
                "type": "prediction_log"
            })

            result_label.config(text=f"Predicted Marks: {prediction}", fg="#2ecc71")
            messagebox.showinfo("Success", f"Prediction {prediction} saved to Atlas!")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")
        except Exception as e:
            messagebox.showerror("System Error", str(e))

    # --- UI Elements ---
    tk.Label(root, text="Student Performance Predictor", font=("Helvetica", 14, "bold")).pack(pady=10)
    tk.Label(root, text="Enter Study Hours:", font=app_font).pack()

    hours_entry = tk.Entry(root, font=app_font, justify='center')
    hours_entry.pack(pady=5)
    hours_entry.focus_set()

    predict_btn = tk.Button(root, text="Predict Marks", command=process_prediction,
                            bg="#3498db", fg="white", font=app_font, padx=10)
    predict_btn.pack(pady=15)

    result_label = tk.Label(root, text="", font=("Helvetica", 11, "bold"))
    result_label.pack()

    root.mainloop()


if __name__ == "__main__":
    run_application()