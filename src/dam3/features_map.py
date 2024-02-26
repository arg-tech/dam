
from src.sentiment import sim_feature
from src.similarity import get_sim, get_anotnyms_dam3
from src.get_entailemnt import get_entailement
from src.decompose.get_components import get_functional_componenets_dam3

class ArgumentRelationAnalyzer:
    @staticmethod
    def get_argument_relation(p1p2):
        text1, text2 = p1p2
        merged_tc_c_clean, merged_tc_p_clean, merged_asp_c_clean, merged_asp_p_clean = \
            ArgumentRelationAnalyzer._get_functional_components_dam3(p1p2)

        sim_tc_conclusion_premise = ArgumentRelationAnalyzer._calculate_similarity(
            merged_tc_c_clean, merged_tc_p_clean, get_sim
        )
        sim_tc_conclusion_asp_premise = ArgumentRelationAnalyzer._calculate_similarity(
            merged_tc_p_clean, merged_asp_c_clean, get_sim
        )
        sim_asp_conclusion_tc_premise = ArgumentRelationAnalyzer._calculate_similarity(
            merged_tc_c_clean, merged_asp_p_clean, get_sim
        )
        sim_asp_conclusion_asp_premise = ArgumentRelationAnalyzer._calculate_similarity(
            merged_asp_p_clean, merged_asp_c_clean, get_sim
        )

        antonymys_tc_c = ArgumentRelationAnalyzer._get_antonyms(merged_tc_c_clean)
        antonymys_tc_p = ArgumentRelationAnalyzer._get_antonyms(merged_tc_p_clean)
        antonymys_asp_c = ArgumentRelationAnalyzer._get_antonyms(merged_asp_c_clean)
        antonymys_asp_p = ArgumentRelationAnalyzer._get_antonyms(merged_asp_p_clean)

        entailemt = ArgumentRelationAnalyzer._get_entailement(text1, text2)

        arg_rel1 = ArgumentRelationAnalyzer._get_argument_relation_decomp(
            entailemt, antonymys_asp_p, antonymys_asp_c, antonymys_tc_p, antonymys_tc_c,
            [sim_asp_conclusion_asp_premise], [sim_tc_conclusion_asp_premise],
            [sim_tc_conclusion_premise], [sim_asp_conclusion_tc_premise],
            merged_tc_c_clean, merged_tc_p_clean, merged_asp_c_clean, merged_asp_p_clean
        )
        return arg_rel1

    @staticmethod
    def _calculate_similarity(components1, components2, similarity_function):
        similarity_scores = []
        for component1 in components1:
            for component2 in components2:
                similarity_scores.append(similarity_function(component1, component2))
        if similarity_scores:
            return max(similarity_scores)
        return 0.0

    @staticmethod
    def _get_antonyms(components):
        antonyms = []
        for words in components:
            for word in words.split(" "):
                ants = " ".join(list(get_anotnyms_dam3(word)))
                antonyms.append(ants)
        return antonyms

    @staticmethod
    def _get_entailement(text1, text2):
        return get_entailement(text1, text2)

    @staticmethod
    def _get_functional_components_dam3(p1p2):
        return get_functional_componenets_dam3(p1p2)

    @staticmethod
    def _get_argument_relation_decomp(entailemt, antonymys_asp_p, antonymys_asp_c, antonymys_tc_p, antonymys_tc_c,
                                      sim_asp_conclusion_asp_premise, sim_tc_conclusion_asp_premise,
                                      sim_tc_conclusion_premise, sim_asp_conclusion_tc_premise,
                                      merged_tc_c, merged_tc_p, merged_asp_p, merged_asp_c):
        arg_rel2 = "None"

        if sim_feature(sim_tc_conclusion_premise) and entailemt[0] > 75 and \
                sim_feature(sim_asp_conclusion_asp_premise):
            arg_rel2 = "RA"
        elif sim_feature(sim_tc_conclusion_premise) and entailemt[0] < 40 and \
                sim_feature(sim_asp_conclusion_asp_premise):
            arg_rel2 = "CA"
        elif sim_feature(sim_tc_conclusion_premise) and entailemt[0] > 75:
            arg_rel2 = "RA"
        elif sim_feature(sim_asp_conclusion_tc_premise) and entailemt[0] > 75:
            arg_rel2 = "RA"
        elif sim_feature(sim_asp_conclusion_asp_premise) and entailemt[0] < 40:
            arg_rel2 = "CA"
        elif sim_feature(sim_asp_conclusion_asp_premise) and entailemt[0] > 75:
            arg_rel2 = "RA"

        elif sim_feature(sim_asp_conclusion_asp_premise) and entailemt[0] > 75:
            arg_rel2 = "RA"

        elif sim_feature(sim_tc_conclusion_asp_premise) and entailemt[0] > 75:
            arg_rel2 = "RA"

        elif sim_feature(sim_tc_conclusion_premise) and entailemt[0] > 55 and \
                ArgumentRelationAnalyzer._are_anotnyms(antonymys_asp_c, merged_asp_p):
            arg_rel2 = "CA"

        elif sim_feature(sim_asp_conclusion_asp_premise) and entailemt[0] > 55 and \
                ArgumentRelationAnalyzer._are_anotnyms(antonymys_tc_c, merged_tc_p):
            arg_rel2 = "CA"

        else:
            arg_rel2 = "None"

        return arg_rel2

    @staticmethod 
    def _are_anotnyms(string1,string2):
        if len(string1)==0 or len(string2)==0:
            return False
        for word in string1:
            if word in string2:
                return True
        return False
            





