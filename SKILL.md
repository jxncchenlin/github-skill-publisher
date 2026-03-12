# GitHub Skill Publisher

**自动发布WorkBuddy技能到GitHub**

将您的WorkBuddy技能一键发布到GitHub，自动准备所有必需的文档和配置，让您只需简单几步即可完成专业级开源发布。

## 功能特性

- ✅ **自动化文档生成**：自动生成README、LICENSE、配置文件
- ✅ **智能文件组织**：自动整理项目结构
- ✅ **版本管理**：支持语义化版本号
- ✅ **Git初始化**：自动执行Git命令
- ✅ **多上传方式**：支持Git、Codespaces、CLI
- ✅ **发布包准备**：自动打包.skill文件
- ✅ **模板定制**：支持自定义发布模板

## 安装说明

将此文件保存为：
```
skills/github-skill-publisher/SKILL.md
skills/github-skill-publisher/scripts/publisher.py
```

## 使用方法

### 方式一：完整自动化发布（推荐）

```bash
python skills/github-skill-publisher/scripts/publisher.py
```

### 方式二：分步引导模式

```bash
python skills/github-skill-publisher/scripts/publisher.py --guide
```

### 方式三：仅生成文档

```bash
python skills/github-skill-publisher/scripts/publisher.py --docs-only
```

## 参数说明

| 参数 | 说明 | 必需 |
|------|------|------|
| `--name` | 技能名称 | 是 |
| `--desc` | 技能描述 | 是 |
| `--version` | 版本号（默认v1.0.0） | 否 |
| `--author` | 作者名称 | 否 |
| `--license` | 开源协议（默认MIT） | 否 |
| `--style` | README风格（modern/classic） | 否 |
| `--guide` | 启用交互式引导 | 否 |
| `--docs-only` | 仅生成文档 | 否 |
| `--help` | 显示帮助信息 | 否 |

## 使用示例

### 基础使用

```bash
# 完整发布流程
python skills/github-skill-publisher/scripts/publisher.py \
  --name "md-to-wechat" \
  --desc "将Markdown转换为微信公众号格式" \
  --author "YourName" \
  --version "1.0.0"
```

### 交互式模式

```bash
# 启动交互式向导
python skills/github-skill-publisher/scripts/publisher.py --guide
```

系统会逐步询问：
1. 技能名称
2. 技能描述
3. 版本号
4. 作者信息
5. 开源协议
6. 功能特性
7. 安装步骤
8. 使用示例

### 自定义模板

```bash
# 使用现代风格README
python skills/github-skill-publisher/scripts/publisher.py \
  --name "my-skill" \
  --desc "我的技能" \
  --style modern
```

## 输出文件

运行后会生成以下文件结构：

```
your-skill/
├── README.md                    # 项目说明（自动生成）
├── LICENSE                      # 开源协议（自动生成）
├── .gitignore                   # Git忽略配置（自动生成）
├── SKILL.md                     # 技能文档（自动生成）
├── CHANGELOG.md                 # 版本日志（自动生成）
├── your-skill.skill             # 技能包（自动打包）
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md        # Bug报告模板（自动生成）
│   │   └── feature_request.md   # 功能请求模板（自动生成）
│   └── pull_request_template.md # PR模板（自动生成）
└── scripts/
    └── publisher.log            # 发布日志
```

## 发布流程

### 自动化流程

1. **📋 信息收集**：收集技能元数据
2. **📝 文档生成**：自动生成所有文档
3. **📦 文件打包**：创建技能包
4. **🗂️ 结构整理**：组织GitHub标准结构
5. **⚙️ Git初始化**：初始化Git仓库
6. **📤 准备上传**：生成上传指南

### 用户操作（仅需3步）

#### 第1步：创建GitHub仓库

1. 访问 https://github.com/new
2. 填写仓库名称（系统会自动提示）
3. 选择公开仓库
4. 点击"Create repository"
5. **不要初始化README**

#### 第2步：上传文件（选择一种方式）

**方式A：GitHub Codespaces（推荐，无需Git）**
1. 在仓库页面点击"Code" → "Codespaces" → "Create codespace"
2. 在Codespaces中点击"Add files" → "Upload files"
3. 选择所有生成的文件
4. 打开终端执行：
   ```bash
   git add .
   git commit -m "Initial release"
   git push
   ```

**方式B：拖拽上传（最简单）**
1. 在仓库页面点击"uploading an existing file"
2. 直接拖拽所有文件到浏览器
3. 填写提交信息："Initial release"
4. 点击"Commit changes"

**方式C：本地Git命令**
```bash
cd your-skill-directory
git init
git add .
git commit -m "Initial release"
git remote add origin https://github.com/username/repo.git
git branch -M main
git push -u origin main
```

#### 第3步：创建Release

1. 在仓库页面点击"Releases" → "Draft a new release"
2. 输入版本号（如v1.0.0），点击空白处触发"Create new tag"
3. 系统会自动填充发布标题和描述
4. 上传 `.skill` 文件
5. 点击"Publish release"

完成！🎉

## 高级功能

### 自定义README模板

创建自定义模板文件 `custom-readme-template.md`：

```bash
python skills/github-skill-publisher/scripts/publisher.py \
  --name "my-skill" \
  --template custom-readme-template.md
```

### 批量发布多个技能

创建配置文件 `batch-publish.json`：

```json
{
  "skills": [
    {
      "name": "skill-one",
      "desc": "技能一描述"
    },
    {
      "name": "skill-two",
      "desc": "技能二描述"
    }
  ]
}
```

运行批量发布：

```bash
python skills/github-skill-publisher/scripts/publisher.py \
  --batch batch-publish.json
```

### 更新已有技能

```bash
python skills/github-skill-publisher/scripts/publisher.py \
  --name "my-skill" \
  --update \
  --version "1.1.0"
```

## 交互式引导示例

```
$ python skills/github-skill-publisher/scripts/publisher.py --guide

🚀 GitHub Skill Publisher - 交互式向导
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

第1步：基本信息

📝 请输入技能名称: md-to-wechat

📝 请输入技能描述（1-2句话）:
将Markdown转换为微信公众号格式

✓ 技能名称: md-to-wechat
✓ 技能描述: 将Markdown转换为微信公众号格式
✓ 版本号: v1.0.0
✓ 作者: YourName
✓ 开源协议: MIT License

继续吗？(Y/n): Y

第2步：功能特性

📝 请列出3-5个核心功能（每行一个）:
1. 三种主题风格
2. 一键转换
3. 批量处理
4. 完美适配公众号

✓ 功能特性已添加

第3步：安装说明

📝 安装步骤（系统会自动生成标准模板）:
- 下载skill包
- 在WorkBuddy中安装
- 运行命令

✓ 安装说明已生成

第4步：生成文档

📄 正在生成 README.md... ✓
📄 正在生成 LICENSE... ✓
📄 正在生成 SKILL.md... ✓
📄 正在生成 .gitignore... ✓
📄 正在生成模板文件... ✓
📦 正在打包技能... ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎉 发布准备完成！

📦 生成的文件：
  - README.md (项目说明)
  - LICENSE (MIT License)
  - SKILL.md (技能文档)
  - .gitignore (Git配置)
  - md-to-wechat.skill (技能包)
  - .github/ (模板文件)

📋 下一步操作：
  1. 创建GitHub仓库
  2. 上传文件（拖拽或Codespaces）
  3. 创建Release v1.0.0

💡 详细指南已保存到：github-publish-guide.md

查看指南？(Y/n): Y
[显示详细上传指南]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 支持的开源协议

- MIT License（推荐，最宽松）
- Apache 2.0
- GPL v3
- BSD 3-Clause
- Mozilla Public License 2.0

## 常见问题

**Q: 生成的文档可以修改吗？**
A: 可以！所有生成的文档都是Markdown格式，您可以随意编辑和定制。

**Q: 如何添加截图？**
A: 在README.md中手动添加图片链接，使用标准Markdown语法：
```markdown
![功能演示](screenshots/demo.png)
```

**Q: 支持私有仓库吗？**
A: 完全支持，发布流程完全相同。

**Q: 如何更新版本？**
A: 使用 `--update` 参数，系统会自动更新版本号和文档。

**Q: 可以自定义Git提交信息吗？**
A: 可以，编辑生成的 `commit-message.txt` 文件。

## 配置文件

创建 `publisher-config.json` 以保存默认配置：

```json
{
  "author": "YourName",
  "license": "MIT",
  "style": "modern",
  "default_branch": "main",
  "include_badges": true,
  "include_screenshots": true
}
```

## 日志和调试

所有操作会记录到 `scripts/publisher.log`：

```bash
# 查看日志
cat scripts/publisher.log

# 启用详细模式
python skills/github-skill-publisher/scripts/publisher.py --verbose
```

## 贡献指南

欢迎改进此技能！您可以：

- 添加新的README模板
- 支持更多开源协议
- 优化交互式引导
- 添加新的功能特性

## 许可证

MIT License - 自由使用、修改和分发

## 致谢

感谢以下项目：
- GitHub REST API
- Python packaging tools
- WorkBuddy community

---

**开始使用：**
```bash
python skills/github-skill-publisher/scripts/publisher.py --guide
```

让发布变得简单！🚀
