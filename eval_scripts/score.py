# encoding=utf-8
import sys
import os

from evaluate_ners import calc_ner_f1
from evaluate_rels import calc_rels_f1

def eval_ners(true_dir, pred_dir):
    return calc_ner_f1(true_dir, pred_dir)


def eval_rels(true_dir, pred_dir):
    return calc_rels_f1(true_dir, pred_dir)


if __name__ == "__main__":
    output_stream = sys.stdout

    # if len(sys.argv) == 1:
    # else:
    # true_dir = os.path.join(sys.argv[1], "ref")
    # predict_dir = os.path.join(sys.argv[1], "res")
    true_dir = "test_pred\\ref"
    predict_dir = "test_pred\\res"

    if not os.path.exists(sys.argv[2]):
        os.mkdir(sys.argv[2])
    output_stream = open(os.path.join(sys.argv[2], "scores.txt"), "w")


    set_1_dir = os.path.join(predict_dir, "set_1")
    set_2_dir = os.path.join(predict_dir, "set_2")
    set_3_dir = os.path.join(predict_dir, "set_3")

    set_1_score = 0.0
    set_2_score = -1.0
    set_3_score = 0.0

    # Дорожка NER
    if not os.path.exists(set_1_dir) or len(os.listdir(set_1_dir)) == 0:
        set_1_score = 0.0
    else:
        set_1_score = eval_ners(true_dir, set_1_dir)

    # # Дорожка RE с сущностями
    # if  not os.path.exists(set_2_dir) or len(os.listdir(set_2_dir)) == 0:
    #     set_2_score = 0.0
    # else:
    #     set_2_score = evaluate_rels(os.path.join(true_dir, "set_2"), set_2_dir)

    # End-to-end RE
    if not os.path.exists(set_3_dir) or len(os.listdir(set_3_dir)) == 0:
        set_3_score = 0.0
    else:
        set_3_score = eval_rels(true_dir, set_3_dir)

    # print(set_1_score, set_3_score)

    output_stream.write("set_1_score: %0.12f\n" % set_1_score)
    output_stream.write("set_2_score: %0.12f\n" % set_2_score)
    output_stream.write("set_3_score: %0.12f\n" % set_3_score)

    output_stream.close()
