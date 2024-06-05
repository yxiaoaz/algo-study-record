# Coin Change

## Basic Info: 

|  |  |
| --- | --- |
| **Source** | Leetcode #322 |
| **Link** | https://leetcode.com/problems/coin-change/description/ |

## Problem Description

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

### Example 1:

    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

### Example 2:

    Input: coins = [2], amount = 3
    Output: -1

### Example 3:

    Input: coins = [1], amount = 0
    Output: 0

## Solution

Given $coins = [c_1, ..., c_n]$, assume that the minimum number of coins to use to get $a$ dollars is $minCoin(a)$. 

Similar to the staircase problem, we can view this problem in the following way:
$$minCoin(a) = \min{\{1 + minCoin(a-c_i): c_i  \in coins\}}$$

In other words, given the last coin to use is $c_i$, the optimal solution for reaching $a$ builds upon the optimal solution for reaching $a-c_i$.