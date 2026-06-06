# Marketing Development

LLM API / Kimi / Codex / Coding Agent 客户开发作战手册。

这是一套面向 **Kimi API / 国产合规模型服务** 与 **Codex / Coding Agent 海外合规服务** 的客户开发、产品包装、获客执行路线图。

核心目标不是“卖 token”，而是把 token 能力包装成客户愿意持续付费的业务结果：

- 对国内客户：卖 **Kimi API Gateway / 模型网关 / 成本优化 / AI 功能上线服务**。
- 对海外支持地区客户：卖 **Codex Coding Agent Workflow / PR Agent / Code Review Agent / CI Repair Agent**。
- 对系统集成商和外包团队：卖 **白标模型基础设施 + 项目交付加速能力**。

## 核心原则

1. 不卖裸 token，卖可量化结果。
2. 不做灰色绕限制访问，先划清合规边界。
3. 不找所有客户，先找高痛感、高 LTV、7 天内能验证价值的客户。
4. 不只讲模型名字，讲成本下降、研发效率、上线速度、稳定性和权限审计。
5. 用交易式获客思路管理增长：把渠道当成 portfolio，每周加仓赢家、砍掉衰减渠道。
6. 每次交付都沉淀 proof artifact：成本报告、节省小时、before/after、匿名案例。

## 目录结构

```text
llm-api-customer-acquisition-playbook/
  README.md
  docs/
    00_compliance_and_positioning.md
    01_strategy_overview.md
    02_kimi_api_gateway_playbook.md
    03_codex_coding_agent_playbook.md
    04_90_day_roadmap.md
    05_growth_operating_system.md
    06_lead_finder_mvp_operating_playbook.md
  templates/
    customer_signal_table.csv
    weekly_growth_review.csv
    outreach_templates.md
    audit_report_template.md
    lead_finder_daily_sop.md
  scripts/
    lead_score.py
```

## 推荐执行顺序

1. 先读 [合规边界与定位](docs/00_compliance_and_positioning.md)。
2. 再读 [总策略](docs/01_strategy_overview.md)。
3. 国内客户路线看 [Kimi/API Gateway 方案](docs/02_kimi_api_gateway_playbook.md)。
4. Codex/coding agent 路线看 [Codex 方案](docs/03_codex_coding_agent_playbook.md)。
5. 按 [90 天路线图](docs/04_90_day_roadmap.md) 执行。
6. 每周用 [增长操作系统](docs/05_growth_operating_system.md) 和 [weekly_growth_review.csv](templates/weekly_growth_review.csv) 复盘。
7. 如果使用 Lead Finder MVP，每天按 [Lead Finder 作战手册](docs/06_lead_finder_mvp_operating_playbook.md) 和 [每日 SOP](templates/lead_finder_daily_sop.md) 跑线索。

## 最小可执行目标

前 30 天不要追求复杂平台，先完成下面四件事：

1. 一个 landing page。
2. 一个成本体检 / workflow audit offer。
3. 200 个高意向客户名单。
4. 5 个免费或低价诊断，2 个付费试点。

## 最适合先打的两个 offer

### 国内 Kimi 线

```text
免费做一次 LLM API 成本与稳定性体检。
我们看 7 天调用日志或典型 prompt，输出 token 浪费点、可缓存上下文、Kimi/多模型路由建议和预计节省金额。
```

### 海外 Codex 线

```text
Free AI Coding Workflow Audit.
Give us 3 historical issues / PRs / CI failures. We estimate which tasks can be handled by a coding agent and how many engineer-hours can be saved monthly.
```

## 结果导向

所有获客内容和销售话术都应该围绕这些结果：

- 节省 token 成本。
- 降低接口失败率。
- 缩短 AI 功能上线时间。
- 减少工程师处理小 bug、PR review、CI failure 的时间。
- 让系统集成商/外包团队提高交付毛利。
- 让 SaaS/AI 应用团队不用自己维护复杂模型网关。

## 重要提醒

OpenAI/Codex 相关业务必须遵守支持地区、账号/API key 使用和服务条款边界。国内客户主线应放在 Kimi 或其他可合规提供的模型与应用交付上；海外 OpenAI/Codex 线应定位为合规应用集成和工作流自动化，不做账号、key、token 转售。
