# AI Attention Visualizer

AI Attention Visualizer is a Streamlit-based application that extracts text from images, generates semantic embeddings for the extracted words, and calculates attention scores to identify which words receive higher attention.

The project demonstrates how OCR, embeddings, and attention mechanisms can be combined in an interactive AI application.

## Features

* Upload an image in JPG, JPEG, or PNG format
* Extract text from the uploaded image using OCR
* Process extracted words using semantic embeddings
* Calculate attention scores for the analyzed words
* Display the extracted text
* Show the number of words extracted and analyzed
* Display individual word attention scores
* Highlight the word with the highest attention score
* Interactive Streamlit interface

## How It Works

The application follows a simple processing pipeline:

```text
Image Upload
     |
     v
OCR Text Extraction
     |
     v
Text Processing
     |
     v
Semantic Embeddings
     |
     v
Attention Calculation
     |
     v
Attention Scores
     |
     v
Highest Attention Word
```

### 1. Image Upload

The user uploads an image through the Streamlit interface.

Supported formats:

* JPG
* JPEG
* PNG

### 2. OCR

The uploaded image is processed using the OCR module to extract the text.

If no text is detected, the application displays an error message and stops the analysis.

### 3. Text Processing

The extracted text is split into individual words.

Punctuation is removed and words with fewer than three characters are filtered out. The application then analyzes up to 20 words.

### 4. Semantic Embeddings

The processed words are passed to the embedding module to create semantic representations.

```python
embeddings = create_embeddings(words)
```

### 5. Attention Calculation

The generated embeddings are passed to the attention module.

```python
scores = calculate_attention(embeddings)
```

The attention module creates Query, Key, and Value representations and calculates scaled dot-product attention.

```text
Embeddings
    |
    +--> Query
    |
    +--> Key
    |
    +--> Value
    |
    v
Q × Kᵀ
    |
    v
Scaled Attention Scores
    |
    v
Softmax
    |
    v
Attention Weights
    |
    v
Word Attention Scores
```

### 6. Result Visualization

The application displays:

* Words analyzed
* Words extracted
* Embeddings count
* Attention score for each word
* Highest-attention word

Attention scores are normalized using the maximum score before being displayed.

## Project Structure

```text
AI-Attention-Visualizer/
│
├── app.py
├── attention.py
├── OCR.py
├── embedding.py
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Streamlit
* NumPy
* PIL
* OCR
* Semantic Embeddings
* Attention Mechanism

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/srudhyasankarannarayanan/AI-Attention-Visualizer.git
```

### 2. Navigate to the Project

```bash
cd AI-Attention-Visualizer
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install the main dependencies:

```bash
pip install streamlit numpy pillow
```

Additional dependencies required by `OCR.py` and `embedding.py` should also be installed according to their implementation.

## How to Run

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

## Example Workflow

1. Open the application.
2. Upload an image containing text.
3. The application extracts the text using OCR.
4. The extracted text is divided into words.
5. Semantic embeddings are generated.
6. Attention scores are calculated.
7. Individual attention scores are displayed.
8. The word receiving the highest attention score is highlighted.

## Attention Mechanism

The project implements a scaled dot-product attention approach.

The attention module creates three matrices:

```text
Q = X × WQ
K = X × WK
V = X × WV
```

The attention scores are calculated using:

```text
Scores = Q × Kᵀ
```

The scores are scaled using the square root of the key dimension:

```text
Scaled Scores = Scores / √dk
```

Softmax is then applied to obtain attention weights.

Finally, the attention weights are averaged to obtain a score for each word.

## Output

The application provides an interactive visualization containing:

* Extracted text
* Number of words extracted
* Number of words analyzed
* Attention score for every analyzed word
* Highest-attention word

## Use Cases

This project can be used for learning and demonstrating:

* Optical Character Recognition
* Natural Language Processing
* Semantic Embeddings
* Transformer-style Attention
* Scaled Dot-Product Attention
* AI visualization
* Streamlit application development

## Limitations

* The application analyzes only the first 20 processed words.
* The quality of the results depends on the quality of the OCR output.
* Attention scores depend on the generated embeddings.
* The attention weights are calculated using randomly initialized projection matrices in the current implementation.
* The project is intended primarily for educational and experimental purposes.

## Screenshots
<img width="1063" height="647" alt="image" src="https://github.com/user-attachments/assets/1d81225c-65b6-4d6c-b5b3-02c0443a6d74" />
<img width="324" height="646" alt="image" src="https://github.com/user-attachments/assets/dae3e35b-3390-4683-abc5-7947dfa9ca73" />

## Future Improvements

* Add support for PDF documents.
* Improve OCR accuracy.
* Add better text preprocessing.
* Use a pretrained transformer model for attention analysis.
* Add attention heatmap visualization.
* Display attention relationships between words.
* Add downloadable analysis reports.
* Support larger text inputs.
* Add model selection for different embedding models.

## License

This project is intended for educational and learning purposes. Add an appropriate open-source license if you plan to distribute the project publicly.

## Author

**Srudhya Sankaranarayanan**
