# 01. 总策略：从卖 token 到卖业务结果

## 核心启发

这套增长思路可以概括成：

```text
把 AI 放进真实工作流
让它能访问工具
让它执行可验证任务
让结果能被截图和传播
让客户能算清楚 ROI
```

套到我们这里，不是问：

```text
谁要买 Kimi/Codex token？
```

而是问：

```text
谁正在为模型成本、AI 功能上线、工程师时间、交付效率和系统稳定性付出高成本？
```

## 两个主业务飞轮

### Kimi/API Gateway 飞轮

```text
找到 AI 应用/SaaS/集成商
  -> 免费成本体检
  -> 找出 token 浪费和模型路由机会
  -> 接入 Kimi/API Gateway
  -> 提供成本、日志、权限、fallback dashboard
  -> 输出节省报告
  -> 形成匿名案例
  -> 用案例获取更多高意向客户
```

### Codex/Coding Agent 飞轮

```text
找到研发任务重的软件团队
  -> 免费 coding workflow audit
  -> 选择历史 issue/PR/CI failure
  -> agent 生成 PR draft/review/fix
  -> 统计节省工程师小时
  -> 形成案例和截图
  -> 获取更多 SaaS/dev agency 客户
```

## 客户选择原则

优先找：

- 问题很贵。
- 现在已经在为问题付钱。
- 7 天内能看到结果。
- 有团队预算。
- 成功案例可传播。
- 使用频率高，有复购。

不要优先找：

- 个人低价用户。
- 只问 token 单价的人。
- 没有明确业务场景的人。
- 灰色用途客户。
- 只有好奇心没有预算的人。

## 获客渠道不是列表，是 portfolio

每个渠道都要像交易策略一样看：

- 投入成本。
- 回复率。
- 有效对话率。
- 试点率。
- 成交率。
- 客户质量。
- 容量上限。
- 边际 ROI。
- 品牌/合规风险。

每周只问：

```text
下一单位时间/钱投到哪个渠道，回报最高？
```

## 主要渠道组合

### 高意向私信/邮件

根据具体触发信号联系客户，不做泛泛群发。

触发信号：

- 招聘 LLM/AI 工程师。
- 新上线 AI 功能。
- 抱怨 token 成本或模型不稳定。
- GitHub issue/PR 堆积。
- Dev agency 项目交付压力大。
- 刚融资，需要提高 shipping velocity。

### 技术内容

写实用教程，不写空泛营销。

主题：

- Kimi API 接入坑。
- token 成本优化。
- 模型路由。
- coding agent 如何从 issue 生成 PR。
- PR review agent 边界。
- dev agency 如何用 coding agent 提高毛利。

### 开源工具

用小工具建立信任：

- `llm-cost-inspector`
- `kimi-openai-router`
- `codex-pr-auditor`
- `ci-failure-analyzer`

### 系统集成商/外包伙伴

他们有客户和项目，你们提供底层模型网关、白标 dashboard、分账和技术支持。

### 案例传播

每个客户诊断或试点都要沉淀：

- before/after。
- 节省成本。
- 节省工程师小时。
- 被采纳的 PR 数。
- token 成本下降比例。
- 接口稳定性变化。

## 最小 30 天目标

```text
高意向客户名单：200 个
有效对话：20 个
诊断/audit：5 个
付费试点：2 个
匿名案例：1-2 个
明确主 ICP：1 个
明确主渠道：1 个
```
