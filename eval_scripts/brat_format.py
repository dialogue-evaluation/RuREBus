import codecs
import bisect

class BratDoc:
    def __init__(self):
        self.relations = [] #List[Tuple[str, int, int]]
        self.ners = [] #List[Tuple[str, int, int]]

        self.rel_id_2_idx = dict()
        self.ner_id_2_idx = dict()

    def add_relation(self, rel_id, reltype, start_idx, end_idx):
        rel_idx = len(self.relations)
        self.rel_id_2_idx[rel_id] = rel_idx
        self.relations.append((reltype, start_idx, end_idx))

    def add_ner(self, ner_id, ner_type, head_l, head_r):
        ner_idx = len(self.ners)
        self.ner_id_2_idx[ner_id] = ner_idx
        self.ners.append((ner_type, head_l, head_r))

def read_file(path):
    data = []
    with codecs.open(path, encoding="utf-8") as f_in:
        data = f_in.readlines()

    brat_doc = BratDoc()
    for line in data:
        line = line.strip()
        if line.startswith("T"):
            # NER
            ner_id, ner, _ = line.split('\t')
            nertype, start_idx, end_idx = ner.split()

            ner_id = int(ner_id[1:])
            start_idx = int(start_idx)
            end_idx = int(end_idx)

            brat_doc.add_ner(ner_id, nertype, start_idx, end_idx)

        elif line.startswith("R"):
            # Relation
            rel_id, rel = line.split('\t')
            reltype, arg1, arg2 = rel.split()

            rel_id = int(rel_id[1:])
            head_l = int(arg1[6:])
            head_r = int(arg2[6:])

            assert head_l in brat_doc.ner_id_2_idx, "left arg not in dict"
            assert head_r in brat_doc.ner_id_2_idx, "right arg not in dict"

            brat_doc.add_relation(rel_id, reltype, head_l, head_r)

    return brat_doc




