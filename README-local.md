## 本次测试

用2080Ti（22g）测试了一下本地推理difftoon, 8秒的示例视频，需要2个多小时才能转换完毕，效率太低了。配置不够硬的情况下，玩玩就好。期望后续的推理提速。

### 环境配置
- 【推荐】使用vscode的`Dev Containers`模式，参考[.devcontainer/README.md](.devcontainer/README.md)

- 【可选】其他虚拟环境方式
    - 【二选一】安装torch-cpu版
        ```shell
        pip install torch torchvision
        ```
    - 【二选一】安装torch-cuda版
        ```shell
        pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
        ```
    - 【必要】安装依赖
        ```shell
        pip install -r requirements.txt


### 模型下载：
```shell
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/229575 -d /app/models/stable_diffusion -o aingdiffusion_v12.safetensors
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt -d /app/models/AnimateDiff -o mm_sd_v15_v2.ckpt
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart.pth -d /app/models/ControlNet -o control_v11p_sd15_lineart.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile.pth -d /app/models/ControlNet -o control_v11f1e_sd15_tile.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth.pth -d /app/models/ControlNet -o control_v11f1p_sd15_depth.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge.pth -d /app/models/ControlNet -o control_v11p_sd15_softedge.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/Annotators/resolve/main/dpt_hybrid-midas-501f0c75.pt -d /app/models/Annotators -o dpt_hybrid-midas-501f0c75.pt
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/Annotators/resolve/main/ControlNetHED.pth -d /app/models/Annotators -o ControlNetHED.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/Annotators/resolve/main/sk_model.pth -d /app/models/Annotators -o sk_model.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/Annotators/resolve/main/sk_model2.pth -d /app/models/Annotators -o sk_model2.pth
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M "https://civitai.com/api/download/models/25820?type=Model&format=PickleTensor&size=full&fp=fp16" -d /app/models/textual_inversion -o verybadimagenegative_v1.3.pt
aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/Diffutoon/resolve/main/input_video.mp4 -d /app/.cache -o input_video.mp4
```


### 跳过已存在的方式下载：
```shell
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M https://civitai.com/api/download/models/229575 -d /app/models/stable_diffusion -o aingdiffusion_v12.safetensors
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt -d /app/models/AnimateDiff -o mm_sd_v15_v2.ckpt
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart.pth -d /app/models/ControlNet -o control_v11p_sd15_lineart.pth
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile.pth -d /app/models/ControlNet -o control_v11f1e_sd15_tile.pth
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth.pth -d /app/models/ControlNet -o control_v11f1p_sd15_depth.pth
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge.pth -d /app/models/ControlNet -o control_v11p_sd15_softedge.pth
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/Annotators/resolve/main/dpt_hybrid-midas-501f0c75.pt -d /app/models/Annotators -o dpt_hybrid-midas-501f0c75.pt
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/Annotators/resolve/main/ControlNetHED.pth -d /app/models/Annotators -o ControlNetHED.pth
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/Annotators/resolve/main/sk_model.pth -d /app/models/Annotators -o sk_model.pth
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M https://huggingface.co/lllyasviel/Annotators/resolve/main/sk_model2.pth -d /app/models/Annotators -o sk_model2.pth
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M "https://civitai.com/api/download/models/25820?type=Model&format=PickleTensor&size=full&fp=fp16" -d /app/models/textual_inversion -o verybadimagenegative_v1.3.pt
aria2c --console-log-level=error --check-integrity --auto-file-renaming=false -c -x 16 -s 16 -k 1M https://huggingface.co/camenduru/Diffutoon/resolve/main/input_video.mp4 -d /app/.cache -o input_video.mp4
```


### 测试推理：
```shell
python diffutoon_demo.py
```

### 相关截图
![image](https://github.com/Samge0/DiffSynth-Studio/assets/17336101/7bbc0d9f-838a-46e2-a296-5c4e94ffae87)

![image](https://github.com/Samge0/DiffSynth-Studio/assets/17336101/8093318e-a793-4218-9ccf-d817c6116881)
