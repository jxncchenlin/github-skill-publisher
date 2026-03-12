#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Skill Publisher - 自动发布WorkBuddy技能到GitHub
"""

import os
import sys
import json
import shutil
import argparse
from datetime import datetime
from pathlib import Path

# 颜色输出
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    print(f"\n{Colors.HEADER}{text}{Colors.ENDC}")

def print_success(text):
    print(f"{Colors.OKGREEN}✓ {text}{Colors.ENDC}")

def print_info(text):
    print(f"{Colors.OKCYAN}ℹ {text}{Colors.ENDC}")

def print_warning(text):
    print(f"{Colors.WARNING}⚠ {text}{Colors.ENDC}")

def print_error(text):
    print(f"{Colors.FAIL}✗ {text}{Colors.ENDC}")

class GitHubSkillPublisher:
    def __init__(self, name, desc, version="1.0.0", author="", license_type="MIT",
                 style="modern", features=None, install_steps=None, usage_examples=None, github_username=""):
        self.name = name
        self.desc = desc
        self.version = version
        self.author = author or "YourName"
        self.github_username = github_username or "YOUR_USERNAME"  # GitHub用户名
        self.license_type = license_type
        self.style = style
        self.features = features or []
        self.install_steps = install_steps or []
        self.usage_examples = usage_examples or []
        self.repo_name = name.lower().replace(' ', '-')

        # 创建输出目录
        self.output_dir = Path(self.repo_name)
        self.output_dir.mkdir(exist_ok=True)

        # GitHub模板目录
        self.github_dir = self.output_dir / ".github" / "ISSUE_TEMPLATE"
        self.github_dir.mkdir(parents=True, exist_ok=True)

    def generate_readme(self):
        """生成README.md"""
        badges = f"""
![License](https://img.shields.io/badge/license-{self.license_type}-blue.svg)
![Version](https://img.shields.io/badge/version-{self.version}-green.svg)
"""

        features_list = "\n".join([f"- {f}" for f in self.features])
        if not self.features:
            features_list = "- [待添加]核心功能1\n- [待添加]核心功能2\n- [待添加]核心功能3"

        install_list = "\n".join([f"{i+1}. {step}" for i, step in enumerate(self.install_steps)])
        if not self.install_steps:
            install_list = """1. 下载 `{self.repo_name}.skill` 文件
2. 在WorkBuddy中安装技能
3. 根据README中的说明配置和使用"""

        usage_section = "\n".join([f"### {ex['title']}\n```\n{ex['code']}\n```" for ex in self.usage_examples])
        if not self.usage_examples:
            usage_section = """### 基础使用
\`\`\`
# 基本命令示例
python skills/{self.repo_name}/scripts/main.py --help
\`\`\`
"""

        readme_content = f"""# {self.name}

{badges}

{self.desc}

## 功能特性

{features_list}

## 安装说明

{install_list}

## 使用示例

{usage_section}

## 文档

- [技能详细文档](SKILL.md)
- [更新日志](CHANGELOG.md)
- [问题反馈](../../issues)

## 开源协议

本项目采用 {self.license_type} License - 查看 [LICENSE](LICENSE) 文件了解详情

## 贡献

欢迎提交 Issue 和 Pull Request！

## 作者

{self.author}

---

## 快速开始

### 前置要求

- WorkBuddy 环境
- Python 3.7+ （如技能需要）

### 安装

1. 下载最新版本的 `{self.repo_name}.skill`
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

{self.license_type} License - 详见 [LICENSE](LICENSE)

## 联系方式

- GitHub Issues: [提交问题](../../issues)
- 作者: {self.author}
"""

        readme_path = self.output_dir / "README.md"
        readme_path.write_text(readme_content, encoding='utf-8')
        print_success(f"README.md 已生成")

    def generate_license(self):
        """生成LICENSE文件"""
        licenses = {
            "MIT": """MIT License

Copyright (c) {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""",
            "Apache-2.0": """Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.""",
            "GPL-3.0": """GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) {year} {author}

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
        }

        license_content = licenses.get(self.license_type, licenses["MIT"])
        license_content = license_content.format(
            year=datetime.now().year,
            author=self.author
        )

        license_path = self.output_dir / "LICENSE"
        license_path.write_text(license_content, encoding='utf-8')
        print_success(f"LICENSE 已生成 ({self.license_type})")

    def generate_skill_md(self):
        """生成SKILL.md"""
        skill_md_content = f"""# {self.name} - 技能文档

## 概述

{self.desc}

## 技能版本

当前版本: **v{self.version}**
发布日期: {datetime.now().strftime('%Y-%m-%d')}

## 功能说明

### 核心功能

{chr(10).join([f'### {i+1}. {f}' for i, f in enumerate(self.features)]) if self.features else '请添加核心功能说明'}

### 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| --help | 显示帮助信息 | - |
| --version | 显示版本信息 | - |

## 安装指南

### 下载安装

1. 从 [GitHub Releases](../../releases) 下载最新的 `{self.repo_name}.skill`
2. 在WorkBuddy中导入技能文件
3. 重启WorkBuddy

### 手动安装

克隆仓库后，将技能文件夹复制到WorkBuddy的skills目录：
```
git clone https://github.com/{self.github_username}/{self.repo_name}.git
cp -r {self.repo_name} ~/.workbuddy/skills/
```

## 使用方法

### 基础用法

```bash
# 运行技能
python skills/{self.repo_name}/scripts/main.py

# 查看帮助
python skills/{self.repo_name}/scripts/main.py --help
```

### 高级用法

```bash
# 自定义参数
python skills/{self.repo_name}/scripts/main.py --option value

# 批量处理
python skills/{self.repo_name}/scripts/main.py --batch input.txt
```

## 配置选项

创建配置文件 `config.json`:
```json
{{
  "setting1": "value1",
  "setting2": "value2"
}}
```

## 常见问题

### Q1: 技能无法加载?

**A**: 检查以下几点：
- 技能文件是否完整
- WorkBuddy版本是否兼容
- 依赖项是否已安装

### Q2: 如何更新技能?

**A**: 下载新版本的.skill文件，覆盖安装即可。

### Q3: 技能支持哪些平台?

**A**: 支持所有WorkBuddy支持的操作系统。

## 故障排除

### 日志查看

技能运行日志保存在：
```
logs/{self.repo_name}.log
```

### 调试模式

启用详细输出：
```bash
python skills/{self.repo_name}/scripts/main.py --verbose
```

## 版本历史

查看 [CHANGELOG.md](CHANGELOG.md) 了解详细更新记录。

## 贡献指南

欢迎贡献代码！请：
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

{self.license_type} License - 详见 [LICENSE](LICENSE)

## 联系方式

- 作者: {self.author}
- GitHub Issues: [提交问题](../../issues)
- 文档: https://github.com/{self.github_username}/{self.repo_name}/wiki

---

**最后更新**: {datetime.now().strftime('%Y-%m-%d')}
"""

        skill_md_path = self.output_dir / "SKILL.md"
        skill_md_path.write_text(skill_md_content, encoding='utf-8')
        print_success(f"SKILL.md 已生成")

    def generate_gitignore(self):
        """生成.gitignore"""
        gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# WorkBuddy
.workbuddy/
*.log
logs/
temp/
tmp/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Custom
config.local.json
.env
.env.local
"""

        gitignore_path = self.output_dir / ".gitignore"
        gitignore_path.write_text(gitignore_content, encoding='utf-8')
        print_success(f".gitignore 已生成")

    def generate_changelog(self):
        """生成CHANGELOG.md"""
        changelog_content = f"""# 更新日志

所有项目变更都将记录在此文件中。

## [{self.version}] - {datetime.now().strftime('%Y-%m-%d')}

### 新增
- 初始版本发布
- 核心功能实现
- 基础文档完善

### 功能
- {chr(10).join([f'- {f}' for f in self.features]) if self.features else '- 基础功能'}

### 文档
- README.md
- SKILL.md
- LICENSE
- CHANGELOG.md

## [未发布]

### 计划中
- [ ] 功能增强
- [ ] 性能优化
- [ ] 文档完善

---

**版本格式**: `[主版本.次版本.修订号]`
- 主版本：不兼容的API修改
- 次版本：向下兼容的功能新增
- 修订号：向下兼容的问题修正
"""

        changelog_path = self.output_dir / "CHANGELOG.md"
        changelog_path.write_text(changelog_content, encoding='utf-8')
        print_success(f"CHANGELOG.md 已生成")

    def generate_github_templates(self):
        """生成GitHub模板文件"""
        # Bug报告模板
        bug_report = """---
name: Bug report
about: Create a report to help us improve
title: '[BUG] '
labels: bug
assignees: ''

---

**描述bug**
清晰简洁地描述bug是什么。

**复现步骤**
1. 执行 '...'
2. 点击 '....'
3. 滚动到 '....'
4. 看到错误

**期望行为**
清晰简洁地描述你期望发生什么。

**截图**
如果适用，添加截图以帮助解释你的问题。

**环境信息**
 - WorkBuddy版本: [例如: 1.0.0]
 - 操作系统: [例如: Windows 10]
 - Python版本: [例如: 3.8]

**附加信息**
在此添加任何其他关于问题的信息。
"""

        bug_report_path = self.github_dir / "bug_report.md"
        bug_report_path.write_text(bug_report, encoding='utf-8')

        # 功能请求模板
        feature_request = """---
name: Feature request
about: Suggest an idea for this project
title: '[FEATURE] '
labels: enhancement
assignees: ''

---

**你的功能请求是否与问题相关？**
清晰简洁地描述问题。例如：我总是因为……而感到困扰

**描述你想要的解决方案**
清晰简洁地描述你希望发生什么。

**描述你考虑过的替代方案**
清晰简洁地描述你考虑过的任何替代解决方案或功能。

**附加信息**
在此添加任何其他关于功能请求的信息或截图。
"""

        feature_request_path = self.github_dir / "feature_request.md"
        feature_request_path.write_text(feature_request, encoding='utf-8')

        # PR模板
        pr_template = """---
about: '开始前请检查PR清单！'
title: ''
labels: ''
assignees: ''
---

## 描述
PR的简要描述

## 类型
- [ ] Bug修复 (修复问题)
- [ ] 新功能 (增加功能)
- [ ] 破坏性更改 (破坏性变更)
- [ ] 文档 (文档更新)

## 测试
- [ ] 测试已通过
- [ ] 新增测试用例

## 检查清单
- [ ] 代码符合项目的代码风格
- [ ] 已进行自我代码审查
- [ ] 已注释难以理解的代码
- [ ] 已更新相应的文档
- [ ] 无新的警告产生

## 截图（如适用）
在此添加截图
"""

        pr_template_path = self.output_dir / ".github" / "pull_request_template.md"
        pr_template_path.parent.mkdir(exist_ok=True)
        pr_template_path.write_text(pr_template, encoding='utf-8')

        print_success(f"GitHub模板已生成")

    def generate_publish_guide(self):
        """生成发布指南"""
        guide_content = f"""# GitHub 发布指南

## 快速发布（3步完成）

### 第1步：创建GitHub仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - Repository name: **{self.repo_name}**
   - Description: {self.desc}
   - 选择 **Public**（公开仓库）
   - **不要**勾选 "Initialize this repository with a README"
3. 点击 "Create repository"

### 第2步：上传文件

#### 方式A：拖拽上传（最简单）⭐推荐
1. 在仓库页面点击 "uploading an existing file"
2. 将以下文件拖拽到浏览器：
   - README.md
   - LICENSE
   - SKILL.md
   - CHANGELOG.md
   - .gitignore
   - .github/ （整个文件夹）
   - {self.repo_name}.skill
3. 在提交信息框中输入：`Initial release`
4. 点击 "Commit changes"

#### 方式B：GitHub Codespaces（适合大文件）
1. 在仓库页面点击 "Code" → "Codespaces" → "Create codespace"
2. 点击 "Add files" → "Upload files"
3. 上传所有文件
4. 打开终端，执行：
   ```bash
   git add .
   git commit -m "Initial release"
   git push
   ```

#### 方式C：本地Git命令
```bash
cd {self.repo_name}
git init
git add .
git commit -m "Initial release"
git remote add origin https://github.com/{self.github_username}/{self.repo_name}.git
git branch -M main
git push -u origin main
```

### 第3步：创建Release

1. 在仓库页面点击 "Releases" → "Draft a new release"
2. 输入版本号：`v{self.version}`（点击空白处触发"Create new tag"）
3. 填写发布信息：
   - **Release title**: {self.name} v{self.version}
   - **Description**（最多350字符）:
     ```
     {self.desc} - WorkBuddy技能，版本v{self.version}
     功能：{chr(10).join([f for f in self.features[:2]]) if self.features else '基础功能'}
     下载{self.repo_name}.skill，在WorkBuddy中安装使用。
     ```
4. 上传资产文件：
   - 点击 "Attach binaries by dropping them here"
   - 选择 `{self.repo_name}.skill` 文件
5. 点击 "Publish release"

完成！🎉 您的技能已成功发布到GitHub！

---

## 验证发布

访问以下链接确认发布成功：
- 仓库主页: https://github.com/{self.github_username}/{self.repo_name}
- Release页面: https://github.com/{self.github_username}/{self.repo_name}/releases

## 后续维护

### 发布新版本
1. 修改版本号（如 v1.1.0）
2. 运行发布工具：`python publisher.py --update --version 1.1.0`
3. 更新CHANGELOG.md
4. 提交并推送到GitHub
5. 创建新的Release

### 回应用户反馈
- 定期检查GitHub Issues
- 及时回复用户问题
- 合并有价值的Pull Request

## 常见问题

**Q: Release描述超过350字符怎么办？**
A: 将详细内容放在README.md中，Release描述只保留核心信息。

**Q: 如何修改已发布的Release？**
A: 在Release页面点击"Edit release"进行修改。

**Q: 如何删除错误的Release？**
A: 在Release页面点击"Delete release"（这也会删除对应的tag）。

---

**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

        guide_path = self.output_dir / "github-publish-guide.md"
        guide_path.write_text(guide_content, encoding='utf-8')
        print_success(f"发布指南已生成")

    def create_skill_package(self):
        """创建技能包（模拟）"""
        # 这里应该是实际的打包逻辑
        # 示例中只是创建一个说明文件
        package_content = f"""WorkBuddy Skill Package
Name: {self.name}
Version: {self.version}
Description: {self.desc}

安装说明:
1. 将此文件重命名为 {self.repo_name}.skill
2. 在WorkBuddy中导入
3. 重启WorkBuddy
"""

        package_path = self.output_dir / f"{self.repo_name}.skill"
        package_path.write_text(package_content, encoding='utf-8')
        print_success(f"技能包已生成: {package_path.name}")

    def generate_all(self):
        """生成所有文件"""
        print_header(f"🚀 开始生成 GitHub 发布文件 - {self.name}")
        print(f"\n仓库名称: {self.repo_name}")
        print(f"版本: v{self.version}")
        print(f"作者: {self.author}")
        print(f"GitHub用户名: {self.github_username}")
        print(f"仓库地址: https://github.com/{self.github_username}/{self.repo_name}")
        print(f"开源协议: {self.license_type}")
        print(f"风格: {self.style}\n")

        print_header("📝 生成文档")

        self.generate_readme()
        self.generate_license()
        self.generate_skill_md()
        self.generate_gitignore()
        self.generate_changelog()
        self.generate_github_templates()
        self.generate_publish_guide()

        print_header("📦 打包文件")
        self.create_skill_package()

        print_header("✅ 生成完成")
        print(f"\n所有文件已保存到: {self.output_dir.absolute()}")
        print(f"\n下一步：")
        print(f"  1. 查看 github-publish-guide.md 获取详细发布步骤")
        print(f"  2. 访问 https://github.com/new 创建仓库")
        print(f"  3. 上传文件并创建 Release v{self.version}\n")

def interactive_mode():
    """交互式模式"""
    print(f"""
{Colors.HEADER}🚀 GitHub Skill Publisher - 交互式向导{Colors.ENDC}
{Colors.OKCYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.ENDC}
""")

    # 第1步：基本信息
    print(f"\n{Colors.BOLD}第1步：基本信息{Colors.ENDC}\n")

    name = input("📝 请输入技能名称: ").strip()
    while not name:
        print_error("技能名称不能为空")
        name = input("📝 请输入技能名称: ").strip()

    desc = input(f"📝 请输入技能描述（1-2句话）: ").strip()
    while not desc:
        print_error("技能描述不能为空")
        desc = input(f"📝 请输入技能描述（1-2句话）: ").strip()

    version = input(f"📝 请输入版本号（默认 v1.0.0）: ").strip() or "1.0.0"
    author = input(f"📝 请输入作者名称（默认 YourName）: ").strip() or "YourName"
    github_username = input(f"📝 请输入GitHub用户名（重要！用于生成仓库链接）: ").strip()
    while not github_username:
        print_warning("GitHub用户名很重要，请输入您的GitHub用户名（用于生成仓库链接）")
        github_username = input(f"📝 请输入GitHub用户名: ").strip()

    licenses = ["MIT", "Apache-2.0", "GPL-3.0", "BSD-3-Clause"]
    print(f"\n📝 选择开源协议:")
    for i, lic in enumerate(licenses, 1):
        print(f"  {i}. {lic}")
    license_choice = input(f"📝 请选择（默认 1-MIT）: ").strip() or "1"
    license_type = licenses[min(int(license_choice) - 1, 0)]

    print(f"\n{Colors.OKGREEN}✓ 技能名称: {name}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}✓ 技能描述: {desc}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}✓ 版本号: v{version}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}✓ 作者: {author}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}✓ GitHub用户名: {github_username}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}✓ 开源协议: {license_type}{Colors.ENDC}")

    confirm = input(f"\n{Colors.WARNING}继续吗？(Y/n): {Colors.ENDC}").strip().lower()
    if confirm == 'n':
        print_info("已取消")
        return

    # 第2步：功能特性
    print(f"\n{Colors.BOLD}第2步：功能特性{Colors.ENDC}\n")

    features = []
    print(f"📝 请列出3-5个核心功能（每行一个，空行结束）:")
    while True:
        feature = input(f"  {len(features) + 1}. ").strip()
        if not feature:
            break
        features.append(feature)

    if not features:
        print_warning("未输入功能特性，将使用默认模板")

    print(f"{Colors.OKGREEN}✓ 功能特性已添加 ({len(features)}个){Colors.ENDC}")

    # 生成所有文件
    publisher = GitHubSkillPublisher(
        name=name,
        desc=desc,
        version=version,
        author=author,
        github_username=github_username,
        license_type=license_type,
        features=features
    )

    publisher.generate_all()

def main():
    parser = argparse.ArgumentParser(
        description='GitHub Skill Publisher - 自动发布WorkBuddy技能到GitHub',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 交互式模式（推荐）
  python publisher.py --guide

  # 完整发布（包含GitHub用户名）
  python publisher.py --name "my-skill" --desc "我的技能" --github-username "yourname"

  # 自定义版本和作者
  python publisher.py --name "my-skill" --desc "我的技能" --version "2.0.0" --author "MyName" --github-username "yourname"

  # 仅生成文档
  python publisher.py --docs-only
        """
    )

    parser.add_argument('--name', help='技能名称')
    parser.add_argument('--desc', help='技能描述')
    parser.add_argument('--version', default='1.0.0', help='版本号（默认v1.0.0）')
    parser.add_argument('--author', default='YourName', help='作者名称')
    parser.add_argument('--github-username', dest='github_username', default='',
                       help='GitHub用户名（用于生成仓库链接）')
    parser.add_argument('--license', dest='license_type', default='MIT',
                       choices=['MIT', 'Apache-2.0', 'GPL-3.0', 'BSD-3-Clause'],
                       help='开源协议（默认MIT）')
    parser.add_argument('--style', default='modern', choices=['modern', 'classic'],
                       help='README风格（默认modern）')
    parser.add_argument('--guide', action='store_true', help='启用交互式引导')
    parser.add_argument('--docs-only', action='store_true', help='仅生成文档')

    args = parser.parse_args()

    if args.guide:
        interactive_mode()
    elif args.name and args.desc:
        publisher = GitHubSkillPublisher(
            name=args.name,
            desc=args.desc,
            version=args.version,
            author=args.author,
            github_username=args.github_username,
            license_type=args.license_type,
            style=args.style
        )
        publisher.generate_all()
    else:
        print(f"""
{Colors.HEADER}GitHub Skill Publisher{Colors.ENDC}
{Colors.OKCYAN}自动发布WorkBuddy技能到GitHub{Colors.ENDC}

{Colors.WARNING}使用方法:{Colors.ENDC}

1. {Colors.BOLD}交互式模式（推荐）{Colors.ENDC}
   python publisher.py --guide

2. {Colors.BOLD}命令行模式{Colors.ENDC}
   python publisher.py --name "技能名" --desc "技能描述"

3. {Colors.BOLD}查看帮助{Colors.ENDC}
   python publisher.py --help

{Colors.OKCYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.ENDC}
""")
        parser.print_help()

if __name__ == "__main__":
    main()
Add main publisher script
