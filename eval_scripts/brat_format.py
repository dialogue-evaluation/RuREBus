import codecs
import bisect
import os


class BratDoc:
    def __init__(self, data):
        self.txt_data = data # Str
        self.relations = [] # List[Tuple[str, int, int]]
        self.ners = [] # List[Tuple[str, int, int]]

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

    def write_to_file(self, path):
        with codecs.open(path[:-3] + "txt", "w+", encoding="utf-8") as txt_out:
            txt_out.write(self.txt_data)

        with codecs.open(path, "w+", encoding="utf-8") as ann_out:
            for num, idx in self.ner_id_2_idx.items():
                ann_out.write("T{}\t{} {} {}\t{}\n".format(
                    num,
                    self.ners[idx][0],
                    self.ners[idx][1],
                    self.ners[idx][2],
                    self.txt_data[self.ners[idx][1]:self.ners[idx][2]].lstrip(),
                ))

            for num, idx in self.rel_id_2_idx.items():
                left_op = self.ner_id_2_idx[self.relations[idx][1]]
                right_op = self.ner_id_2_idx[self.relations[idx][2]]
                if '\n' in self.txt_data[self.ners[left_op][1]:self.ners[right_op][2]]:
                    continue
                ann_out.write("R{}\t{} Arg1:T{} Arg2:T{}\n".format(
                    num,
                    self.relations[idx][0],
                    self.relations[idx][1],
                    self.relations[idx][2],
                ))


def read_file(path, win_file=True):
    """
    :param path: "path/to/file.ann"
    :param win_file: \r\n counted in markup
    :return:
    """
    data = []
    with codecs.open(path, encoding="utf-8") as f_in:
        data = f_in.readlines()

    pure_txt = ""
    if os.path.exists(path[:-3] + "txt"):
        with codecs.open(path[:-3] + "txt", encoding="utf-8") as f_in:
            pure_txt = f_in.read()

    # deal with \r\n

    # lines_ends = []
    # with codecs.open(path[:-3] + "txt", encoding="utf-8") as f_in:
    #     lines_ends = [len(line.strip()) for line in f_in.readlines()]
    #     acc = 0
    #     for idx, end in enumerate(lines_ends):
    #         lines_ends[idx] += acc
    #         acc += end + 2

    # dec_mul = 0 #2 if win_file else 1

    ignored = dict()

    brat_doc = BratDoc(pure_txt)
    ner_list = []
    for line_num, line in enumerate(data):
        line = line.strip()
        if line.startswith("T"):
            # NER
            try:
                arr = line.split('\t')
                ner_id = arr[0]
                ner = arr[1] 
            except:
                print("Invalid relation format")
            if len(ner.split()) != 3:
                ner_id = int(ner_id[1:])
                if ner_id in ignored:
                    ignored[ner_id].append(ner_id)
                else:
                    ignored[ner_id] = [ner_id]
                continue
            nertype, start_idx, end_idx = ner.split()

            ner_id = int(ner_id[1:])
            start_idx = int(start_idx)
            end_idx = int(end_idx)

            # if '\n' in pure_txt[start_idx:end_idx]:
            #     if ner_id in ignored:
            #         ignored[ner_id].append(ner_id)
            #     else:
            #         ignored[ner_id] = [ner_id]
            #     continue

            # decrement = bisect.bisect_left(lines_ends, start_idx) * dec_mul
            # start_idx -= decrement
            # end_idx -= decrement

            ner_list.append((ner_id, nertype, start_idx, end_idx))

    ner_list.sort(key=lambda x: x[2])
    for (ner_id, nertype, start_idx, end_idx) in ner_list:
        brat_doc.add_ner(ner_id, nertype, start_idx, end_idx)

    for line_num, line in enumerate(data):
        line = line.strip()
        if line.startswith("R"):
            # Relation
            rel_id, rel = line.split('\t')
            reltype, arg1, arg2 = rel.split()

            rel_id = int(rel_id[1:])
            head_l = int(arg1[6:])
            head_r = int(arg2[6:])

            if head_l in ignored:
                if head_l in ignored[head_l]:
                    continue

            if head_r in ignored:
                if head_r in ignored[head_r]:
                    continue

            # assert head_l in brat_doc.ner_id_2_idx, "left arg not in dict {}".format(line_num)
            # assert head_r in brat_doc.ner_id_2_idx, "right arg not in dict {}".format(line_num)

            brat_doc.add_relation(rel_id, reltype, head_l, head_r)

    return brat_doc




