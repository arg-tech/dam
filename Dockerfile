#FROM python:3.7.2
FROM python:3.8.2

#RUN apt-get update \
#        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y \
#        && pip3 install pyaudio

RUN pip install --upgrade pip

RUN pip3 install tqdm

RUN pip3 install pandas
 
RUN pip3 install torch
RUN pip3 install numpy
RUN pip3 install transformers
RUN pip3  install scikit-learn 
RUN pip3  install nltk
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader wordnet
RUN python3 -m nltk.downloader averaged_perceptron_tagger
RUN python3 -m nltk.downloader omw-1.4


RUN pip3 install spacy
RUN pip3 install Cython
#RUN python -m spacy download en
RUN python -m spacy download en_core_web_lg
RUN python -m spacy download en_core_web_sm
#RUN pip3 install sacrebleu
#RUN pip3 install -U Werkzeug
RUN pip3 install sentence_transformers


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5003
CMD python ./main.py