# Hongten GitHub Pages Blog

已基于你确认的样式生成静态博客。

## 目录

- `index.html` 首页
- `about.html` 关于
- `posts/` 文章页
- `assets/style.css` 样式

## 发布到 GitHub Pages

1. 使用仓库：`Hongten/hongten.github.io`
2. 把本目录文件推送到仓库根目录
3. 打开仓库 `Settings -> Pages`
4. Source 选择 `Deploy from a branch`
5. Branch 选 `master` / root
6. 几十秒后访问：
   - `https://hongten.github.io`

## 已加入功能

- 文章卡片按日期自动倒序
- SEO / Open Graph / Twitter Card 元信息
- Giscus 评论区预留（每篇文章页）

## 启用 Giscus（一次性）

当前仓库还没启用 Discussions，所以 `data-category-id` 为空。

1. 到仓库 `Settings -> General` 打开 `Discussions`
2. 创建一个分类（建议 `General`）
3. 在 Giscus 配置页获取 category id：
   - https://giscus.app/zh-CN
4. 把两个文章页里 `data-category-id=""` 填成实际 ID：
   - `posts/openclaw-notify.html`
   - `posts/github-pages-quickstart.html`

## 本地预览

在此目录执行：

```bash
python3 -m http.server 8080
```

然后打开 `http://127.0.0.1:8080`
