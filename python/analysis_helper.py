# -*- coding: utf-8 -*-


import os


analysis_dir = "./analysis"


DIFFICULTY = ['easy', 'moderate', 'hard']

FALSE_CASES = ['fns', 'fps', 'fps_bst', 'fns_bst']

result_dir = "./data"
label_dir = "~/Data/label/"

label_dir = os.path.expanduser(label_dir)


def InitPath():
    pass


def ListDir(dir_path):
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isfile(file_path):
            yield file_path
        elif os.path.isdir(file_path):
            for file_path in ListDir(file_path):
                yield file_path


def AnalysisIdxFile(file_path):
    box_idxs = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                continue
            box_idxs.append(int(line))
    return os.path.basename(file_path), box_idxs


def AnalysisBoxFile(box_file):
    # just str is enough
    boxes_str = []
    with open(box_file, "r") as f:
        for line in f.readlines():
            boxes_str.append(line.strip())

    return boxes_str


def SaveToFile(info, file_name):
    with open(file_name, "w") as f:
        f.write("\n".join(info))


def main():
    for difficulty in DIFFICULTY:
        for false_case in FALSE_CASES:
            tmp_dir = os.path.join(
                analysis_dir, "./", difficulty, "./", false_case)
            for tmp_file in ListDir(tmp_dir):
                basename, box_idxs = AnalysisIdxFile(tmp_file)

                if len(box_idxs) == 0:
                    # delete file if it is nothing
                    os.remove(tmp_file)
                    continue

                # find box infos in label dir or result dir according to box idx and img name
                # and write infos to file(inplace of old file)
                use_dir = label_dir if false_case == "fns" else result_dir
                boxes_file = os.path.join(use_dir, basename)
                boxes_str = AnalysisBoxFile(boxes_file)

                # select from box file
                selected_boxes = [boxes_str[box_idx] for box_idx in box_idxs]

                # save back to file(override)
                SaveToFile(selected_boxes, tmp_file)
main()
