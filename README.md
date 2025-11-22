# GitHub CI/CD 构建与发布测试仓库

这是一个用于测试GitHub Actions自动构建和发布流程的示例仓库。

## 功能特性

- 推送代码时自动触发自定义构建流程，生成release内容。
- 将release内容推送到github release上
- 维护独立的release分支，并清除覆盖历史记录

## 配置说明

- 需要配置GitHub Token权限

## 配置要求

### GitHub仓库设置
1. 确保仓库有足够的权限：
   - `contents: write` (用于创建release和更新分支)
   - `actions: write` (用于运行工作流)

2. 默认使用`secrets.GITHUB_TOKEN`，无需额外配置