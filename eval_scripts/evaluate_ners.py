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


def cacl_ner_tp_fp_fn(true_ners, pred_ners):
    # A - концы true, B - концы red, С - совпадение
    # C C  = TP + 1
    # A A B B | A B C | A B A B = FN + 1, advance A
    # B B A A | B A C | B A B A = FP + 1, advance B
    # C A B | C B A = FP + 1, FN + 1, advance A and B

    true_positive = 0
    false_positive = 0
    false_negative = 0

    i = 0
    j = 0
    while i != len(true_ners) and j != len(pred_ners):
        if true_ners[i] == pred_ners[j]:
            true_positive += 1
            i += 1
            j += 1
            continue
        if true_ners[i][1] >= pred_ners[j][2]:
            false_positive += 1
            j += 1
            continue
        if true_ners[i][2] <= pred_ners[j][1]:
            false_negative += 1
            i += 1
            continue
        if true_ners[i][1] < pred_ners[j][1]:
            false_negative += 1
            i += 1
            continue
        if true_ners[i][1] > pred_ners[j][1]:
            false_positive += 1
            i += 1
            continue

        false_positive += 1
        false_negative += 1
        j += 1
        i += 1

    false_negative += len(true_ners) - i
    false_positive += len(pred_ners) - j

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

        true_ners = sorted(true_data.ners, key=lambda x: x[1])
        pred_ners = sorted(pred_data.ners, key=lambda x: x[1])

        tp, fp, fn = cacl_ner_tp_fp_fn(true_ners, pred_ners)

        print("{} : TP - {} / FP - {} / FN - {}".format(doc, tp, fp, fn))

        total_tp += tp
        total_fp += fp
        total_fn += fn

precision, recall = compute_precision_and_recall(total_tp, total_fp, total_fn)
f_measure = 2 * precision * recall / (precision + recall)
print("f_1: ", f_measure)

# """
# true : <BIN> Создание <BIN> <ECO> новых рабочих мест <ECO> необходимо <BIN> производить релугярно <BIN> в рамках <ACT> программы поддержки населения <ACT>.
# pred : <BIN> Создание <BIN> новых <ECO> рабочих мест <ECO> необходимо <BIN> производить <BIN> релугярно в рамках программы поддержки <ACT> населения <ACT>.
# TP = 1, FP = 3, FN = 3
# """
