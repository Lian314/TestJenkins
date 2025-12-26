# 使用一个轻量级的官方 Python 基础镜像
FROM python:3.11-slim

# 设置在容器内部的工作目录
WORKDIR /app

# 先将依赖清单文件复制到工作目录（利用Docker的缓存机制，提高重建速度）
COPY requirements.txt .

# 安装项目依赖（使用国内镜像源可加速下载）
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 将当前目录下的所有文件复制到容器的 /app 目录下
COPY . .

# 声明容器运行时监听的端口（您的测试脚本可能不需要，但这是一个好习惯）
# EXPOSE 5000

# 定义容器启动后要执行的命令：运行单元测试
CMD ["python", "-m", "unittest", "discover", "-v"]