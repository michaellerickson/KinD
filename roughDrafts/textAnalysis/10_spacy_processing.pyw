return
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def process_text_with_nltk(text):
    
    # Process text using NLTK (Natural Language Toolkit).

    text: Text to be processed.
    return Tokenized, lemmatized, and stopword-removed text.
    
    # Tokenize the text
    tokens = word_tokenize(text)

    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in lemmatized_tokens if token not in stop_words]

    return filtered_tokens

def process_text_with_spacy(text):
    
    Process text using spaCy.

    text: Text to be processed.
    return Tokenized, lemmatized, and stopword-removed text.
    
    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Process text
    doc = nlp(text)

    # Get lemmatized tokens and filter out stopwords and punctuation
    processed_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

    return processed_tokens

# Example usage
# text = "The quick brown fox jumps over the lazy dog."
# nltk_tokens = process_text_with_nltk(text)
# print(f"Processed with NLTK: {nltk_tokens}")
# spacy_tokens = process_text_with_spacy(text)
# print(f"Processed with spaCy: {spacy_tokens}")
return
