from models import train_from_csv

def main():
    # Replace with actual CSV file path
    csv_path = "training_data.csv"
    
    print("Training models...")
    vectorizer, classifier, test_data = train_from_csv(csv_path)
    print("Models trained and saved successfully!")
    print("You can now run app.py to start the API server.")

if __name__ == "__main__":
    main()