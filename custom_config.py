#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-06-24 23:06
# describe：



frame_count = 8 * 25

config_stage_2_template = {
    "models": {
        "model_list": [
            "models/stable_diffusion/aingdiffusion_v12.safetensors",
            "models/AnimateDiff/mm_sd_v15_v2.ckpt",
            "models/ControlNet/control_v11f1e_sd15_tile.pth",
            "models/ControlNet/control_v11p_sd15_lineart.pth"
        ],
        "textual_inversion_folder": "models/textual_inversion",
        "device": "cuda",
        "lora_alphas": [],
        "controlnet_units": [
            {
                "processor_id": "tile",
                "model_path": "models/ControlNet/control_v11f1e_sd15_tile.pth",
                "scale": 0.5
            },
            {
                "processor_id": "lineart",
                "model_path": "models/ControlNet/control_v11p_sd15_lineart.pth",
                "scale": 0.5
            }
        ]
    },
    "data": {
        "input_frames": {
            "video_file": ".cache/input_video.mp4",
            "image_folder": None,
            "height": 1024,
            "width": 1024,
            "start_frame_id": 0,
            "end_frame_id": frame_count
        },
        "controlnet_frames": [
            {
                "video_file": ".cache/input_video.mp4",
                "image_folder": None,
                "height": 1024,
                "width": 1024,
                "start_frame_id": 0,
                "end_frame_id": frame_count
            },
            {
                "video_file": ".cache/input_video.mp4",
                "image_folder": None,
                "height": 1024,
                "width": 1024,
                "start_frame_id": 0,
                "end_frame_id": frame_count
            }
        ],
        "output_folder": ".cache/output",
        "fps": 25
    },
    "pipeline": {
        "seed": 0,
        "pipeline_inputs": {
            "prompt": "best quality, perfect anime illustration, light, a girl is dancing, smile, solo",
            "negative_prompt": "verybadimagenegative_v1.3",
            "cfg_scale": 7.0,
            "clip_skip": 2,
            "denoising_strength": 1.0,
            "num_inference_steps": 10,
            "animatediff_batch_size": 16,
            "animatediff_stride": 8,
            "unet_batch_size": 1,
            "controlnet_batch_size": 1,
            "cross_frame_attention": False,
            # The following parameters will be overwritten. You don't need to modify them.
            "input_frames": [],
            "num_frames": frame_count,
            "width": 1536,
            "height": 1536,
            "controlnet_frames": []
        }
    }
}
