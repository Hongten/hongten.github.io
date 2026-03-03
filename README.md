# Hongten GitHub Pages Blog

已基于你确认的样式生成静态博客。

## 目录

- `index.html` 首页
- `about.html` 关于
- `posts/` 文章页
- `assets/style.css` 样式

## 发布到 GitHub Pages

1. 在 GitHub 新建仓库：`Hongten.github.io`
2. 把本目录文件推送到仓库根目录
3. 打开仓库 Settings -> Pages
4. Source 选择 `Deploy from a branch`
5. Branch 选 `main` / root
6. 几十秒后访问：
   - `https://hongten.github.io`

## 本地预览

在此目录执行：

```bash
python3 -m http.server 8080
```

然后打开 `http://127.0.0.1:8080`
