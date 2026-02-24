
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')  
nltk.download('stopwords')
nltk.download('wordnet')
import pdfplumber
packages = ['punkt', 'punkt_tab', 'stopwords', 'wordnet']

for pkg in packages:
    nltk.download(pkg)