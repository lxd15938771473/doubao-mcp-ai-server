import os
from volcenginesdkarkruntime import Ark
from volcenginesdkarkruntime.types.images.images import SequentialImageGenerationOptions

# 初始化 Ark 客户端，从环境变量中读取 API Key
client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=os.environ.get("ARK_API_KEY"),
)

# 调用文生图 API，只生成 1 张图片
imagesResponse = client.images.generate(
    model="doubao-seedream-4-0-250828",
    prompt="生成一张女孩在游乐园开心地坐过山车的图片",
    size="2K",
    sequential_image_generation="auto",
    sequential_image_generation_options=SequentialImageGenerationOptions(max_images=1),
    response_format="url",
    watermark=True
)

# 遍历所有图片数据
for image in imagesResponse.data:
    print(f"URL: {image.url}, Size: {image.size}")