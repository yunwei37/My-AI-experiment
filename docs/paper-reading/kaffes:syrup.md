# Introducing Syrup: Revolutionizing Scheduling Across the Computing Stack

In the ever-evolving landscape of computing systems, performance optimization remains a critical challenge. As applications grow in complexity and demand, the underlying operating systems (OS) must adapt to ensure efficient resource utilization. Enter **Syrup**, a groundbreaking framework presented by Kostis Kaffes, Jack Tigar Humphries, David Mazières, and Christos Kozyrakis from Stanford University at the **ACM Symposium on Operating Systems Principles (SOSP) 2021**. Published on October 26–29, 2021, in the virtual event in Germany, Syrup promises to redefine how scheduling is handled across the entire software stack.

![Figure1](https://example.com/figure1_syrup.png)
*Figure 1: Syrup enables user-defined scheduling across the stack.*

## Table of Contents

1. [The Scheduling Conundrum](#the-scheduling-conundrum)
2. [What is Syrup?](#what-is-syrup)
3. [Deep Dive: How Syrup Works](#deep-dive-how-syrup-works)
4. [Implementation Insights](#implementation-insights)
5. [Performance Benchmarks](#performance-benchmarks)
6. [Comparative Analysis: Syrup vs. Traditional Schedulers](#comparative-analysis-syrup-vs-traditional-schedulers)
7. [Broader Implications and Future Directions](#broader-implications-and-future-directions)
8. [Conclusion](#conclusion)
9. [References](#references)

## The Scheduling Conundrum

**Scheduling** is a foundational operation in computer systems, determining how tasks are allocated to processing units. Traditional schedulers, like the Linux Completely Fair Scheduler (CFS), operate with generic policies aiming to balance fairness and efficiency across all processes. However, as the authors note:

> "Syrup enables untrusted application developers to express application-specific scheduling policies across these execution resources... and improve performance up to 8× compared with often an order of magnitude or more more [18,27,38,40,42]."

This highlights a significant limitation: **default scheduling policies often result in suboptimal performance for specific application classes**, leading to higher latency and lower throughput.

## What is Syrup?

Syrup is introduced as a **framework for user-defined scheduling across the stack**. Unlike traditional schedulers embedded deeply within the OS kernel, Syrup empowers developers to **customize scheduling policies** tailored to their application's unique characteristics and requirements.

The authors succinctly describe Syrup's essence:

> "Syrup allows application developers to specify scheduling policies in a safe, efficient, and high-level manner across the stack."

By treating scheduling as a **matching problem**, Syrup maps units of work (e.g., network packets, threads) to execution resources (e.g., cores, network sockets) using **user-defined functions**. This abstraction not only simplifies the implementation of custom policies but also ensures that these policies can be deployed seamlessly across different system layers.

## Deep Dive: How Syrup Works

At its core, Syrup addresses the **lack of coherence and coordination** across multiple scheduling layers in a traditional stack. Here's a breakdown of its operational model:

1. **User-Defined Policies**: Developers write scheduling policies as a set of matching functions. These functions determine how inputs (like threads or network connections) are mapped to executors (like CPU cores or network sockets).
   
   > "The only thing this user-defined function needs to do is select an executor for the input passed to it as an argument."

2. **Policy Deployment**: Syrup introduces system hooks across various stack layers, including the network stack and the thread scheduler. Policies are deployed at these hooks, allowing them to function across the entire stack without intrusion into low-level system mechanisms.

3. **Abstraction via Maps**: Scheduling decisions use a **Map abstraction**, facilitating communication between layers and ensuring that policies remain modular and maintainable.

4. **Isolation and Safety**: Syrup ensures that policies from one application **cannot interfere** with others, maintaining system stability and performance integrity.

![Figure3](https://example.com/figure3_schedulingworkflow.png)
*Figure 3: Scheduling workflow in Syrup.*

## Implementation Insights

Syrup leverages modern kernel features such as **eBPF (Extended Berkeley Packet Filter)** and **ghOSt** to implement its scheduling policies safely and efficiently.

- **eBPF**: Acts as a vehicle to inject user-defined code into the kernel in a sanitized manner, ensuring that policies do not compromise system stability. Policies are compiled into eBPF bytecode and loaded into the kernel, where they handle scheduling decisions.

- **ghOSt**: A lightweight user-space scheduler that offloads thread scheduling decisions, allowing Syrup to implement more complex and centralized scheduling policies without incurring significant context-switching overhead.

The combination of these technologies allows Syrup to:

> "Treat scheduling as a series of 'small' decisions, implementing a custom scheduling policy for even the most complex policies."

This design ensures that policies remain **composable and understandable**, enabling developers to achieve significant performance improvements with minimal effort.

## Performance Benchmarks

One of Syrup's standout claims is its ability to **improve performance up to 8×** compared to default scheduling policies. The paper presents several benchmarks to substantiate this:

### RocksDB Workload

RocksDB, a popular in-memory key-value store, was used to evaluate Syrup's efficacy. By implementing a user-defined scheduling policy, Syrup achieved:

- **60% Reduction** in 99% tail latency compared to the default Linux scheduler.
- **Eightfold Increase** in throughput, handling significantly higher requests per second (RPS) without sacrificing responsiveness.

> "Using Syrup, we also deploy custom policies for the application characteristics can reduce or eliminate problems such as head-of-line blocking."

### MICA Key-Value Store

MICA, another key-value store, was employed to test Syrup's cross-layer scheduling capabilities. Syrup demonstrated its prowess by:

- Allowing coordinated scheduling across network and thread layers, leading to substantial improvements in both latency and throughput.
- Ensuring policies are portable across different stack layers, maintaining performance consistency.

![Figure6](https://example.com/figure6_rocksdb_performance.png)
*Figure 6: Performance of a RocksDB workload running on 6 cores and serving 99.5% GET-0.5% SCAN requests using different Syrup scheduling policies.*

## Comparative Analysis: Syrup vs. Traditional Schedulers

Traditional schedulers like Linux's CFS are designed with general-purpose workloads in mind. While effective for a broad range of applications, they often fall short for specialized tasks that could benefit from tailored scheduling policies.

**Syrup's Advantages:**

1. **Customization**: Developers can define policies that align closely with their application's needs, avoiding the constraints of one-size-fits-all schedulers.
   
2. **Cross-Layer Coordination**: By enabling scheduling decisions across multiple stack layers, Syrup ensures coherence and reduces performance bottlenecks.
   
3. **Minimal Overhead**: Despite the high degree of customization, Syrup maintains low overhead, ensuring that the performance gains are not offset by the framework's own resource consumption.

4. **Safety and Isolation**: Ensures that custom policies do not interfere with system stability or other applications, a crucial feature in multi-tenant environments.

**Real-World Implications:**

Consider a data center running high-performance databases like RocksDB and MICA. Traditional schedulers might allocate resources based purely on fairness, leading to scenarios where latency-sensitive GET requests are delayed behind bulk SCAN operations. Syrup's user-defined policies can prioritize GET requests, ensuring low latency without sacrificing overall throughput.

## Broader Implications and Future Directions

Syrup represents a significant step towards **programmable operating systems**, where developers have granular control over system behaviors without delving into low-level kernel modifications. This approach aligns with broader trends in system design, emphasizing **flexibility, efficiency, and developer empowerment**.

**Potential Extensions:**

1. **Distributed Scheduling**: Extending Syrup's framework to handle distributed systems, enabling coordinated scheduling across multiple nodes.
   
2. **Integration with Emerging Hardware**: Leveraging advances in programmable network interfaces and specialized accelerators to enhance Syrup's capabilities.
   
3. **Enhanced Security Features**: Building upon Syrup's isolation guarantees to introduce more robust security policies, preventing potential misuse of scheduling policies.

The authors acknowledge these avenues, hinting at a future where Syrup could become a foundational tool in system optimization.

## Conclusion

**Syrup** emerges as a transformative framework in the realm of operating system scheduling. By empowering developers to define and deploy custom scheduling policies across the entire system stack, Syrup not only addresses the limitations of traditional schedulers but also paves the way for future innovations in system performance optimization.

As computing demands continue to surge, frameworks like Syrup will be instrumental in ensuring that applications run efficiently, responsively, and reliably. The research presented at **SOSP 2021** serves as a testament to the ongoing strides in making operating systems more adaptable and developer-friendly, heralding a new era of **user-defined system optimizations**.

## References

1. Kaffes, K., Humphries, J. T., Mazières, D., & Kozyrakis, C. (2021). Syrup: User-Defined Scheduling Across the Stack. In *Proceedings of the 28th ACM Symposium on Operating Systems Principles (SOSP’21)*. ACM. https://doi.org/10.1145/3477132.3483548
2. Additional references as cited in the original paper.

*Note: For a comprehensive understanding and detailed implementation insights, readers are encouraged to refer directly to the [Syrup paper](https://doi.org/10.1145/3477132.3483548).*

> For more interesting AI experiments and insights, please visit my AI experiment and throughts website <https://yunwei37.github.io/My-AI-experiment/> and github repo: <https://github.com/yunwei37/My-AI-experiment>
