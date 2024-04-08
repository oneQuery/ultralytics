"""
Format converter tools in `ultralytics`:
    - https://docs.ultralytics.com/reference/data/converter/#ultralytics.data.converter.convert_coco
"""

import argparse
import shutil
from glob import glob

from ultralytics.data.converter import yolo_bbox2segment


def get_args():
    parser = argparse.ArgumentParser(description="Convert COCO to YOLO OBB format")

    # fmt: off
    parser.add_argument('--img-dir', required=True, type=str, help='Directory containing images')
    parser.add_argument("--input-coco-dir", required=True, type=str, help="Directory containing COCO dataset")
    parser.add_argument("--output-yolo-obb-dir", required=True, type=str, help="Directory to save YOLO OBB dataset")
    # fmot: on

    args = parser.parse_args()
    return args


def main():
    args = get_args()

    img_dir = args.img_dir
    input_coco_dir = args.input_coco_dir
    output_yolo_obb_dir = args.output_yolo_obb_dir
    converted_coco_dir = "outputs/converted_coco"

    # COCO bbox to YOLO bbox
    # HACK: Temporal comment out to skip the conversion
    # convert_coco(
    #     labels_dir=input_coco_dir,
    #     save_dir=converted_coco_dir,
    # )

    # TODO: Check the directories
    # Copy images to the new directory
    converted_coco_dir_list = glob(f"outputs/converted_coco*")
    last_converted_coco_dir = converted_coco_dir_list[-1]
    img_copy_dir = f"{last_converted_coco_dir}/images"
    shutil.copy(img_dir, img_copy_dir)

    # TODO: YOLO bbox to YOLO OBB
    yolo_bbox2segment(im_dir=img_copy_dir, save_dir=output_yolo_obb_dir)


if __name__ == "__main__":
    main()
