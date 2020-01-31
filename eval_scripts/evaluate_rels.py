from brat_format import read_file
import os

true_dir = "test_1\\true_dir"
predict_dir = "test_1\\predict_dir"

ner_types = {"OUT", "ACT", "BIN", "CMP", "ECO", "INST", "MET", "SOC", "QUA"}
rel_types = {"NNG", "NNT", "NPS", "FNG", "FNT", "FPS", "PNG", "PNT", "PPS", "GOL", "TSK"}


def compute_precision_and_recall(true_positive, false_positive, false_negative):
    """
    Вычисляем точность и полноту по TP, FP и FN
    """
    if false_positive + true_positive > 0:
        precision = float(true_positive) / (true_positive + false_positive)
    else:
        precision = 0
    if false_negative + true_positive > 0:
        recall = float(true_positive) / (true_positive + false_negative)
    else:
        recall = 0
    return recall, precision


def cacl_rel_tp_fp_fn(true_data, pred_data):
    true_rels = true_data.relations
    true_ners = true_data.ners

    pred_rels = true_data.relations
    pred_ners = pred_data.ners

    true_positive = 0
    false_positive = 0
    false_negative = 0

    def find_rel(lh_rel, lh_ner_arr, rel_arr, ner_arr):
        for rh_rel in rel_arr:
            if lh_rel[0] != rh_rel:
                continue
            if (lh_ner_arr[lh_rel[1]] == ner_arr[rel_arr[1]] and lh_ner_arr[lh_rel[2]] == ner_arr[rel_arr[2]]) \
                or (lh_ner_arr[lh_rel[1]] == ner_arr[rel_arr[2]] and lh_ner_arr[lh_rel[2]] == ner_arr[rel_arr[1]]):
                return True
        return False

    for true_r in true_rels:
        if find_rel(true_r, true_ners, pred_rels, pred_ners):
            true_positive += 1
        else:
            false_negative += 1

    for pred_r in pred_rels:
        if not find_rel(pred_r, pred_ners, true_rels, true_ners):
            false_positive += 1

    return true_positive, false_positive, false_negative



total_tp = 0
total_fp = 0
total_fn = 0

for doc in os.listdir(true_dir):
    if doc.endswith(".ann"):
        true_doc = os.path.join(true_dir, doc)
        pred_doc = os.path.join(predict_dir, doc)

        true_data = read_file(true_doc)
        pred_data = read_file(pred_doc)

        if len(pred_data.relations) == 0:
            total_fn += len(true_data.relations)
            continue

        if len(true_data.relations) == 0:
            total_fp += len(pred_data.relations)
            continue

        tp, fp, fn = cacl_rel_tp_fp_fn(true_data, pred_data)

        print("{} : TP - {} / FP - {} / FN - {}".format(doc, tp, fp, fn))

        total_tp += tp
        total_fp += fp
        total_fn += fn

precision, recall = compute_precision_and_recall(total_tp, total_fp, total_fn)
f_measure = 2 * precision * recall / (precision + recall)
print("f_1: ", f_measure)
