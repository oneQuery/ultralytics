"""
Format converter tools in `ultralytics`:
    - https://docs.ultralytics.com/reference/data/converter/#ultralytics.data.converter.convert_coco
"""

import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Convert COCO to YOLO OBB format")

    # fmt: off
    parser.add_argument("--input-coco-dir", required=True, type=str, help="Directory containing COCO dataset")
    parser.add_argument("--output-yolo-obb-dir", required=True, type=str, help="Directory to save YOLO OBB dataset")
    # fmot: on

    args = parser.parse_args()
    return args


def main():
    args = get_args()

    input_coco_dir = args.input_coco_dir
    output_yolo_obb_dir = args.output_yolo_obb_dir

    # TODO: COCO segments to YOLO bbox
    # convert_coco()

    # TODO: YOLO bbox to YOLO OBB
    # yolo_bbox2segment()


if __name__ == "__main__":
    main()
