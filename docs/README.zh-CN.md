# Fixen UI Studio

[English — 主要文档](../README.md) · [Bahasa Indonesia](README.id.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · 简体中文

**理解产品需求，构建可用界面，以证据验证结果。**

Fixen UI Studio 是面向 AI 智能体的开源技能，用于设计、实现、审查和改进 Web 界面。它将产品调研、艺术指导、用户体验、前端实现、视觉检查，以及按需进行的真实图片检索整合为可调整的工作流程。

**v1.3.0 · 实验阶段。** 项目原名为 Fixenzo UI Studio，通过 `$fixen-ui-studio` 调用。本技能是 Markdown/YAML 指令包；模型、工具和权限由智能体运行环境提供。

## 安装

从 [GitHub Releases](https://github.com/riantosee/Fixen-ui-Studio/releases) 下载 `fixen-ui-studio-v1.3.0.zip`，将 `fixen-ui-studio/` 文件夹解压到 Codex 技能目录，确保入口文件位于：

```text
~/.codex/skills/fixen-ui-studio/SKILL.md
```

在 Windows 中，`~` 通常代表用户个人目录。如果配置了 `CODEX_HOME`，请使用该配置下的技能目录。替换已有安装前，请备份自定义修改。也可克隆仓库，仅复制 `skills/fixen-ui-studio/` 文件夹。其他运行环境尚未全部测试。

## 使用示例

```text
使用 $fixen-ui-studio 构建配送调度仪表板。
优先展示延迟配送、筛选功能和明确的处理操作。
沿用项目现有技术栈，并使用合成数据。
```

```text
使用 $fixen-ui-studio 审查此页面的信息层级和无障碍设计。
提供证据和可执行的建议，不要修改文件。
```

```text
使用 $fixen-ui-studio 构建以英语为主要语言的预订界面，
同时提供简体中文和阿拉伯语版本。复用现有 i18n 系统，
检查价格、日期、移动端布局和从右向左的导航。
```

## 多语言与图片

英语是项目文档的主要语言。智能体应使用用户要求的语言进行沟通；界面语言则遵循产品要求及仓库现有约定。对于未指定语言的新产品，默认使用英语，并说明这一假设。[本地化指南](../skills/fixen-ui-studio/systems/localization.md) 涵盖区域格式、文本长度变化、字体覆盖和从右向左的布局。本技能不安装翻译引擎，也不保证所有语言的翻译质量。

[图片检索](../skills/fixen-ui-studio/design/asset-sourcing.md) 是可选流程，依赖运行环境提供的工具。候选筛选、下载、集成和渲染验证是不同阶段。仅要求候选清单时，流程止于推荐。请在[素材记录](../skills/fixen-ui-studio/templates/asset-register.md)中记录来源、作者、使用条款和验证状态。第三方图片保留各自的许可证，不会自动适用项目的 MIT 许可证。

## 贡献与验证

请阅读英文版 [CONTRIBUTING.md](../CONTRIBUTING.md)。欢迎提交翻译；请保留技能标识符、命令、路径、许可证含义以及验证范围说明。如有文档差异，请参考[英文 README](../README.md)和[更新日志](../CHANGELOG.md)，并报告问题。

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s scripts -p "test_*.py" -v
```

上述贡献者检查需要 Python 3.10+；仅使用技能指令无需 Python。结构验证通过并不证明视觉质量、翻译质量、无障碍合规性或基准测试优势。具体范围见[验证说明](validation.md)。README 的翻译也不能作为每个语言版本均已通过浏览器测试的证据。

## 安全与许可证

项目贡献和社区空间禁止未经授权的利用、凭据窃取、恶意提示注入、恶意软件及破坏性操作。允许在隔离环境中使用合成数据开展经授权的防御性评估。请按照[安全政策](../SECURITY.md)私下报告漏洞，并遵守[行为准则](../CODE_OF_CONDUCT.md)。本技能不是沙箱，也不保证能够抵御提示注入。

[MIT 许可证](../LICENSE)允许商业使用、修改、再分发和销售，但必须保留版权及许可证声明。安全和社区政策不会改变 MIT 授予的权限，也不授权攻击其他系统。分支项目应说明来源和修改内容，不得冒充官方发行版。
