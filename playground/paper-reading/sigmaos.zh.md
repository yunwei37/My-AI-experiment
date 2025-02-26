# 弥合无服务器与微服务之间的鸿沟——SigmaOS

在当今以云为中心的世界中，对灵活、可扩展且高效的计算解决方案的需求日益增加。为满足这些需求，出现了两个突出的范式：**无服务器计算**与**微服务架构**。尽管两者各有显著优势，但它们通常针对不同的需求，并伴随各自的挑战。由MIT CSAIL的Ariel Szekely、Adam Belay、Robert Morris和M. Frans Kaashoek提出的**SigmaOS**系统应运而生，这是一项开创性的研究。本博客文章将深入探讨题为“[Unifying serverless and microservice tasks with SigmaOS](https://www.usenix.org/conference/sosp24/presentation/szekely)”的研究论文，解析其创新点、意义以及它如何旨在颠覆云计算领域。

## 目录
1. [简介](#简介)
2. [背景：无服务器与微服务](#背景无服务器与微服务)
3. [挑战](#挑战)
4. [引入SigmaOS](#引入sigmaos)
5. [SigmaOS的核心组件](#sigmaos的核心组件)
6. [实现细节](#实现细节)
7. [性能评估](#性能评估)
8. [相关工作](#相关工作)
9. [未来方向](#未来方向)
10. [结论](#结论)

---

## 简介

云计算已彻底改变了应用的开发、部署和扩展方式。在无数解决方案中，**无服务器计算**与**微服务架构**因其增强扩展性和灵活性的能力而脱颖而出。然而，要将这两种范式无缝集成一直是个挑战。MIT CSAIL在2023年的研究论文正面解决了这一问题，提出了**SigmaOS**——一个旨在统一无服务器函数和微服务的多租户云操作系统。

## 背景：无服务器与微服务

### 无服务器计算

无服务器计算使开发者无需预置或管理服务器即可运行代码。像AWS Lambda、Azure Functions和Google Cloud Functions这样的服务负责管理基础设施，根据需求自动扩展或缩减。该模型擅长处理短期、无状态任务，并具备快速扩展的能力。

### 微服务架构

另一方面，微服务架构则将应用拆分为较小的、独立的服务，这些服务通过定义良好的API进行通信。借助Kubernetes等工具进行编排，微服务非常适合构建复杂且有状态的应用。它们在开发和部署方面具有灵活性，但相较于无服务器函数，其扩展速度较慢，并且资源开销更大。

## 挑战

SigmaOS论文所讨论的核心挑战是**无服务器函数与微服务平台之间的不兼容性**。无服务器函数轻量且易于快速扩展，但在长期状态管理和服务间通信上表现不足。而像Kubernetes这样的微服务平台虽然能有效管理有状态应用，但在快速扩展和管理众多容器方面却存在局限性。

正如作者所指出的：

“无服务器函数虽然轻量，但不能作为具有长期状态的服务器运行；而容器编排提供了通用计算能力，但实例启动时间过长，无法支持突发式并行。”

## 引入SigmaOS

SigmaOS作为填补这一空白的解决方案应运而生。它是一个**多租户云操作系统**，结合了无服务器计算与微服务编排的最佳特性。SigmaOS引入了一个统一平台，使无服务器函数和微服务能够共存，使开发者能够利用这两种范式的优势而不受其固有限制的影响。

摘要中提到：

“σOS是一种全新的多租户云操作系统，支持长期运行的有状态执行和短期进程。”

## SigmaOS的核心组件

为了实现其统一架构，SigmaOS引入了几个关键概念：

### 进程（Procs）

在SigmaOS中，最基本的计算单位称为**proc**。一个proc可以表示一个无服务器函数或一个微服务组件，从而实现多样化的执行模型。

“σOS中的一个工作单元称为proc。σOS假设这些proc将使用云存储，因此不会为每个proc创建本地读写文件系统，从而节省开销。”

### σEPs（Sigma终端）

为了在同一个租户的proc之间实现高效通信，SigmaOS引入了**σEPs**。这是一种新颖的抽象概念，允许proc之间进行安全且低开销的通信，从而避免了传统网络隔离技术的需求。

“σEPs是一种新奇的抽象，为proc之间提供低开销的网络通信，但仅允许同一租户内的proc之间进行通信，并且具有严格的安全隔离。”

### σ容器（σcontainers）

SigmaOS采用轻量级容器，称为**σcontainers**，来实现proc隔离。与传统容器不同，σcontainers针对快速启动和最小化开销进行了优化，从而确保SigmaOS能高效处理突发的无服务器任务和稳定的微服务工作负载。

“σcontainers为proc提供与传统容器相当的隔离效果，但启动时间更快。”

## 实现细节

SigmaOS使用Go语言进行原型开发，利用其并发模型高效管理proc和σEPs。该系统通过避免设置网络命名空间和重叠文件系统（这些通常会耗费大量时间）而显著减少了传统容器编排的开销。

“传统的缓慢原因之一在于，每个实例需要启动一个带有Linux安装的容器编排实例：一个隔离的读写文件系统或网络。”

通过绕开这些步骤，SigmaOS实现了极其快速的proc启动时间，这对于无服务器与微服务的工作负载都至关重要。

## 性能评估

论文对SigmaOS与现有平台如AWS Lambda、Docker和Kubernetes进行了全面评估。主要发现包括：

### Proc启动延迟

与AWS Lambda和Kubernetes相比，SigmaOS展示了**显著更低的冷启动时间**。AWS Lambda和Kubernetes的冷启动延迟大约在1.3到2.7秒之间，而SigmaOS的启动时间低至7.7毫秒。

“微基准测试显示，σOS可以在7.7毫秒内冷启动一个proc，并且每秒可以创建36,650个proc，这些proc分布在一个拥有24台机器的集群中。”

### 吞吐量与可扩展性

SigmaOS在每秒处理大量proc创建方面表现卓越，非常适合需要快速扩展的应用。

“σOS在生成速率达到星级速率之前，每秒能够启动36,650个proc。”

### 网络性能

借助σEPs，SigmaOS实现了**高性能的proc间网络通信**，其性能优于传统基于容器的网络方法。

“一项通信微基准测试显示，σOS的σEPs每个数据包延迟降低了48%，吞吐量提高了14%，相比于Docker和Kubernetes的重叠网络。”

### 应用级性能

利用DeathStarBench的基准测试，尤其是酒店和社交网络应用，SigmaOS不仅在延迟和吞吐量上达到了Kubernetes水平，而且表现**更为出色**。

“σOS-hotel和σOS-socialnet分别实现了比Kubernetes高1.68倍和3.01倍的峰值吞吐量。”

## 相关工作

SigmaOS在云计算、容器编排和无服务器架构领域丰富的研究基础上构建。它在调度方面受到Borg和Kubernetes等系统的启发，并在无服务器执行方面借鉴了AWS Lambda的经验。但其独特贡献在于通过σEPs和σcontainers等创新抽象，实现了这两种范式的无缝整合。

“与以往的工作相比，σOS的主要贡献在于它在一个以云为中心的平台中统一支持无服务器与微服务任务，同时通过σEPs实现网络隔离和通过σcontainers实现proc隔离。”

## 未来方向

尽管SigmaOS已经展示了一套健壮的解决方案，作者仍然指出了未来改进的方向：

1. **增强安全功能**：在σOS中实现细粒度授权和更全面的安全策略。
2. **支持异构资源**：扩展SigmaOS以支持GPU资源及其他专用硬件，以满足多样化的应用需求。
3. **高级调度算法**：优化调度器以更好地处理混合型工作负载，并动态优化资源分配。

## 结论

SigmaOS在云计算领域代表了一项重大进展，它有效地弥合了无服务器函数与微服务之间的鸿沟。通过提供一个将两者优势结合于一体的统一平台，SigmaOS使开发者能够构建出更高效、可扩展且灵活的应用。其在proc启动延迟与网络吞吐量方面令人印象深刻的性能指标，凸显了其在未来多租户云操作系统中的潜力。

随着云原生应用的不断进化，像SigmaOS这样的系统将在满足对速度、可扩展性和灵活性日益增长的需求方面发挥关键作用。即将在SOSP’24上进行的发布会无疑将进一步阐明SigmaOS的能力及其对更广泛的计算社区的意义。

---

**参考文献：**
- Szekely, A., Belay, A., Morris, R., & Kaashoek, M. F. (2023). *Unifying serverless and microservice tasks with SigmaOS*. MIT CSAIL. [论文链接](https://www.usenix.org/conference/sosp24/presentation/szekely)
- [DeathStarBench](http://www.deathstarbench.org)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Kubernetes](https://kubernetes.io/)

*这篇博客文章基于MIT CSAIL的Ariel Szekely、Adam Belay、Robert Morris和M. Frans Kaashoek于2023年11月提出的研究论文“[Unifying serverless and microservice tasks with SigmaOS](https://www.usenix.org/conference/sosp24/presentation/szekely)”。*

> 了解更多请访问 <https://yunwei37.github.io/My-AI-experiment/> 或者GitHub：<https://github.com/yunwei37/My-AI-experiment>