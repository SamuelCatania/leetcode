# [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings)

Given two strings `s` and `t`, *determine if they are isomorphic*.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

**Example 1:**

<pre>
<b>Input:</b> s = "egg", t = "add"
<b>Output:</b> true
</pre>

**Example 2:**

<pre>
<b>Input:</b> s = "foo", t = "bar"
<b>Output:</b> false
</pre>

**Example 3:**

<pre>
<b>Input:</b> s = "paper", t = "title"
<b>Output:</b> true
</pre>

**Constraints:**

- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ascii character.
