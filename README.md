# Hongten GitHub Pages Blog

A static blog built with the confirmed visual style.

## Structure

- `index.html` — Home page
- `about.html` — About page
- `posts/` — Post pages
- `assets/style.css` — Main style sheet

## Deploy to GitHub Pages

1. Use repository: `Hongten/hongten.github.io`
2. Push this directory to the repository root
3. Open repository `Settings -> Pages`
4. Choose `Deploy from a branch`
5. Select `master` / root
6. Visit:
   - `https://hongten.github.io`

## Included Features

- Post cards auto-sorted by date (descending)
- SEO metadata (Open Graph + Twitter Card)
- Giscus comment section on post pages

## Enable Giscus (one-time)

1. Go to repository `Settings -> General` and enable `Discussions`
2. Create a category (recommended: `General`)
3. Get the category ID from:
   - https://giscus.app
4. Fill `data-category-id` in post pages if needed

## Local Preview

Run in this directory:

```bash
python3 -m http.server 8080
```

Then open `http://127.0.0.1:8080`.
