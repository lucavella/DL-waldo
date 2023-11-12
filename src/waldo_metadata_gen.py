import sys
import os
import csv


if len(sys.argv) != 2:
    print("Please provide the root path.", file=sys.stderr)
    exit(-1)

root = sys.argv[1]
ann_fields = ['path', 'width', 'height', 'label']
img_dirs = ['64', '128']
out_path = 'waldo_metadata.csv'

with open(out_path, 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(ann_fields)

    for img_dir in img_dirs:
        dim = img_dir.split('-')[0]
        
        pos_dir = os.path.join(root, img_dir, 'waldo')
        for pos_file in os.listdir(pos_dir):
            pos_path = os.path.join(img_dir, 'waldo', pos_file)
            out_csv.writerow([pos_path, dim, dim, 1])

        neg_dir = os.path.join(root, img_dir, 'notwaldo')
        for neg_file in os.listdir(neg_dir):
            neg_path = os.path.join(img_dir, 'notwaldo', neg_file)
            out_csv.writerow([neg_path, dim, dim, 0])