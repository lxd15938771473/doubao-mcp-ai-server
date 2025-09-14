# Doubao MCP AI Server

本项目基于 FastMCP 框架，提供 AI 文生图、图生视频、文生视频等多种 AI 能力的 MCP 服务接口，适用于自动化、AI 助手、智能内容生成等场景。

## 功能简介
- 文本生成图片（文生图）
- 图片生成视频（图生视频）
- 文本生成视频（文生视频）
- 支持 API 密钥动态配置
- 支持多种模型和参数灵活调用

## 运行 MCP 服务器

### 1. 构建 Docker 镜像
```bash
docker build -t doubao-mcp-ai-server .
```

### 2. 启动 Docker 容器
```bash
docker rm -f doubao-mcp-ai-server; docker run -d -p 8000:8000 --name doubao-mcp-ai-server doubao-mcp-ai-server
```

容器启动后，MCP 服务将监听 0.0.0.0:8000，主机可通过 8000 端口访问。

### 3. 运行前请设置 API_KEY
服务启动后，请先通过 set_api_key 工具设置豆包 API 密钥，否则无法正常调用 AI 能力。

### 4. MCP 客户端配置示例
```json
{
  "mcpServers": {
    "doubao_mcp_ai_server": {
      "url": "https://127.0.0.1/sse",
      "type": "sse"
    }
  }
}
```
> 说明：如需公网访问，可使用 ngrok、frp 等工具将本地 8000 端口映射到公网。

## 依赖说明
- Python 3.10
- FastMCP
- openai
- requests

## 主要文件说明
- `doubao_mcp_ai_server.py`：主服务代码，定义了所有 AI 工具和接口
- `requirements.txt`：依赖包列表
- `Dockerfile`：Docker 镜像构建文件

## 其他
如需自定义模型、API 密钥或扩展功能，请参考代码注释进行修改。

---
如有问题欢迎反馈。
