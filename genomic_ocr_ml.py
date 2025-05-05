import pytesseract
from PIL import Image
import re
import json
from Bio import SeqIO
from Bio.Seq import Seq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

# Sample training data for ML classification (simplified for demo)
# In a real project, this would be a larger dataset
training_texts = [
    "The sequence ATGCGTACG is a coding region for protein X",
    "Non-coding region contains TTAGGG repeats",
    "ATGCCCTAG is a promoter sequence",
    "Random text with no genomic data"
]
labels = ["coding", "non-coding", "promoter", "irrelevant"]

# Train a simple Naive Bayes classifier
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(training_texts)
clf = MultinomialNB()
clf.fit(X_train, labels)

def perform_ocr(image_path):
    """Extract text from an image using OCR."""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error during OCR: {str(e)}"

def extract_gene_sequences(text):
    """Extract potential gene sequences using regex."""
    # Simple regex for DNA sequences (at least 6 bases, A/T/G/C)
    pattern = r'[ATGC]{6,}'
    sequences = re.findall(pattern, text)
    return sequences

def classify_text(text):
    """Classify text using the trained ML model."""
    X_test = vectorizer.transform([text])
    prediction = clf.predict(X_test)[0]
    return prediction

def process_genomic_document(image_path):
    """Main function to process a genomic document image."""
    # Step 1: Perform OCR
    extracted_text = perform_ocr(image_path)
    
    # Step 2: Extract gene sequences
    sequences = extract_gene_sequences(extracted_text)
    
    # Step 3: Classify the text
    classification = classify_text(extracted_text)
    
    # Step 4: Validate sequences using BioPython
    valid_sequences = []
    for seq in sequences:
        try:
            bioseq = Seq(seq)
            valid_sequences.append({
                "sequence": seq,
                "length": len(bioseq),
                "is_valid_dna": str(bioseq).upper() == seq.upper()
            })
        except Exception as e:
            valid_sequences.append({
                "sequence": seq,
                "error": str(e)
            })
    
    # Step 5: Prepare output
    result = {
        "extracted_text": extracted_text,
        "classification": classification,
        "gene_sequences": valid_sequences
    }
    
    # Save results to JSON
    with open("genomic_ocr_results.json", "w") as f:
        json.dump(result, f, indent=4)
    
    return result

if __name__ == "__main__":
    # Example usage (replace with actual image path)
    image_path = "data/sample_image.png"
    results = process_genomic_document(image_path)
    print(json.dumps(results, indent=4))
