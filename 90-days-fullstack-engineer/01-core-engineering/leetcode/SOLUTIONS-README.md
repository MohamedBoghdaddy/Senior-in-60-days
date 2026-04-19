# LeetCode Solutions

## The rule: every solution must have 3 parts

Every solution file must include:
1. **Brute force** — the obvious O(n²) or recursive solution. Write it. Understand it. Don't skip it.
2. **Optimized** — the better solution. Know *why* it is better and *what insight* unlocked it.
3. **Real-world mapping** — where does this pattern appear in real backend/systems work?

If you only write the optimized solution, you do not understand the problem.
You have pattern-matched. That is not the same as thinking.

---

## Directory structure

```
solutions/
  day01/
    001-two-sum.py
    002-best-time-buy-sell-stock.py
  day02/
    003-product-array-except-self.py
  ...
  day38/
    001-two-sum.cpp
    002-valid-parentheses.cpp
```

---

## Required Python solution format

```python
# ============================================================
# Problem: Two Sum
# Difficulty: Easy
# Pattern: Hash Map
# Date: YYYY-MM-DD
# ============================================================

# REAL-WORLD MAPPING:
# This pattern appears in:
# - Cache lookup: "Is this request ID already in the cache?"
# - Deduplication: "Have I seen this event before?" (idempotency keys)
# - Index building: Hash map IS an index (e.g., PostgreSQL hash index)
# - Rate limiting: "How many requests from this IP in this window?"
# The core insight: trade O(n) space for O(1) lookup, eliminating O(n) scan.

from typing import List


# ── BRUTE FORCE ──────────────────────────────────────────────
# Check every pair. O(n²) time, O(1) space.
# Write this first — it makes the optimization obvious.
def twoSum_brute(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
# Time: O(n²) — two nested loops
# Space: O(1) — no extra storage
# Why it's slow: we re-scan the array for every element.


# ── OPTIMIZED ─────────────────────────────────────────────────
# Key insight: instead of scanning for the complement, store what
# we've seen and look it up in O(1).
# One pass: check if complement exists, then store current.
def twoSum(nums: List[int], target: int) -> List[int]:
    seen: dict[int, int] = {}          # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i                  # insert AFTER checking (prevents same-element reuse)
    return []
# Time: O(n) — single pass
# Space: O(n) — hash map stores at most n elements
# Key decision: insert after check, not before. This prevents using nums[i] twice.


# ── WHAT I LEARNED ───────────────────────────────────────────
# The O(n²) → O(n) jump comes from asking "what do I need to have
# already seen?" instead of "what do I need to find next?"
# This framing works for: Two Sum, 3Sum, 4Sum, LRU cache design.
# The hash map is just a materialized index — same idea as adding a
# database index to avoid a full table scan.
```

---

## Required C++ solution format

```cpp
// ============================================================
// Problem: Two Sum
// Difficulty: Easy
// Pattern: Hash Map
// Date: YYYY-MM-DD
// ============================================================
//
// REAL-WORLD MAPPING:
// Same as Python version — cache lookups, dedup, index building.
// In C++: unordered_map<int,int> is a hash table (avg O(1) ops).
// map<int,int> is a balanced BST (O(log n) ops) — use when you need sorted order.

#include <vector>
#include <unordered_map>
using namespace std;


// ── BRUTE FORCE ──────────────────────────────────────────────
vector<int> twoSum_brute(vector<int>& nums, int target) {
    for (int i = 0; i < (int)nums.size(); i++) {
        for (int j = i + 1; j < (int)nums.size(); j++) {
            if (nums[i] + nums[j] == target) return {i, j};
        }
    }
    return {};
}
// Time: O(n²)   Space: O(1)


// ── OPTIMIZED ─────────────────────────────────────────────────
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen;       // value → index
    for (int i = 0; i < (int)nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement)) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {};
}
// Time: O(n) average (hash collisions make worst case O(n²), rare in practice)
// Space: O(n)
// STL used: unordered_map — O(1) avg insert and lookup
// Alternative: map<int,int> would give O(n log n) but sorted iteration


// ── WHAT I LEARNED ───────────────────────────────────────────
// unordered_map vs map:
//   unordered_map: O(1) avg — use when order doesn't matter
//   map:           O(log n)  — use when you need sorted keys (e.g., prefix sums in order)
// seen.count(k) vs seen.find(k) != seen.end(): both work, count is cleaner for existence check
```

---

## Real-world mappings reference

This is the key discipline that separates interview-prep LeetCode from engineering LeetCode.

For every pattern, know where it appears in real systems:

| Pattern | Real-world system appearance |
|---------|------------------------------|
| Hash Map (lookup) | Cache hit/miss check, deduplication, ID-to-object mapping, database hash indexes |
| Sliding Window | Rate limiting (fixed/sliding window), session activity detection, time-series aggregation |
| Two Pointers | Merge sorted arrays (merge step in merge sort), stream merging in Kafka consumers |
| BFS (shortest path) | Network routing (Dijkstra), service dependency resolution, recommendation engines |
| DFS (all paths) | File system traversal, crawlers, transitive dependency resolution |
| Topological Sort | Build system dependency ordering, CI/CD pipeline step ordering, migration ordering |
| Dynamic Programming | Optimal resource allocation, CDN cache eviction scoring, route optimization |
| Backtracking | Query planner (trying execution plans), regex matching, constraint solvers |
| Heap/Priority Queue | Task scheduling (BullMQ job priority), Dijkstra's algorithm, merge K sorted streams |
| Binary Search | Finding a breakeven threshold, time-range queries on sorted event logs, versioned config rollout |
| Union Find | Connected components in a network graph, detecting circular dependencies |
| Trie | Autocomplete (search prefix matching), IP routing (longest prefix match), DNS |
| Monotonic Stack | Stock span problem → caching freshness windows, histogram → capacity planning |
| Interval scheduling | Calendar booking, reservation systems, resource allocation slots |
| LRU Cache | Every cache eviction policy you will ever implement |

---

## Quality gate

Before marking any solution as complete in the progress tracker, it must pass:

- [ ] Brute force solution written (even if trivially obvious)
- [ ] Optimized solution written with time/space complexity annotated
- [ ] Key insight stated in one sentence (what unlocked the optimization?)
- [ ] Real-world mapping written (where does this appear in systems?)
- [ ] For C++ solutions: STL container named and the O() of that container noted
- [ ] "What I learned" section is not empty and is specific (not "I learned about hash maps")

A solution file that is just code is not a complete entry.
The commentary is what proves you understood it.
