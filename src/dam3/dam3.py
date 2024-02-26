from features_map import ArgumentRelationAnalyzer
from src.data import Data, AIF
from src.templates import DAMOutput

class DAM3:
    def __init__(self):
        pass
    @staticmethod
    def get_argument_structure(file_obj):
        data = Data(file_obj)
        propositions_id_pairs = {}
        if not data.is_json(): 	
            return "Invalid Input"
        extended_json_aif = data.get_aif()
        json_aif = extended_json_aif['AIF']
        if 'nodes' not in json_aif or 'locutions' not in json_aif or 'edges' not in json_aif:
            return "Invalid json-aif"
        edges, nodes = json_aif['edges'], json_aif['nodes']
        for node in nodes:
            if node.get('type') == "I":
                proposition = node.get('text', '').strip()
                if proposition:
                    node_id = node.get('nodeID')
                    propositions_id_pairs[node_id] = proposition
        checked_pairs = set()
        for prop1_node_id, prop1 in propositions_id_pairs.items():
            for prop2_node_id, prop2 in propositions_id_pairs.items():
                if prop1_node_id != prop2_node_id:
                    pair1 = (prop1_node_id, prop2_node_id)
                    pair2 = (prop2_node_id, prop1_node_id)
                    if pair1 not in checked_pairs and pair2 not in checked_pairs:
                        checked_pairs.add(pair1)
                        checked_pairs.add(pair2)
                    prediction = ArgumentRelationAnalyzer.get_argument_relation((prop1, prop2)) 
                    nodes, edges = AIF.create_entry(nodes, edges, prediction, prop1_node_id, prop2_node_id)
        return DAMOutput.format_output(nodes, edges, json_aif, extended_json_aif)

	

