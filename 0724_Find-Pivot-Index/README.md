# [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers **strictly** to the left of the index is equal to the sum of all the numbers **strictly** to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return the ***leftmost pivot index***. If no such index exists, return `-1`.


**Example 1:**

<pre>
<b>Input:</b> nums = [1,7,3,6,5,6]
<b>Output:</b> 3
<b>Explanation:</b>
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
</pre>

**Example 2:**

<pre>
<b>Input:</b> nums = [1,2,3]
<b>Output:</b> -1
<b>Explanation:</b>
There is no index that satisfies the conditions in the problem statement.
</pre>

**Example 3:**

<pre>
<b>Input:</b> nums = [2,1,-1]
<b>Output:</b> 0
<b>Explanation:</b>
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
</pre>

**Constraints:**

- <tt>1 <= nums.length <= 10<sup>4</sup></tt>
- `-1000 <= nums[i] <= 1000`
