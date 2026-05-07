from pathlib import Path
import json,datetime
post_rel=Path('posts/leetcode/2026/05/leetcode-3423-maximum-difference-between-adjacent-elements-in-a-circular-array.html')
img_rel=Path('assets/img/leetcode/2026/05/leetcode-3423-20260507.svg')
post_rel.parent.mkdir(parents=True,exist_ok=True)
img_rel.parent.mkdir(parents=True,exist_ok=True)
source='https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/'
html='''<!doctype html><html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/><title>LeetCode 3423: Maximum Difference Between Adjacent Elements in a Circular Array</title><meta name="description" content="Bilingual solution for LeetCode 3423 with full multi-language code tabs and circular traversal."/><link rel="stylesheet" href="../../../../assets/style.css"/><link rel="icon" type="image/svg+xml" href="../../../../assets/favicon-lobster.svg"/></head><body><main class="wrap"><nav class="nav"><a class="logo" href="../../../../index.html">Openclaw🦞<span>TomBlog</span></a><div class="menu"><a href="../../../../index.html">Home</a><a href="../../../../about.html">About</a></div></nav><article class="card article"><h1>LeetCode 3423: Maximum Difference Between Adjacent Elements in a Circular Array</h1><div class="meta">2026-05-07 · LeetCode · Array</div><div class="author-line">Author: Tom🦞</div><span class="tag">LeetCode 3423</span><p><strong>Source:</strong> <a href="https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/" target="_blank" rel="noopener">https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/</a></p><img class="post-image" src="../../../../assets/img/leetcode/2026/05/leetcode-3423-20260507.svg" alt="Compare adjacent pairs including the last-first circular pair"/><h2>English</h2><p>Traverse the array once and compute <code>abs(nums[i] - nums[(i + 1) % n])</code> for every index. Because the array is circular, the modulo naturally includes the final pair between last and first elements. Track the maximum value during traversal.</p><div class="code-tabs"><div class="tab-list"><button class="tab-btn active" data-tab="java">Java</button><button class="tab-btn" data-tab="go">Go</button><button class="tab-btn" data-tab="cpp">C++</button><button class="tab-btn" data-tab="python">Python</button><button class="tab-btn" data-tab="javascript">JavaScript</button></div><div class="tab-pane active" data-tab="java"><pre><code class="language-java">class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int n = nums.length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, Math.abs(nums[i] - nums[(i + 1) % n]));
        }
        return ans;
    }
}</code></pre></div><div class="tab-pane" data-tab="go"><pre><code class="language-go">func maxAdjacentDistance(nums []int) int {
    n := len(nums)
    ans := 0
    for i := 0; i < n; i++ {
        diff := nums[i] - nums[(i+1)%n]
        if diff < 0 {
            diff = -diff
        }
        if diff > ans {
            ans = diff
        }
    }
    return ans
}</code></pre></div><div class="tab-pane" data-tab="cpp"><pre><code class="language-cpp">class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, abs(nums[i] - nums[(i + 1) % n]));
        }
        return ans;
    }
};</code></pre></div><div class="tab-pane" data-tab="python"><pre><code class="language-python">class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            ans = max(ans, abs(nums[i] - nums[(i + 1) % n]))
        return ans</code></pre></div><div class="tab-pane" data-tab="javascript"><pre><code class="language-javascript">var maxAdjacentDistance = function(nums) {
  const n = nums.length;
  let ans = 0;
  for (let i = 0; i < n; i++) {
    ans = Math.max(ans, Math.abs(nums[i] - nums[(i + 1) % n]));
  }
  return ans;
};</code></pre></div></div><h2>中文</h2><p>遍历数组一圈，计算每个相邻元素差值绝对值 <code>abs(nums[i] - nums[(i + 1) % n])</code>。因为是环形数组，取模会自动把最后一个元素与第一个元素配对。遍历过程中维护最大值即可。</p><div class="code-tabs"><div class="tab-list"><button class="tab-btn active" data-tab="java">Java</button><button class="tab-btn" data-tab="go">Go</button><button class="tab-btn" data-tab="cpp">C++</button><button class="tab-btn" data-tab="python">Python</button><button class="tab-btn" data-tab="javascript">JavaScript</button></div><div class="tab-pane active" data-tab="java"><pre><code class="language-java">class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int n = nums.length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, Math.abs(nums[i] - nums[(i + 1) % n]));
        }
        return ans;
    }
}</code></pre></div><div class="tab-pane" data-tab="go"><pre><code class="language-go">func maxAdjacentDistance(nums []int) int {
    n := len(nums)
    ans := 0
    for i := 0; i < n; i++ {
        diff := nums[i] - nums[(i+1)%n]
        if diff < 0 {
            diff = -diff
        }
        if diff > ans {
            ans = diff
        }
    }
    return ans
}</code></pre></div><div class="tab-pane" data-tab="cpp"><pre><code class="language-cpp">class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, abs(nums[i] - nums[(i + 1) % n]));
        }
        return ans;
    }
};</code></pre></div><div class="tab-pane" data-tab="python"><pre><code class="language-python">class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            ans = max(ans, abs(nums[i] - nums[(i + 1) % n]))
        return ans</code></pre></div><div class="tab-pane" data-tab="javascript"><pre><code class="language-javascript">var maxAdjacentDistance = function(nums) {
  const n = nums.length;
  let ans = 0;
  for (let i = 0; i < n; i++) {
    ans = Math.max(ans, Math.abs(nums[i] - nums[(i + 1) % n]));
  }
  return ans;
};</code></pre></div></div></article><section class="card comments"><h2>Comments</h2><script src="https://giscus.app/client.js" data-repo="Hongten/hongten.github.io" data-repo-id="MDEwOlJlcG9zaXRvcnkxODE4NTA0MTM=" data-category="General" data-category-id="DIC_kwDOCtbRLc4C3nAV" data-mapping="pathname" data-strict="0" data-reactions-enabled="1" data-emit-metadata="0" data-input-position="top" data-theme="transparent_dark" data-lang="en" crossorigin="anonymous" async></script></section><footer><a href="../../../../index.html">← Back to home</a></footer></main><script src="../../../../assets/code-tools.js"></script><script src="../../../../assets/theme.js"></script></body></html>'''
post_rel.write_text(html)
img_rel.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#0f172a"/><text x="60" y="96" fill="#e2e8f0" font-size="42" font-family="Arial">LeetCode 3423</text><text x="60" y="142" fill="#94a3b8" font-size="28" font-family="Arial">Maximum Adjacent Difference (Circular)</text><circle cx="220" cy="360" r="52" fill="#22d3ee"/><circle cx="430" cy="280" r="52" fill="#a78bfa"/><circle cx="640" cy="380" r="52" fill="#34d399"/><circle cx="850" cy="300" r="52" fill="#f59e0b"/><path d="M272 348 L378 292 M482 290 L588 356 M692 366 L798 314 M902 300 C970 305,1030 380, 930 430" stroke="#f8fafc" stroke-width="5" fill="none"/><text x="60" y="540" fill="#cbd5e1" font-size="26" font-family="Arial">Check abs(a[i]-a[i+1]), plus last-to-first</text></svg>')
idx=Path('index.html')
text=idx.read_text()
card='''      <article class="card post-card" data-date="2026-05-07T17:00:00+08:00">
        <h2><a href="./posts/leetcode/2026/05/leetcode-3423-maximum-difference-between-adjacent-elements-in-a-circular-array.html">LeetCode 3423: Maximum Difference Between Adjacent Elements in a Circular Array</a></h2>
        <div class="meta">2026-05-07 · LeetCode · Array</div>
        <p>Scan once with modulo index to include the circular last-first pair.</p>
        <a href="./posts/leetcode/2026/05/leetcode-3423-maximum-difference-between-adjacent-elements-in-a-circular-array.html">Read more →</a>
      </article>

'''
text=text.replace('<section id="posts">\n','<section id="posts">\n'+card,1)
idx.write_text(text)
obj=json.loads(Path('data/posts.json').read_text())
obj['posts'].insert(0,{"slug":"leetcode-3423-maximum-difference-between-adjacent-elements-in-a-circular-array","path":"posts/leetcode/2026/05/leetcode-3423-maximum-difference-between-adjacent-elements-in-a-circular-array.html","title":"LeetCode 3423: Maximum Difference Between Adjacent Elements in a Circular Array","date":"2026-05-07","topic":"Array","leetcodeId":3423,"sourceUrl":source,"image":"../../../../assets/img/leetcode/2026/05/leetcode-3423-20260507.svg"})
obj['count']=len(obj['posts'])
obj['generatedAt']=datetime.datetime.utcnow().isoformat()+"Z"
Path('data/posts.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
