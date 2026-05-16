# Local AI Note CLI
一款轻量、开源的本地AI笔记管理工具，基于OpenAI Embedding和FAISS向量检索，实现笔记的语义化搜索和管理。

## 项目简介
Local AI Note CLI 是为开发者设计的命令行笔记工具，支持快速添加笔记、语义搜索和标签管理。所有数据存储在本地，保护隐私，同时利用AI技术提升笔记检索效率。

## 为什么做这个项目
我自己平时习惯用命令行记笔记，但现有的工具要么太重（如Obsidian、Notion），要么没有语义搜索功能。传统的关键词搜索经常找不到我想要的笔记，所以我开发了这个轻量工具，专门解决开发者快速记笔记和智能检索的需求。

目前我自己每天都在使用这个工具，后续会根据自己的使用体验持续迭代优化。

## 主要功能
- ✅ 快速添加笔记，支持多标签
- ✅ 语义化搜索，比传统关键词搜索更准确
- ✅ 所有数据本地存储，不上传云端
- ✅ 轻量无冗余依赖，跨平台可用
- ✅ 简洁的命令行界面，适合开发者使用
- ✅ 笔记删除和列表查看功能

## 技术栈
- Python 3.8+
- OpenAI Embedding API
- FAISS 向量数据库
- Click 命令行框架

## 安装与使用
### 安装
```bash
git clone https://github.com/yangg881/local-ai-note-cli.git
cd local-ai-note-cli
pip install -r requirements.txt
