from models import (stopwords, findSVOs, nlp, pos_tag)
from src.decompose import get_componenets_svo,get_components_list, decomposotionality




def get_functional_components(pair_of_propositions):
    text1, text2 = pair_of_propositions	
    doc1 = nlp(text1)
    doc2 = nlp(text2)    
    more_elements1 = decomposotionality(doc1)
    more_elements2 = decomposotionality(doc2)
    tok1 = nlp(text1)
    svos1 = findSVOs(tok1)  
    comp1 = [list(elem) for elem in svos1]    
    more_elements1 = [list(elem) for elem in more_elements1]    
    comp1 = comp1+more_elements1
    tok2 = nlp(text2)
    svos2 = findSVOs(tok2)
    comp2=[list(elem) for elem in svos2]    
    more_elements2=[list(elem) for elem in more_elements2]    
    comp2=comp2+more_elements2### elements of p2


    comp22=[] #remove stop words for p1

    for ll in comp2:# list
        wrd_lst=[]
        for phrase in ll: #pharse
            phrase_wrd=""			
            tokens=phrase.split()
            for word in tokens:
                if word not in stopwords.words('english'):
                    if word:
                        phrase_wrd=phrase_wrd+" "+ word.strip()
            if phrase_wrd:
                wrd_lst.append(phrase_wrd.strip())
        comp22.append(wrd_lst)
        

    comp11=[]  ## remve stop words from p2  
    for ll in comp1:# list
        wrd_lst=[]		
        for phrase in ll: #pharse
            phrase_wrd=""			
            tokens=phrase.split()
            for word in tokens:
                if word not in stopwords.words('english'):
                    if word:
                        phrase_wrd=phrase_wrd+" "+ word.strip()
            if phrase_wrd:
                wrd_lst.append(phrase_wrd.strip())
        comp11.append(wrd_lst)
    return comp11, comp22


def get_functional_componenets_dam3(p1p2):

    text1,text2=p1p2  
    entailemt=[]
        
    d_tc_c,d_asp_c,d_opinion_c,d_sentimnt_c,texts_all_c=get_components_list([text1])# sequence labling based   
    svo_tc_c,svo_asp_c,svo_opinion_c=get_componenets_svo(text1)# svo pattern based
    merged_tc_c,merged_asp_c,merged_opinion_c=list(set(svo_tc_c) | set([" ".join(d_tc_c)])),\
        list(set(svo_asp_c) | set([" ".join(d_asp_c)])),\
            list(set(svo_opinion_c) | set([" ".join(d_opinion_c)]))
        

    d_tc_p,d_asp_p,d_opinion_p,d_sentimnt_p,texts_all_p=get_components_list([text2])# sequence labling based   

    svo_tc_p,svo_asp_p,svo_opinion_p=get_componenets_svo(text2)# svo pattern based
    merged_tc_p,merged_asp_p,merged_opinion_p=list(set(svo_tc_p) | set([" ".join(d_tc_p)])),\
        list(set(svo_asp_p) | set([" ".join(d_asp_p)])),\
            list(set(svo_opinion_p) | set([" ".join(d_opinion_p)]))
            
            
    #consider Nouns and VERBS only for tc and aspects

    merged_tc_c_clean=[]
    for m_tc_c in merged_tc_c:
        cleaned_tokens=[]
        token_tag_dct=pos_tag([m_tc_c])
        #print("token_tag_dct : ",token_tag_dct)
        for tok,tag in token_tag_dct:
            if tag in ['NNP','NN','VBP','NNS','JJ']:
                cleaned_tokens.append(tok)
        if len(cleaned_tokens)>0:
            merged_tc_c_clean.append(" ".join(cleaned_tokens))
        
    merged_tc_p_clean=[]
    for m_tc_c in merged_tc_p:
        cleaned_tokens=[]
        token_tag_dct=pos_tag([m_tc_c])
        for tok,tag in token_tag_dct:
            if tag in ['NNP','NN','VBP','NNS','JJ']:
                cleaned_tokens.append(tok)
        if len(cleaned_tokens)>0:
            merged_tc_p_clean.append(" ".join(cleaned_tokens))
        
    merged_asp_c_clean=[]
    for m_tc_c in merged_asp_c:
        cleaned_tokens=[]
        token_tag_dct=pos_tag([m_tc_c])
        for tok,tag in token_tag_dct:
            if tag in ['NNP','NN','VBP','NNS','JJ']:
                cleaned_tokens.append(tok)			
        if len(cleaned_tokens)>0:
            merged_asp_c_clean.append(" ".join(cleaned_tokens))

    merged_asp_p_clean=[]
    for m_tc_c in merged_asp_p:
        cleaned_tokens=[]
        token_tag_dct=pos_tag([m_tc_c])
        for tok,tag in token_tag_dct:
            if tag in ['NNP','NN','VBP','NNS','JJ']:
                cleaned_tokens.append(tok)			
        if len(cleaned_tokens)>0:        
            merged_asp_p_clean.append(" ".join(cleaned_tokens))
        
        
        

    # if the target concept, aspect of the premise and conclussion are not recoginized by the models
    # use patterns

    if len(merged_tc_c_clean)==0 or len(merged_asp_c_clean)==0:
        doc=nlp(text1)
        c_patterns_tc,c_pattern_asp,c_paterns_ops=decomposotionality(doc)
        
        if len(merged_tc_c_clean)==0:
            merged_tc_c_clean=c_patterns_tc
            
        if len(merged_asp_c_clean)==0:
            merged_asp_c_clean=c_pattern_asp        

    if len(merged_tc_p_clean)==0 or len(merged_asp_p_clean)==0:
        doc=nlp(text2)    
        p_patterns_tc,p_pattern_asp,p_paterns_ops=decomposotionality(doc)
        
        if len(merged_tc_p_clean)==0:
            merged_tc_p_clean=p_patterns_tc
        
        if len(merged_asp_p_clean)==0:
            merged_asp_p_clean=p_pattern_asp 
    return  merged_tc_c_clean  , merged_tc_p_clean , merged_asp_c_clean, merged_asp_p_clean