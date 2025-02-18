from entity_matching import compare_names_with_sentence_bert
import argparse
import pandas as pd
from data_handling import load_data_from_excel


def main():
    # Initialize ArgumentParser
    parser = argparse.ArgumentParser(description="Compare names between two Excel files using Sentence-BERT.")

    # Add arguments
    parser.add_argument("file1", help="Path to the first Excel file")
    parser.add_argument("file2", help="Path to the second Excel file")

    # Parse arguments
    args = parser.parse_args()

    # Load data from Excel files
    df1 = load_data_from_excel(args.file1)
    df2 = load_data_from_excel(args.file2)

    # Extract name columns as lists
    names1 = df1['Name'].tolist()
    names2 = df2['Name'].tolist()

    # names1 = ["John", "Alice", "Bob"]
    # names2 = ["Emma", "David", "Alice", "Sarah"]

    # Compare names using Sentence-BERT
    sbert_results, sbert_similarity_result, similarity = compare_names_with_sentence_bert(names1, names2)

    # Create DataFrame from results
    result_df = pd.DataFrame({
        'Name1': names1,
        'Similarity': similarity,
        'sbert_similarity_result': sbert_similarity_result,
        'sbert_all_results': sbert_results
    })

    # Save DataFrame to Excel
    result_df.to_excel("result_sbert.xlsx")
    print("Comparison results saved to result_sbert.xlsx")


if __name__ == "__main__":
    main()

# Run main file - python main.py file1.xlsx file2.xlsx
