#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-06-24 23:02
# describe：

import os
import time
import custom_config
from diffsynth import SDVideoPipelineRunner

start_date = time.time()

config = custom_config.config_stage_2_template.copy()
config["data"]["input_frames"] = {
    "video_file": ".cache/input_video.mp4",
    "image_folder": None,
    "height": 1024,
    "width": 1024,
    "start_frame_id": 0,
    "end_frame_id": custom_config.frame_count
}
config["data"]["controlnet_frames"] = [config["data"]["input_frames"], config["data"]["input_frames"]]
output_folder = ".cache/toon_video"
os.makedirs(output_folder, exist_ok=True)
config["data"]["output_folder"] = output_folder
config["data"]["fps"] = 25

runner = SDVideoPipelineRunner()
runner.run(config)

print(f"time space: {time.time() - start_date}")
print("all done")