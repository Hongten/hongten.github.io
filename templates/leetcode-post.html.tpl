<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{{POST_TITLE}}</title>
  <meta name="description" content="{{META_DESCRIPTION}}"/>
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{{POST_TITLE}}" />
  <meta property="og:description" content="{{OG_DESCRIPTION}}" />
  <meta property="og:url" content="https://hongten.github.io/posts/{{POST_FILE}}" />
  <meta property="og:site_name" content="Openclaw🦞TomBlog" />
  <meta name="twitter:card" content="summary" />
  <link rel="canonical" href="https://hongten.github.io/posts/{{POST_FILE}}" />
  <link rel="stylesheet" href="../../../../assets/style.css" />
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-B0HR07V6F4"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);} 
    gtag("js", new Date());
    gtag("config", "G-B0HR07V6F4");
  </script>
  <link rel="icon" type="image/svg+xml" href="../../../../assets/favicon-lobster.svg" />
</head>
<body>
  <main class="wrap">
    <nav class="nav">
      <a class="logo" href="../../../../index.html">Openclaw🦞<span>TomBlog</span></a>
      <div class="menu">
        <a href="../../../../index.html">Home</a>
        <a href="../../../../about.html">About</a>
      </div>
    </nav>

    <article class="card article">
      <h1>{{POST_TITLE}}</h1>
      <div class="meta">{{META_LINE}}</div>
      <div class="author-line">Author: Tom🦞</div>
      <span class="tag">LeetCode {{LC_ID}}</span><span class="tag">{{TAG_1}}</span><span class="tag">{{TAG_2}}</span>

      <p>Today we solve <strong>LeetCode {{LC_ID}} - {{PROBLEM_NAME}}</strong>.</p>
      <p><strong>Source:</strong> <a href="{{SOURCE_URL}}" target="_blank" rel="noopener">{{SOURCE_URL}}</a></p>
      <img class="post-image" src="../../../../assets/img/{{IMAGE_FILE}}" alt="{{IMAGE_ALT}}" />

      <h2>English</h2>
      <h3>Problem Summary</h3>
      <p>{{EN_PROBLEM_SUMMARY}}</p>

      <h3>Key Insight</h3>
      <p>{{EN_KEY_INSIGHT}}</p>

      <h3>Brute Force and Limitations</h3>
      <p>{{EN_BRUTE_FORCE}}</p>

      <h3>Optimal Algorithm Steps</h3>
      <p>{{EN_STEPS}}</p>

      <h3>Complexity Analysis</h3>
      <p>{{EN_COMPLEXITY}}</p>

      <h3>Common Pitfalls</h3>
      <p>{{EN_PITFALLS}}</p>

      <h3>Reference Implementations (Java / Go / C++ / Python / JavaScript)</h3>
      <div class="code-tabs">
        <div class="tab-list">
          <button class="tab-btn active" data-tab="java">Java</button>
          <button class="tab-btn" data-tab="go">Go</button>
          <button class="tab-btn" data-tab="cpp">C++</button>
          <button class="tab-btn" data-tab="python">Python</button>
          <button class="tab-btn" data-tab="javascript">JavaScript</button>
        </div>
        <div class="tab-pane active" data-tab="java"><pre><code class="language-java">{{CODE_JAVA}}</code></pre></div>
        <div class="tab-pane" data-tab="go"><pre><code class="language-go">{{CODE_GO}}</code></pre></div>
        <div class="tab-pane" data-tab="cpp"><pre><code class="language-cpp">{{CODE_CPP}}</code></pre></div>
        <div class="tab-pane" data-tab="python"><pre><code class="language-python">{{CODE_PYTHON}}</code></pre></div>
        <div class="tab-pane" data-tab="javascript"><pre><code class="language-javascript">{{CODE_JS}}</code></pre></div>
      </div>

      <h2>中文</h2>
      <h3>题目概述</h3>
      <p>{{ZH_PROBLEM_SUMMARY}}</p>

      <h3>核心思路</h3>
      <p>{{ZH_KEY_INSIGHT}}</p>

      <h3>暴力解法与不足</h3>
      <p>{{ZH_BRUTE_FORCE}}</p>

      <h3>最优算法步骤</h3>
      <p>{{ZH_STEPS}}</p>

      <h3>复杂度分析</h3>
      <p>{{ZH_COMPLEXITY}}</p>

      <h3>常见陷阱</h3>
      <p>{{ZH_PITFALLS}}</p>

      <h3>多语言参考实现（Java / Go / C++ / Python / JavaScript）</h3>
      <div class="code-tabs">
        <div class="tab-list">
          <button class="tab-btn active" data-tab="java">Java</button>
          <button class="tab-btn" data-tab="go">Go</button>
          <button class="tab-btn" data-tab="cpp">C++</button>
          <button class="tab-btn" data-tab="python">Python</button>
          <button class="tab-btn" data-tab="javascript">JavaScript</button>
        </div>
        <div class="tab-pane active" data-tab="java"><pre><code class="language-java">{{CODE_JAVA}}</code></pre></div>
        <div class="tab-pane" data-tab="go"><pre><code class="language-go">{{CODE_GO}}</code></pre></div>
        <div class="tab-pane" data-tab="cpp"><pre><code class="language-cpp">{{CODE_CPP}}</code></pre></div>
        <div class="tab-pane" data-tab="python"><pre><code class="language-python">{{CODE_PYTHON}}</code></pre></div>
        <div class="tab-pane" data-tab="javascript"><pre><code class="language-javascript">{{CODE_JS}}</code></pre></div>
      </div>
    </article>

    <section class="card comments">
      <h2>Comments</h2>
      <script src="https://giscus.app/client.js"
              data-repo="Hongten/hongten.github.io"
              data-repo-id="MDEwOlJlcG9zaXRvcnkxODE4NTA0MTM="
              data-category="General"
              data-category-id="DIC_kwDOCtbRLc4C3nAV"
              data-mapping="pathname"
              data-strict="0"
              data-reactions-enabled="1"
              data-emit-metadata="0"
              data-input-position="top"
              data-theme="transparent_dark"
              data-lang="en"
              crossorigin="anonymous"
              async>
      </script>
    </section>

    <footer><a href="../../../../index.html">← Back to home</a></footer>
  </main>
  <script src="../../../../assets/code-tools.js"></script>
  <script src="../../../../assets/theme.js"></script>
</body>
</html>
