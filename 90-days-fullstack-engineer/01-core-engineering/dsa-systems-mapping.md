# DSA and OOP Patterns → Real Systems

LeetCode patterns are not interview tricks. They are the building blocks of every system you will work on.

This document maps every major pattern to its real-world backend counterpart.
Every time you solve a LeetCode problem, check this map: where does this exact pattern appear in production systems?

---

## Data Structures → Real System Uses

### Hash Map / Hash Table

| LeetCode use | Real system use |
|-------------|----------------|
| Two Sum (check if complement exists) | Cache hit/miss check — "Is this key already cached?" |
| Group anagrams | Grouping events by user ID, session ID, or correlation ID |
| First unique character | Deduplication — "Have I already processed this event?" (idempotency keys) |
| LRU Cache | Every cache eviction policy. Session store. In-memory rate limiter. |

**Key insight:** A hash map is a materialized index. When you add an index to a database column, you are building a hash map (or B-tree) on disk. Same concept.

**Where you'll build this:** Rate limiting (IP → request count), session management (token → user ID), request deduplication (idempotency key → response).

---

### Graph (BFS/DFS)

| LeetCode use | Real system use |
|-------------|----------------|
| BFS shortest path | Network routing (Dijkstra's), dependency resolution, recommendation engines |
| DFS all paths | File system traversal, crawlers, transitive dependency resolution |
| Detect cycle | Circular import detection, deadlock detection in distributed locks |
| Connected components | Network topology analysis, finding isolated service clusters |
| Topological sort | Build system dependency ordering, CI/CD pipeline step ordering, DB migration ordering |

**Key insight:** Most systems are graphs. Services depend on other services. Users follow other users. Jobs depend on other jobs. When you need to process dependencies correctly, you need graph algorithms.

**Where you'll build this:** Job scheduler (topological sort for dependencies), recommendation engine (BFS from user node), import cycle detection in build tools.

---

### Tree (Binary Tree, BST, Trie)

| LeetCode use | Real system use |
|-------------|----------------|
| BST search/insert | Database B-tree index — every `WHERE id = X` query uses this |
| Trie (prefix tree) | Autocomplete, search prefix matching, IP routing (longest prefix match), DNS |
| Segment tree | Range queries on time-series data |
| Binary tree traversal | Directory listing, XML/JSON parsing, abstract syntax tree processing |
| LCA (lowest common ancestor) | Finding common category in product taxonomy, finding common ancestor in org chart |

**Key insight:** Database indexes are B-trees (balanced BST variant). Every indexed query is a tree traversal. Understanding BST operations explains why index scans are fast and table scans are slow.

**Where you'll build this:** Autocomplete API (Trie), search with prefix matching, hierarchical category navigation.

---

### Heap / Priority Queue

| LeetCode use | Real system use |
|-------------|----------------|
| K largest elements | Top-N ranking: "top 10 most active users", "top products by revenue" |
| Merge K sorted lists | Merging sorted streams from multiple Kafka partitions |
| Task scheduling | Priority queues in BullMQ — high-priority jobs run before low-priority jobs |
| Dijkstra's algorithm | Network routing with weighted edges, finding cheapest deployment path |
| Running median | Real-time percentile calculation for latency metrics (P50, P95, P99) |

**Key insight:** Any time you need to repeatedly find the "best" item from a changing collection, you need a heap. Sorted list is O(n log n) to rebuild. Heap is O(log n) to update.

**Where you'll build this:** Job queue with priorities, real-time leaderboard, streaming metrics with percentile tracking.

---

### Stack

| LeetCode use | Real system use |
|-------------|----------------|
| Valid parentheses | Syntax validation in template engines, HTML/XML parsing, bracket matching in code editors |
| Evaluate expression | Math expression parsers, formula engines, query builders |
| Monotonic stack | Stock span → caching freshness windows, histogram → capacity planning |
| Function call tracing | Call stack in debuggers, distributed tracing (parent → child span relationships) |

**Key insight:** The call stack in your runtime IS a stack data structure. Stack traces in error logs are a literal stack being unwound. Understanding this makes distributed tracing intuitive.

---

### Linked List

| LeetCode use | Real system use |
|-------------|----------------|
| LRU Cache (with hash map) | Browser cache, CDN edge cache, in-memory query cache |
| Reverse linked list | Reversing undo history, reversing a message queue |
| Detect cycle | Circular reference detection in object graphs |
| Merge sorted lists | Merge step in merge sort (used in external sorting for large datasets) |

**Key insight:** Doubly linked list + hash map = O(1) LRU cache. This exact combination is used in Redis's eviction policies, browser page history, and in-memory query result caches.

---

## Algorithm Patterns → Real System Uses

### Sliding Window

| LeetCode use | Real system use |
|-------------|----------------|
| Max sum subarray of size K | Aggregate metrics over a rolling time window |
| Longest substring without repeat | Find longest session without a specific error type |
| Minimum window substring | Find the smallest time range containing all required events |

**Key insight:** Rate limiting uses sliding window. Fixed window (count resets at minute boundary) is cheaper but burstable. Sliding window (count over the last 60 seconds, always) is accurate. Redis sorted sets implement sliding window rate limiting.

**Where you'll build this:** Rate limiting middleware, rolling average calculation, session activity detection.

---

### Two Pointers

| LeetCode use | Real system use |
|-------------|----------------|
| Two Sum on sorted array | Merge sorted arrays (merge step in merge sort) |
| Container with most water | Resource allocation problems with min/max constraints |
| Remove duplicates | Deduplication on sorted streams |
| Palindrome check | Data validation for symmetric structures |

**Key insight:** Merge sorted lists with two pointers is the core of merge sort. Merge sort is what databases use when sorting data that doesn't fit in memory (external sort). Two pointers also models the read/write pointer in stream processing.

---

### Binary Search

| LeetCode use | Real system use |
|-------------|----------------|
| Search in sorted array | Finding a threshold: "what's the minimum server count to handle this load?" |
| Find first/last position | Range queries on sorted event timestamps |
| Search in rotated array | Finding records in partitioned/sharded data with a known partition key range |
| Koko eating bananas | Finding optimal rate: "what's the minimum batch size that processes all jobs within SLA?" |

**Key insight:** Binary search is valid any time you can answer "is the answer in the left half or the right half?" This applies to sorted arrays, monotonic functions, and any problem where you can eliminate half the search space per step.

**Where you'll build this:** Capacity planning models, configuration search ("what's the minimum cache size for X% hit rate?"), event log range queries.

---

### Dynamic Programming

| LeetCode use | Real system use |
|-------------|----------------|
| Knapsack | Optimal resource allocation: "which features fit in this sprint's capacity?" |
| Longest common subsequence | Diff algorithms (git diff), DNA sequence alignment |
| Coin change | Minimum number of requests/operations to achieve a target |
| Edit distance | Fuzzy search, spell correction, record deduplication across datasets |

**Key insight:** DP problems have two properties: optimal substructure (optimal solution uses optimal sub-solutions) and overlapping subproblems (same sub-problems recur). When you see these in a system problem, DP is likely the right tool.

---

### Backtracking

| LeetCode use | Real system use |
|-------------|----------------|
| Subsets / combinations | Feature flag combinations, test case generation |
| N-Queens | Constraint satisfaction: scheduling with mutual exclusions |
| Word search | Pattern matching in structured data |

**Key insight:** Database query planners use backtracking to find optimal join orders. The query planner tries a join order, estimates its cost, backtracks if there's a better option. Understanding backtracking makes EXPLAIN ANALYZE output readable.

---

### Union Find (Disjoint Set)

| LeetCode use | Real system use |
|-------------|----------------|
| Number of islands | Connected components in a network topology |
| Detect cycle in graph | Detecting circular dependencies in service graphs |
| Redundant connection | Finding the extra link that creates a cycle in a service mesh |

**Key insight:** Union-Find is the algorithm behind network partitioning detection. In distributed systems, when a network partition occurs, connected components are detected with a variant of this algorithm.

---

## OOP Patterns → Real System Uses

### Strategy Pattern

**LeetCode analog:** Choosing between different sort algorithms based on data size.

**Real system use:** Payment processing (choose PayPal, Stripe, or Crypto strategy at runtime), shipping rate calculation (choose USPS, FedEx, DHL strategy), authentication (choose JWT, session, API key strategy).

```typescript
interface AuthStrategy {
  authenticate(req: Request): Promise<User>;
}

class JWTStrategy implements AuthStrategy { ... }
class SessionStrategy implements AuthStrategy { ... }
class APIKeyStrategy implements AuthStrategy { ... }
```

---

### Observer Pattern

**LeetCode analog:** Event-driven problems where state change triggers multiple reactions.

**Real system use:** Event emitters in Node.js, webhooks, domain events in DDD (OrderPlaced → send email + update inventory + log audit), React state updates.

```typescript
// Every EventEmitter.on() is the observer pattern
orderService.on('order:placed', async (order) => {
  await emailService.sendConfirmation(order);
  await inventoryService.reserve(order.items);
  await auditLog.record('order:placed', order.id);
});
```

---

### Repository Pattern

**LeetCode analog:** Abstracting data access behind an interface.

**Real system use:** Separating business logic from database access. Allows swapping databases (Postgres → MongoDB) or mocking in tests without changing business logic.

```typescript
interface UserRepository {
  findById(id: string): Promise<User | null>;
  save(user: User): Promise<User>;
  delete(id: string): Promise<void>;
}

class PostgresUserRepository implements UserRepository { ... }
class InMemoryUserRepository implements UserRepository { ... } // for tests
```

---

### Factory Pattern

**LeetCode analog:** Creating objects based on a type parameter.

**Real system use:** Creating the right database connection based on config, instantiating the right payment provider, building the right notification sender (email vs. SMS vs. push).

```typescript
class NotificationFactory {
  static create(channel: 'email' | 'sms' | 'push'): NotificationSender {
    switch (channel) {
      case 'email': return new EmailSender();
      case 'sms': return new SMSSender();
      case 'push': return new PushSender();
    }
  }
}
```

---

### Decorator Pattern

**LeetCode analog:** Adding functionality to a class without modifying it.

**Real system use:** Middleware in Express (each `app.use()` is a decorator), caching decorators (wrap a function to cache its result), logging decorators (wrap a function to log calls), retry decorators (wrap a function to retry on failure).

```typescript
function withCache(fn: (id: string) => Promise<User>): (id: string) => Promise<User> {
  return async (id: string) => {
    const cached = await redis.get(`user:${id}`);
    if (cached) return JSON.parse(cached);
    const user = await fn(id);
    await redis.set(`user:${id}`, JSON.stringify(user), 'EX', 300);
    return user;
  };
}
```

---

## Pattern selection cheat sheet

When you see a problem type, reach for this pattern:

| Problem type | Pattern |
|-------------|---------|
| "Find X in a sorted array/range" | Binary search |
| "All elements within a window" | Sliding window |
| "Shortest path between A and B" | BFS (unweighted) / Dijkstra (weighted) |
| "All possible combinations/paths" | Backtracking or DFS |
| "Optimal value across choices" | Dynamic programming |
| "Dependencies must be processed in order" | Topological sort |
| "Find the Kth largest/smallest" | Heap |
| "Fast lookup by key" | Hash map |
| "Detect a cycle" | Fast/slow pointers (Floyd) or Union-Find |
| "Range queries on sorted data" | Segment tree or Binary indexed tree |
| "Prefix matching / autocomplete" | Trie |
| "Balanced ordering" | BST or sorted set |
| "Two sorted lists/arrays to merge" | Two pointers |

---

## The practice rule

For every pattern you learn:
1. Solve 2–3 LeetCode problems with it
2. Identify one place in the system (this repo's platform) where the same pattern applies
3. Write the real-world mapping in your solution file

If you cannot name a real-world use, you have not understood the pattern — you have only memorized the code.
