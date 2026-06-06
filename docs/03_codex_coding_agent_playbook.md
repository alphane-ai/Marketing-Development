# 03. Codex/Coding Agent 客户开发方案

## 定位

```text
Coding Agent Workflow Infrastructure:
把 Codex-style coding agent 接入 GitHub、GitLab、Linear、Slack 和 CI/CD，
让 issue、PR review、CI failure 变成可审计的 PR draft 和修复建议。
```

## 合规边界

这条线只面向 OpenAI/Codex 支持地区客户做合规应用集成和工作流自动化。

不做：

- API key 转卖。
- 账号转卖。
- 裸 token 转售。
- 国内绕限制访问。
- 无授权代码分析。

## 核心 offer

```text
Free AI Coding Workflow Audit.

Give us 3 historical issues / PRs / CI failures.
We estimate which tasks can be handled by a coding agent and how many engineer-hours can be saved monthly.
```

## 5 个产品包

### 1. Codex PR Agent

流程：

```text
GitHub issue
  -> 读 repo
  -> 定位相关文件
  -> 生成代码修改
  -> 补测试
  -> 跑测试
  -> 生成 PR draft
  -> 写 PR summary 和风险点
```

卖点：

```text
把小需求、小 bug、小重构从工程师手里拿走。
```

### 2. Codex Code Review Agent

流程：

```text
新 PR
  -> 检查 bug
  -> 检查边界条件
  -> 检查安全风险
  -> 检查测试缺失
  -> 输出 review comments
```

卖点：

```text
让 senior engineer 少花时间看低级问题。
```

### 3. Legacy Code Maintainer

流程：

```text
老代码库
  -> 模块说明
  -> 技术债识别
  -> 小 bug 修复
  -> 文档补全
  -> 测试补全
  -> 迁移建议
```

卖点：

```text
让没人愿意碰的老代码继续可维护。
```

### 4. CI Repair Agent

流程：

```text
CI failed
  -> 读 logs
  -> 判断失败原因
  -> 修测试/依赖/构建配置
  -> 生成 patch
```

卖点：

```text
减少工程师处理 CI 红灯的时间。
```

### 5. Coding Agent Gateway

功能：

```text
任务队列
模型路由
成本控制
repo 权限管理
agent 执行日志
任务审计
预算上限
多租户 key 管理
```

卖点：

```text
不是 demo，而是可以安全接进研发流程的 coding agent infrastructure。
```

## ICP 优先级

### 一级：海外 SaaS/AI 创业团队

触发信号：

- 团队 5-50 人。
- 刚融资。
- 正在招工程师。
- GitHub 活跃。
- roadmap 很大但团队小。

主卖：

- PR Agent。
- Code Review Agent。
- Workflow Audit。

### 二级：Dev agency / 软件外包团队

痛点：

- 客户小需求多。
- 工程师时间直接影响毛利。
- 维护项目多。
- 测试和文档没人做。

主卖：

- 多项目 coding agent。
- 白标报告。
- 每项目 agent。

### 三级：企业内部工具/老代码团队

痛点：

- 老系统没人维护。
- 小需求排期长。
- 技术债多。
- 业务部门催。

主卖：

- Legacy maintainer。
- CI repair。
- 文档和测试补全。

### 四级：开源项目/devtool 公司

作用：

- 做案例。
- 做技术信誉。
- 做传播。

## 第一版 MVP

不要一开始做“自动开发整个软件”。先聚焦：

```text
1. Issue -> PR draft
2. PR review
3. CI failure repair
```

原因：

- 输入明确。
- 输出可验证。
- 风险低。
- 客户容易理解。
- ROI 容易算。
- 适合截图传播。

## ROI 公式

```text
节省成本 = 每月自动处理任务数 * 单任务节省工程师小时 * 工程师小时成本
```

示例：

```text
每月处理 80 个小 issue
每个 issue 节省 1.5 小时
工程师成本 $80/小时

80 * 1.5 * 80 = $9,600/月
```

如果收费 $1,000-$3,000/月，客户容易接受。

## 试点包

周期：

```text
2 周
```

价格：

```text
$500 - $3,000
```

交付：

```text
接入 GitHub/Linear/Slack 中的一个
选择 10 个真实任务
agent 生成 PR draft/review/CI fix
人类 review
统计节省时间
输出试点报告
```

成功标准：

```text
至少 5 个任务生成可 review 结果
至少 2 个结果被客户采纳
每个任务节省 30 分钟以上
客户愿意继续月付
```

## 定价建议

### Starter

```text
$299 - $999/月
PR review
固定任务额度
基础 dashboard
```

### Team

```text
$1,000 - $3,000/月
Issue -> PR draft
PR review
CI analysis
GitHub/Slack 接入
每周报告
```

### Agency

```text
$2,000 - $10,000/月
多项目管理
白标报告
客户分组
优先支持
```

### Enterprise

```text
custom
私有环境
安全审计
权限控制
SLA
高级日志
```

## 安全信任设计

必须明确：

```text
客户授权 repo 后才能访问
默认只生成 PR draft，不自动 merge
高风险修改必须人工审批
所有 agent 操作可追踪
不读取无关 repo
支持只读模式
支持删除任务记录
支持私有/本地环境方案
```
