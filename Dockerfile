# 使用官方 Python 运行时作为父镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件和源码
COPY requirements.txt ./
COPY doubao_mcp_ai_server.py ./
# COPY doubao-seedream-4pro.py ./

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置容器启动时执行的命令
CMD ["python", "doubao_mcp_ai_server.py"]
