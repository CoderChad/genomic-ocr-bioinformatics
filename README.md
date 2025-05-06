# Genomic OCR and ML for Bioinformatics

This project integrates Optical Character Recognition (OCR) with AI/ML to process scanned or image-based genomic research documents. It extracts text, identifies gene sequences, and classifies document content using a Naive Bayes classifier. The project is built with Python, leveraging `pytesseract` for OCR, `BioPython` for genomics, and `scikit-learn` for machine learning.

## Features
- Extracts text from images of genomic documents using OCR.
- Identifies DNA sequences using regex patterns.
- Classifies text as coding, non-coding, promoter, or irrelevant using ML.
- Validates sequences with BioPython.
- Outputs results in a structured JSON format.

## Repository Structure
```
genomic-ocr-bioinformatics/
├── data/
│   └── sample_image.png        # Placeholder for sample genomic document image
├── genomic_ocr_ml.py          # Main Python script
├── example_usage.ipynb        # Jupyter notebook with usage demo
├── requirements.txt           # Project dependencies
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## Prerequisites
- Python 3.8+
- Tesseract OCR installed on your system:
  - Windows: Download and install from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
  - Linux: `sudo apt-get install tesseract-ocr`
  - macOS: `brew install tesseract`
- Sample genomic document image (PNG, JPG, or PDF converted to image).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/chad-thomas/genomic-ocr-bioinformatics.git
   cd genomic-ocr-bioinformatics
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure Tesseract is installed and accessible in your system PATH.

## Usage
1. Place a genomic document image in the `data/` directory (e.g., `data/sample_image.png`).
2. Run the main script:
   ```bash
   python genomic_ocr_ml.py
   ```
3. Check the output in `genomic_ocr_results.json`.
4. Alternatively, explore the `example_usage.ipynb` notebook for an interactive demo.

## Example Output
```json
{
    "extracted_text": "The sequence ATGCGTACG is a coding region...",
    "classification": "coding",
    "gene_sequences": [
        {
            "sequence": "ATGCGTACG",
            "length": 9,
            "is_valid_dna": true
        }
    ]
}
```




