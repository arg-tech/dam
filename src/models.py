

#from transformers import AutoTokenizer, AutoModel, BertTokenizer, BertForTokenClassification

from transformers import AutoTokenizer, AutoModel, BertTokenizer, BertForTokenClassification, BartForSequenceClassification, BartTokenizer


from sentence_transformers import SentenceTransformer

s_bert_model = SentenceTransformer('sentence-transformers/all-roberta-large-v1')

tokenizer = AutoTokenizer.from_pretrained('deepset/sentence_bert')
model = AutoModel.from_pretrained('deepset/sentence_bert')

token_clsification_tokenizer = BertTokenizer.from_pretrained('bert-base-cased', do_lower_case=False)

decompositional_model=   BertForTokenClassification.from_pretrained("model_token_clasiffier")


tokenizer_enatilement = BartTokenizer.from_pretrained('facebook/bart-large-mnli')
model_enatilement = BartForSequenceClassification.from_pretrained('facebook/bart-large-mnli')

from transformers import pipeline
sentiment_classifier=pipeline('sentiment-analysis')



from subject_verb_object_extract import findSVOs, nlp
import nltk 
from nltk.corpus import wordnet 
from nltk.corpus import stopwords
from nltk import pos_tag

import spacy
nlp_lg = spacy.load("en_core_web_lg")

