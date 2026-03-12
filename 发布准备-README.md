# GitHub Skill Publisher

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](../../releases)

自动发布WorkBuddy技能到GitHub的一键工具

## 功能特性

- 一键生成所有GitHub发布所需文档
- 交互式向导，操作简单
- 支持命令行参数
- 自动生成README、LICENSE、SKILL.md等文档
- 创建GitHub模板文件（Issue、PR模板）
- 自动生成发布指南
- 支持多种开源协议
- 自动替换GitHub用户名，生成正确的仓库链接

## 安装说明

1. 下载 `github-skill-publisher.skill` 文件
2. 在WorkBuddy中安装技能
3. 根据README中的说明配置和使用

## 使用示例

### 基础使用

```bash
# 运行技能
python skills/github-skill-publisher/scripts/main.py --help
```

## 文档

- [技能详细文档](SKILL.md)
- [更新日志](CHANGELOG.md)
- [问题反馈](../../issues)

## 开源协议

本项目采用 MIT License - 查看 [LICENSE](LICENSE) 文件了解详情

## 贡献

欢迎提交 Issue 和 Pull Request！

## 作者

WorkBuddy Team

---

## 快速开始

### 前置要求

- WorkBuddy 环境
- Python 3.7+ （如技能需要）

### 安装

1. 下载最新版本的 `github-skill-publisher.skill`
2. 在WorkBuddy中导入安装
3. 重启WorkBuddy使技能生效

### 配置

```
# 配置示例（如需要）
config setting value
```

## 常见问题

### 问题1：技能无法加载？

**解答**：检查技能文件是否完整，WorkBuddy版本是否兼容。

### 问题2：运行出错？

**解答**：查看错误日志，确认依赖项是否已安装。

## 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本更新历史。

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 联系方式

- GitHub Issues: [提交问题](../../issues)
- 作者: WorkBuddy Team
