# [392. Is Subsequence](https://leetcode.com/problems/is-subsequence)

Given two strings `s` and `t`, return `true` *if* `s` *is a **subsequence** of* `t`, or `false` *otherwise*.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).


**Example 1:**

<pre>
<b>Input:</b> s = "abc", t = "ahbgdc"
<b>Output:</b> true
</pre>

**Example 2:**

<pre>
<b>Input:</b> s = "axc", t = "ahbgdc"
<b>Output:</b> false
</pre>

**Constraints:**

- `0 <= s.length <= 100`
- <tt>0 <= t.length <= 10<sup>4</sup></tt>
- `s` and `t` consist only of lowercase English letters.
 

**Follow up:** Suppose there are lots of incoming `s`, say <tt>s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub></tt> where <tt>k >= 10<sup>9</sup></tt>, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?
