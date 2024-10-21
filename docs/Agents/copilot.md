# GitHub Copilot 背后的 AI 编码技术：如何让 GPT 更好地理解你的代码


AI 编码工具正在逐渐改变我们的编程习惯和体验，GitHub Copilot 是这一变革的最佳代表。这款产品利用强大的算法，根据开发者的上下文和需求，从多个来源挑选出最相关的代码片段和注释，进而生成编码建议。在这篇文章中，我们将深入探讨 GitHub Copilot 背后的技术思路，结合通过逆向工程获取的部分 copilot prompt，希望能为构建 AI 辅助的编码工具提供一些帮助。这里的内容部分翻译整理自微软的博客，我们也会讨论其他人的研究成果和观点。

> GitHub Copilot 通过算法从多个来源选择相关代码片段或注释，并使用上下文理解能力生成编码建议。GitHub Copilot 创建了精巧的提示词工程的方案，并在提示库中优先处理有关开发人员上下文的信息，使用向量数据库为在私有存储库中或处理专有代码的开发人员创建了定制化的编码体验。

为了让使用 GitHub Copilot 的开发人员感觉像是与另一个程序员合作，GitHub的机器学习专家一直在研究、开发和测试新功能，其中很多都集中在提高 AI 程序员的上下文理解能力。这是因为良好的交流对于合作编程至关重要，推断上下文对于实现良好的交流至关重要。

为了揭示这些背后的工作，原文作者向 GitHub 的研究员和工程师询问了他们正在做的帮助 GitHub Copilot 提高上下文理解能力的工作。以下是他们发现的内容。

从OpenAI的Codex模型到GitHub Copilot
------------------------------

当OpenAI在2020年6月发布GPT-3时，GitHub 知道开发人员将从专门为编码利用该模型的产品中受益。因此，他们向 OpenAI 提供输入，帮助其构建 Codex，它是GPT-3和LLM的后代，将驱动GitHub Copilot。这款程序员配对工具于2021年6月发布为技术预览版，并于2022年6月成为世界上第一个大规模生成式AI编码工具。

为确保该模型具有最佳信息，以便快速做出最佳预测，GitHub的机器学习（ML）研究员进行了大量称为提示工程的工作（将在下面详细解释），以便模型提供上下文相关的响应，并具有低延迟。

尽管GitHub总是在尝试新模型，但Codex是第一个真正强大的生成式AI模型，也是可用的，GitHub的机器学习工程师David Slater表示：“我们从模型和提示改进的迭代中获得的实践经验是非常宝贵的。”

所有这些实验最终导致了一款 pair programming 工具，最终“释放了开发人员的时间，让他们专注于更有意义的工作”。该工具甚至对于从头开始启动新项目或文件也是一个巨大的帮助，因为它提供了一个开发人员可以根据需要进行调整和改进的起点。GitHub的机器学习研究员Alice Li表示。

为什么上下文很重要
---------

开发人员使用拉取请求、项目文件夹、开放问题等详细信息来确定其代码的上下文。当涉及到生成AI编码工具时，Copilot 需要教这个工具使用哪些信息来做同样的事情。

Transformer LLMs 擅长连接和大局思考。生成AI 编码工具是由大型语言模型（LLMs）所支持。这些模型是在大量代码和人类语言上训练的算法集。今天的最先进的 LLMs 是 transformer ，这使它们能够在用户输入的文本和模型已经生成的输出之间建立联系,这就是为什么今天的生成AI工具提供比之前的AI模型更具上下文相关性的响应。

但是，AI 需要被告知哪些信息与您的代码相关。目前，足够快速以支持GitHub Copilot的 transformer 每次只能处理大约6,000个字符。虽然这已足以推进和加速代码完成和代码更改总结等任务，但有限的字符数量意味着无法使用开发人员的所有代码作为上下文。

因此，Copilot 的挑战是找出不仅要向模型提供哪些数据，还要如何最好地排序和输入它以获得最佳建议。

GitHub Copilot 如何理解您的代码
-----------------------

**一切都归结于提示**，这些提示是集成IDE代码和相关上下文的编译，供模型使用。提示由后台算法生成，可以在您编码的任何时候生成编码建议。这就是为什么GitHub Copilot会生成编码建议，无论您是正在编写还是刚刚完成注释，或者正在处理一些复杂的代码。

*   **下面是提示的创建过程**：首先，一系列算法从当前文件和其他来源中选择相关代码片段或注释。然后，对这些片段和注释进行优先排序，过滤和组装，形成最终的提示。
    

**GitHub Copilot的上下文理解能力不断成熟**。第一个版本只能认为您在IDE中工作的文件与上下文相关。但 Copilot 团队知道上下文超出了这个范围。现在，仅仅一年后，他们正在尝试使用算法来考虑您的整个代码库，以生成定制的建议。

他们**如何到达这里的**：

*   **提示工程**是创建提示的精细艺术，以便模型为用户提供最有用的预测。提示告诉包括GitHub Copilot在内的LLMs，要处理哪些数据，以及以什么顺序来对您的代码进行上下文化。大部分工作都在所谓的**提示库**中进行，这是专家与算法一起提取和优先处理有关开发人员上下文的各种信息的地方，创建将由GitHub Copilot模型处理的提示。
    
*   **相邻选项卡**是称之为允许GitHub Copilot处理开发人员IDE中打开的所有文件的技术，而不仅仅是开发人员正在处理的单个文件的技术。通过打开与其项目相关的所有文件，开发人员自动调用GitHub Copilot来扫描所有数据，并在其光标周围的代码之间找到匹配的代码片段，并将这些匹配项添加到提示中。
    

开发相邻选项卡时，GitHub Next团队和内部ML研究人员进行了A/B测试，以确定识别IDE中代码和打开选项卡中代码之间匹配的最佳参数。他们发现**设置非常低的门槛来包括匹配实际上会提供最佳的编码建议**。

通过包含每一个小的上下文，相邻选项卡帮助相对增加了5%的用户接受GitHub Copilot的建议。

*   **Fill-In-the-Middle（FIM）范式**进一步扩大了上下文孔径。在FIM之前，只有光标之前的代码会被放入提示中，而忽略了光标之后的代码。（在GitHub上，将光标之前的代码称为前缀，将光标之后的代码称为后缀）。**使用FIM，我们可以告诉模型提示的哪一部分是前缀，哪一部分是后缀**。
    

即使您从头开始创建文件，并且只有文件的框架，Copilot 也知道编码不是线性或顺序的。因此，当您在文件中跳来跳去时，FIM可以帮助GitHub Copilot为您的文件中光标所在的部分或前缀和后缀之间应该出现的代码提供更好的编码建议。

基于A/B测试，FIM提高了10%的相对性能，这意味着开发人员接受了他们所看到的建议中的10%以上。由于最佳的缓存使用，相邻选项卡和FIM在后台运行，不会增加任何延迟。

![图片](https://mmbiz.qpic.cn/mmbiz_png/UPYfEY1kia004V6Yia6OiaMq3zCGKUfMyDRde1jvVgjSZia33Nd227ZCnAWSD6P6qqOicibtaSLupPye0TCQA2CkBu8A/640?wx_fmt=png)

也许结合实际的代码来理解会更好一些。例如，在逆向出来的 Github Copilot 插件代码中，在构建 prompt 时包含了以下的内容：

```
exports.Priorities =
  exports.PromptWishlist =
  exports.PromptElementRanges =
  exports.PromptChoices =
  exports.PromptBackground =
  exports.PromptElementKind =
    undefined;
const M_prompt_parsing_utils_maybe = require("prompt-parsing-utils");
const M_tokenizer_maybe = require("tokenizer");
var i;
!(function (e) {
  e.BeforeCursor = "BeforeCursor";
  e.AfterCursor = "AfterCursor";
  e.SimilarFile = "SimilarFile";
  e.ImportedFile = "ImportedFile";
  e.LanguageMarker = "LanguageMarker";
  e.PathMarker = "PathMarker";
})((i = exports.PromptElementKind || (exports.PromptElementKind = {})));

```

这段代码的主要作用是定义了一种枚举类型，用于表示 GitHub Copilot 系统内部使用的各种提示元素类型，并导入了一些可能与这些提示元素处理相关的模块。它定义了一些名为 `PromptElementKind` 的变量，该变量是一个枚举对象，用于描述不同类型的提示元素。提示元素可能是在编码过程中需要的不同种类的信息，例如光标之前或之后的代码、相似的文件、已导入的文件、语言标记和路径标记。这些提示可能包括从当前文件和其他来源选择的相关代码片段或注释，然后对这些片段和注释进行优先排序、过滤和组装，形成最终的提示。这些提示告诉模型处理哪些数据，以及以什么顺序来对代码进行上下文化。

一个实际的 Copilot 的提示的示例可能是这样的：

```
{
  "prefix": "# Path: codeviz\\\\app.py\\n# Compare this snippet from codeviz\\\\predictions.py:\\n# import json\\n# import sys\\n# import time\\n# from manifest import Manifest\\n# \\n# sys.path.append(__file__ + \\"/..\\")\\n# from common import module_codes, module_deps, module_categories, data_dir, cur_dir\\n# \\n# gold_annots = json.loads(open(data_dir / \\"gold_annotations.js\\").read()",
  "suffix": "if __name__ == '__main__':\\r\\n    app.run(debug=True)",
  "isFimEnabled": true,
  "promptElementRanges": [
    { "kind": "PathMarker", "start": 0, "end": 23 },
    { "kind": "SimilarFile", "start": 23, "end": 2219 },
    { "kind": "BeforeCursor", "start": 2219, "end": 3142 }
  ]
}

```

正如您所见，此提示包括前缀和后缀。然后，Copilot将此提示（经过一些格式化）发送到模型。在这种情况下，Copilot正在以“插入模式”（也称为填写中间（FIM）模式）调用 Codex，因为后缀不为空。

提高语义理解能力
--------

今天，Copilot 正在尝试使用**向量数据库，可以为在私有存储库中或处理专有代码的开发人员创建定制编码体验**。生成式AI编码工具使用称为嵌入的东西从向量数据库中检索信息。

*   **什么是向量数据库？** 它是一个索引高维向量的数据库。
    
*   **什么是高维向量？** 它们是对象的数学表示，因为这些向量可以以多个维度模拟对象，所以它们可以捕捉该对象的复杂性。当适当地用于表示代码片段时，它们可以表示代码的语义甚至意图，而不仅仅是语法。
    
*   **什么是嵌入？** 在编码和LLM的上下文中，嵌入是将代码片段表示为高维向量的方式。由于LLM对编程和自然语言的“知识”，它能够在向量中捕捉代码的语法和语义。
    

**以下是它们如何共同运作的方式：**

*   算法将为存储库中的所有片段（可能是数十亿个）创建嵌入，并将其存储在向量数据库中。
    
*   然后，当您编码时，算法会在IDE中嵌入片段。
    
*   算法随后会在嵌入到IDE片段和已存储在向量数据库中的嵌入之间进行近似匹配，也是实时的。向量数据库是使算法能够快速搜索向量上的近似匹配（而不仅仅是精确匹配），即使它存储了数十亿个嵌入的原因。
    

开发人员熟悉使用哈希码检索数据，这通常会寻找精确的字符匹配，GitHub的高级ML研究员Alireza Goudarzi解释说。“但嵌入——因为它们来自于经过大量数据培训的LLM——会在代码片段和自然语言提示之间建立语义上的接近感。”

阅读以下三个句子，并确定哪两个语义最相似。

*   **句子A**：国王移动并俘获了兵。
    
*   **句子B**：国王在威斯敏斯特大教堂加冕。
    
*   **句子C**：两个白色的战车仍然在比赛中。
    

答案是句子A和C，因为两者都是关于国际象棋的。虽然句子A和B在语法上或结构上相似，因为国王是主语，但它们在语义上是不同的，因为“国王”在不同的上下文中使用。

以下是每个语句如何转换为Python。请注意，尽管它们在语义上不同，但片段A和B之间具有语法上的相似性，而片段A和C之间具有语义上的相似性。

### 片段A：

```
if king.location() == pawn.location():
board.captures_piece(king, pawn)

```

### 片段B：

```
if king.location() == "Westminster Abbey":
king.crown()

```

### 片段C：

```
if len([ r for r in board.pieces("white") if r.type == "rook" ]) == 2:
return True

```

如上所述，Copilot 仍在尝试检索算法，并正在为企业客户设计该功能，特别是那些正在寻找定制编码体验的私有存储库，并明确选择使用该功能。

我们可以进一步结合逆向工程的 copilot 代码讨论这个问题。为了处理大规模的自然语言处理任务， Copilot 在客户端使用了 Cushman + ONNX 模型处理。具体来说，Copilot 将 Cushman 模型的输出转换为向量表示，然后使用向量相似度计算来匹配最相关的本地文件。

除了就地矢量化（Vector）与相似度匹配，Copilot 还使用了本地的相似计算与 token 处理来管理 token，以便更好地处理大规模自然语言处理任务。例如，在 Copilot 逆向工程中出现的可能的代码片段如下：

```
e.prototype.useAutoCorrelation = function (e, t) {
    if (e && !this._isAutoCorrelating) {
      M_correlation_context_manager.CorrelationContextManager.enable(t);
    } else {
      if (!e && this._isAutoCorrelating) {
        M_correlation_context_manager.CorrelationContextManager.disable();
      }
    }
    this._isAutoCorrelating = e;
  };

```

总结与回顾
-----

去年，Copilot 团队对 GitHub Copilot 进行了定量研究，发现使用这个软件的开发者能够以高达 55% 的速度编码。这意味着开发者感到更加高效，能够更快地完成重复性任务，并且能够更专注于令人满意的工作。但是我们的工作不会止步于此。

GitHub 产品和研发团队，包括 GitHub Next，一直在与 Microsoft Azure AI 平台 合作，继续改进 GitHub Copilot 的上下文理解。许多帮助 GitHub Copilot 理解您的代码的工作都是在幕后进行的。当您编写和编辑您的代码时，GitHub Copilot 会实时响应您的写作和编辑，通过生成提示（或者说，基于您在 IDE 中的操作，优先排序并发送相关信息给模型）来不断给出最佳编码建议。

### 了解更多

*   GitHub Copilot X 是对于以 AI 为动力的软件开发的未来设想。发现新内容。
*   了解 支持 GitHub Copilot 的 LLMs 如何变得更加优秀。
*   阅读对应的研究，了解 GitHub Copilot 如何影响开发者的生产力。
    

Copilot 逆向工程相关资料：

*   https://github.com/thakkarparth007/copilot-explorer
*   https://github.com/saschaschramm/github-copilot