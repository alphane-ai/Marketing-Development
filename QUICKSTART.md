# Quickstart

## 第一天做什么

1. 读 `docs/00_compliance_and_positioning.md`，确认业务红线。
2. 选一条主线：
   - 国内：Kimi/API Gateway。
   - 海外：Codex/Coding Agent。
3. 复制 `templates/customer_signal_table.csv`，开始填 50 个客户。
4. 从 `templates/outreach_templates.md` 里选一条话术，改成高度个性化版本。
5. 今天只做一个目标：发出 20 条高意向联系。

## 第一周目标

```text
高意向客户名单：100 个
发出联系：60 条
有效回复：5 条
诊断/audit：1-2 个
技术内容：1 篇
```

## 第二周目标

```text
高意向客户名单：200 个
有效对话：10 个
诊断/audit：3 个
付费试点：1 个
```

## 每天固定动作

```text
找 20 个客户
发 20 条个性化消息
跟进昨天回复
做一个诊断/audit 或准备诊断材料
记录数据
```

## 每周固定复盘

打开 `templates/weekly_growth_review.csv`，填：

```text
渠道
投入时间
联系数
回复数
有效对话
诊断数
试点数
成交数
客户质量
下周动作
```

## 客户评分

可以用脚本快速算分：

```bash
python scripts/lead_score.py --pain 5 --payment 4 --compliance 5 --validation 4 --case 4
```

结果：

```text
18 分以上：优先联系
15-17 分：二线跟进
15 分以下：暂缓
```
