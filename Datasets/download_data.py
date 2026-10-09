import os
from datasets import load_dataset

def download_benchmark():
    print("Downloading amber-benchmark from Hugging Face...")
    
    # Load the dataset from Hugging Face
    dataset = load_dataset("MM-Hallu/amber-benchmark")
    
    # Create a local directory to save the data if it doesn't exist
    os.makedirs("Datasets/data", exist_ok=True)
    
    # Save the dataset to a local CSV file inside the Datasets folder
    output_path = "Datasets/data/amber_benchmark.csv"
    dataset["train"].to_csv(output_path)
    
    print(f"Success! Dataset saved locally to: {output_path}")

if __name__ == "__main__":
    download_benchmark()
