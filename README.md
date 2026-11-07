# Frontend Design Skills

一套用于 Codex 的界面设计与实现技能，覆盖网页、桌面和移动端的相关界面任务。根据页面用途选择指导，优先真实业务内容、清晰交互和可维护代码。

## 包含的技能

| 技能 | 作用 | 主要场景 |
|---|---|---|
| `ui-ux-pro-max` | 本地设计资料检索、信息层级、交互状态、响应式与可访问性指导 | 功能页、后台、表格、表单、网页与原生界面 |
| `design-taste-frontend` | 构图、排版、视觉节奏、品牌表达及文案删减 | 官网、落地页、作品集、编辑式网页 |

两者共享设计决策和验证。Taste 不将营销页布局套用到后台或复杂操作流程。技能会适配项目现有语言、技术栈、组件与平台习惯。

## 设计偏好

- 标题直接说明页面、对象或任务，减少空泛标语和“让数据，清晰可见”式装饰性标题。
- 文案直接呈现已有事实、功能和下一步，精简无关对照及说明小字；保留必要否定、标签、单位、条件、错误恢复和重要后果。
- 让可点击项在未悬停时也容易识别，用柔和底色、分组、整行交互或其他合适线索，避免满屏独立矩形和无意义的框内套框。
- 优先图形化图标；准确区分按压、选中、展开、禁用与焦点。控件点击、展开和操作后保持静态边界稳定，通过背景、标签或底部指示表达状态和键盘焦点，保留系统高对比度行为。
- 采用组件化结构，复用已有组件，合理拆分页面和逻辑。
- 卡片随实际内容合理布局，避免文字/角标遮挡；详情展开和状态更新保持周围布局稳定，密集图形按需提供完整视图。
- 选中状态不随焦点丢失；点击区域与视觉归属一致；常规提示自动消退，重要错误和决策保持可处理。
- 按需读取参考、检索和验证，不要求叠加其他来源的完整工作流、检测器或多代理流程。

## 安装

需要 Git 和 Python 3。克隆后运行标准库安装脚本：

```sh
git clone https://github.com/csyxcsyx/frontend-design-skills.git
cd frontend-design-skills
python scripts/install.py
```

默认同时安装两个技能到 `$CODEX_HOME/skills`；未设置 `CODEX_HOME` 时使用 `~/.codex/skills`。Windows 上也可使用 `py -3`，部分系统使用 `python3`。

```sh
python scripts/install.py --dry-run
python scripts/install.py --dest /absolute/path/to/skills
```

脚本遇到任何同名技能目录会停止，不覆盖已有内容。需要更新时，请先备份现有自定义版本，再自行将旧目录移开后重新安装。请把两个目录作为同级目录安装，以保留可选协同引用。安装后在新的消息中调用；若客户端尚未刷新技能目录，可重新打开聊天或重启客户端。

也可以让 Codex 的 skill-installer 从本仓库的 `skills/ui-ux-pro-max` 与 `skills/design-taste-frontend` 两个路径安装。

## 直接复制的提示词

```text
请使用 $ui-ux-pro-max，并按界面类型适当结合 $design-taste-frontend，完成当前界面任务。沿用项目技术栈与设计规范，以真实业务和用户操作为中心。文案简洁直接，优先呈现事实、功能和下一步，仅在澄清限制、错误或风险时使用必要的否定表达。布局紧凑清晰、内容完整，控件点击及操作后保持协调，使用背景或局部指示表达状态，保留清晰键盘焦点。采用图形化图标和合理组件化，其余遵循技能规范；按需读取、检索和验证，直接实施并简要报告结果与限制。
```

在项目已有任务上下文中粘贴即可。如果仅需要评审，请同时说明“只评审，暂不修改代码”。

## 本地验证

```sh
python scripts/verify.py
```

该命令检查打包目录、文档引用、资料完整性、检索结果和核心回归测试。上游还带有依赖其完整仓库布局的开发测试，因此这里运行适用于独立技能包的核心回归范围；不是对所有上游仓库工具链的认证。

技能本身不保证视觉效果，也不能替代真实用户研究和界面验收。具体项目应使用实际渲染、交互检查与适当项目测试。

## 来源与许可

本仓库是独立适配整合，非原项目官方发行版。主要来源为 [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) 和 [Taste](https://github.com/Leonxlnx/taste-skill)，并选择性参考 Anthropic frontend-design、Impeccable、Vercel Web Interface Guidelines 与 UI Skills。

详细版本、采用范围和排除的流程见 [来源说明](skills/ui-ux-pro-max/references/source-notices.md) 与两个技能中的 `upstream-source.json`。来源研究时记录的星数仅为历史仓库页面显示值。

原创打包工具和文档使用 MIT 许可；上游内容继续适用各自许可，详见 [LICENSE](LICENSE)、[NOTICE.md](NOTICE.md)、技能目录内的许可证及 [保留的许可副本](skills/ui-ux-pro-max/references/source-licenses)。
