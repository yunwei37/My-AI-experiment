# guidance: 自然语言的编程语言

TLDR:

*微软最近*发布了一个名为 *guidance* 的指导语言,用于控制 *LLM*s 的行为。该语言具有高度的灵活性和可定制性,提供了一种方便且可靠的方法来管理LLMs的相关工作。Guidance 解决了以下的问题：

- 确保生成正确的 YAML 或者 JSON 格式，或者其他任意的格式，同时节约 token 费用
- 相比 langchain 的 Python 代码，用更简单的 DSL，实现多步输出更为复杂和精确的结果

"Guidance"和"LangChain"都是为了帮助用户更有效地利用大型语言模型（Large Language Models, LLMs）而设计的，他们在某些功能性的方面有些类似，但是具体的实现思路、使用体验有很大的不同，Guidance 有点类似于“自然语言编程”的一种表现形式，把精确的 DSL 和模糊的大模型结果结合起来，获取更好的综合表现。

下面是关于这两个项目的一些分析：

### Guidance

"Guidance"是一个用于控制大型语言模型的指导语言。它的主要目标是使用户能够更有效、更高效地控制现代语言模型，而不是通过传统的提示或链式控制【5†source】【6†source】。

它的主要功能包括：

- 提供简单直观的语法，基于Handlebars模板
- 支持多种生成、选择、条件、工具使用等丰富的输出结构
- 支持在Jupyter/VSCode Notebooks中像playground一样进行流式处理
- 提供智能种子生成缓存
- 支持基于角色的聊天模型（例如，ChatGPT）
- 与Hugging Face模型的易于集成，包括指导加速、优化提示边界的令牌治疗，以及使用正则表达式模式指南来强制格式【7†source】。

Guidance 的**用例包含：**

1. **丰富的输出结构：** **`guidance`** 允许在执行过程中交错生成和提示，使得输出结构更加精确，同时也可以生成清晰和可解析的结果。例如，它可以用于识别给定句子是否包含了时代错误（因为时间周期不重叠而不可能的陈述）。使用**`guidance`**，可以通过一个简单的两步提示实现这个任务，其中包含了一个人工制作的思维链条序列**[1](https://github.com/microsoft/guidance)**。
2. **保证有效的语法：** **`guidance`** 可以保证语言模型生成的输出遵循特定的格式，这对于将语言模型的输出用作其他系统的输入非常重要。例如，如果我们想用语言模型生成一个 JSON 对象，我们需要确保输出是有效的 JSON。使用**`guidance`**，我们可以同时加速推理速度并确保生成的 JSON 总是有效的。以下是一个使用**`guidance`**生成具有完美语法的游戏角色配置文件的示例**[1](https://github.com/microsoft/guidance)**。
3. **基于角色的聊天模型：** **`guidance`** 支持通过角色标签自动映射到当前 LLM 的正确令牌或 API 调用的现代聊天式模型，如 ChatGPT 和 Alpaca。README 中提供了是一个展示如何使用基于角色的指导程序实现简单的多步推理和计划的示例**[1](https://github.com/microsoft/guidance)**。

### LangChain

"LangChain"是一个软件开发框架，旨在简化使用大型语言模型（LLMs）创建应用程序的过程。它的用例与语言模型的用例大致相同，包括文档分析和总结、聊天机器人、代码分析等。

"LangChain"的主要功能包括：

**📃 LLM和提示：**

这包括提示管理、提示优化、所有LLM的通用界面以及用于处理LLM的常用工具。

**🔗 链：**

链超越了单个LLM调用，涉及到调用序列（无论是调用LLM还是不同的工具）。LangChain提供了链的标准接口、与其他工具的大量集成以及常见应用的端到端链。

**📚 数据增强生成：**

数据增强生成涉及到特定类型的链，首先与外部数据源进行交互，以获取用于生成步骤的数据。例如，长文本摘要和对特定数据源的问题/回答。

**🤖 代理：**

代理涉及LLM做出决策，选择行动，看到观察结果，并重复该过程直到完成。LangChain为代理提供了标准接口、一组可供选择的代理以及端到端代理的示例。

**🧠 记忆：**

记忆是指在链/代理的调用之间保持状态。LangChain为记忆提供了标准接口、一组记忆实现以及使用记忆的链/代理示例。

**🧐 评估：**

[BETA]生成模型以传统指标难以评估。一种新的评估方法是使用语言模型本身进行评估。LangChain提供了一些提示/链来协助进行此项工作。

### Guidance与LangChain的比较

"Guidance"和"LangChain"都是为了帮助用户更好地使用和控制大型语言模型。两者的主要区别在于它们的关注点和使用场景。

"Guidance"主要关注于如何更有效地控制语言模型的生成过程，提供了一种更自然的方式来组织生成、提示和逻辑控制的流程。这主要适用于需要在一个连续的流程中交替使用生成、提示和逻辑控制的场景，例如，基于聊天的应用或者需要生成有特定结构的文本的应用。

"LangChain"则是一个更全面的框架，它提供了一套完整的工具和接口，用于开发和部署基于大型语言模型的应用。它包括了从数据获取、处理，到模型调用，再到结果呈现的一整套流程。所以，如果你想要开发一个完整的基于语言模型的应用，"LangChain"可能是一个更好的选择。

所以，这两个项目的相关性在于它们都是服务于大型语言模型的，但是它们的侧重点和应用场景是不同的。具体使用哪一个，主要取决于你的具体需求和使用场景。

### Guidance example JSON

生成精确的 JSON 结果：

```jsx
# we use LLaMA here, but any GPT-style model will do
llama = guidance.llms.Transformers("your_path/llama-7b", device=0)

# we can pre-define valid option sets
valid_weapons = ["sword", "axe", "mace", "spear", "bow", "crossbow"]

# define the prompt
character_maker = guidance("""The following is a character profile for an RPG game in JSON format.
```json
{
    "id": "{{id}}",
    "description": "{{description}}",
    "name": "{{gen 'name'}}",
    "age": {{gen 'age' pattern='[0-9]+' stop=','}},
    "armor": "{{#select 'armor'}}leather{{or}}chainmail{{or}}plate{{/select}}",
    "weapon": "{{select 'weapon' options=valid_weapons}}",
    "class": "{{gen 'class'}}",
    "mantra": "{{gen 'mantra' temperature=0.7}}",
    "strength": {{gen 'strength' pattern='[0-9]+' stop=','}},
    "items": [{{#geneach 'items' num_iterations=5 join=', '}}"{{gen 'this' temperature=0.7}}"{{/geneach}}]
}```""")

# generate a character
character_maker(
    id="e1f491f7-7ab8-4dac-8c20-c92b5e7d883d",
    description="A quick and nimble fighter.",
    valid_weapons=valid_weapons, llm=llama
)
```

- 能保证 JSON 不会出错
- 能节约大量的 token 费用，生成时间和价格大约都只有原先直接生成 YAML 的一半

使用 LLaMA 2B 时，上述提示通常需要 5.6000 秒多一点即可在 A7 GPU 上完成。如果我们要运行适合为单次调用的相同提示（今天的标准做法），则需要大约 5 秒才能完成（其中 4 秒是令牌生成，1 秒是提示处理）。*这意味着指导加速比此提示的标准方法提高了 2 倍。*实际上，确切的加速系数取决于特定提示的格式和模型的大小（模型越大，受益越大）。目前也仅支持 transformer LLM的加速。

注意，这种格式控制不仅对于 jSON 有效，对于任意的其他语言或者格式，例如 YAML 等都是有效的，对于开发复杂应用或者生成 DSL 来说，会有很大的帮助。

一个更复杂的例子，同时也包含使用 **`{{#select}}...{{or}}...{{/select}}`** 命令进行控制流的选择：

```
import guidance

# set the default language model used to execute guidance programs
guidance.llm = guidance.llms.OpenAI("text-davinci-003")

# define the few shot examples
examples = [
    {'input': 'I wrote about shakespeare',
    'entities': [{'entity': 'I', 'time': 'present'}, {'entity': 'Shakespeare', 'time': '16th century'}],
    'reasoning': 'I can write about Shakespeare because he lived in the past with respect to me.',
    'answer': 'No'},
    {'input': 'Shakespeare wrote about me',
    'entities': [{'entity': 'Shakespeare', 'time': '16th century'}, {'entity': 'I', 'time': 'present'}],
    'reasoning': 'Shakespeare cannot have written about me, because he died before I was born',
    'answer': 'Yes'}
]

# define the guidance program
structure_program = guidance(
'''Given a sentence tell me whether it contains an anachronism (i.e. whether it could have happened or not based on the time periods associated with the entities).
----

{{~! display the few-shot examples ~}}
{{~#each examples}}
Sentence: {{this.input}}
Entities and dates:{{#each this.entities}}
{{this.entity}}: {{this.time}}{{/each}}
Reasoning: {{this.reasoning}}
Anachronism: {{this.answer}}
---
{{~/each}}

{{~! place the real question at the end }}
Sentence: {{input}}
Entities and dates:
{{gen "entities"}}
Reasoning:{{gen "reasoning"}}
Anachronism:{{#select "answer"}} Yes{{or}} No{{/select}}''')

# execute the program
out = structure_program(
    examples=examples,
    input='The T-rex bit my dog'
)
```

这段代码的主要目标是定义和执行一个使用 guidance 的程序，该程序处理一个指定问题：给出一个句子，告诉我这个句子是否包含了一个时间错误（即基于与实体相关联的时间周期，这件事是否可能发生）。

首先，通过 `import guidance` 语句导入 guidance 库。

然后，设定了默认使用的大型语言模型（LLM）`guidance.llm = guidance.llms.OpenAI("text-davinci-003")`。在这种情况下，使用的是 OpenAI 的 "text-davinci-003" 模型。

定义了一组“少量示例”（few-shot examples），这些示例展示了模型如何处理该问题。每个示例都包含一个句子（`input`），句子中涉及的实体及其时间信息（`entities`），推理（`reasoning`）以及是否存在时间错误的答案（`answer`）。

之后，定义了一个 guidance 程序（`structure_program`）。这个程序首先展示了少量示例，然后处理一个实际的问题。引导程序使用 Handlebars 模板语法来编写。例如，使用 `{{#each examples}}` 和 `{{~/each}}` 可以遍历所有示例。此外，还使用了 `{{gen}}` 命令来生成文本，并使用 `{{#select}}` 和 `{{/select}}` 命令来做出选择。

最后，执行这个程序。作为输入，提供了少量示例（`examples`）和一个实际问题（`input`）。执行的结果（`out`）是一个执行程序对象，可以进一步处理或分析。

整体上，这个例子展示了如何使用 guidance 库来处理一个特定问题。这个库使得对大型语言模型的控制更为高效和有效，不仅可以生成文本，还可以做出逻辑决策。

### Guidance 的原理

**`guidance`**是一个用于控制大型语言模型（LLMs，例如 GPT-3 或 GPT-4）的库。它的设计初衷是使语言模型的控制更为高效和有效。这是通过编写引导程序（guidance programs）实现的，这些程序允许你将文本生成、提示以及逻辑控制交织在一起，形成一个与语言模型处理文本的方式相匹配的连续流程**[1](https://github.com/microsoft/guidance)**。

引导程序基于Handlebars模板语言的简单、直观语法，但具有一些独特的功能。它们有一个与语言模型处理令牌顺序直接对应的独特线性执行顺序。这意味着在执行过程中的任何时刻，都可以使用语言模型来生成文本（使用**`{{gen}}`**命令）或进行逻辑控制流决策（使用**`{{#select}}...{{or}}...{{/select}}`**命令）。生成和提示的交织可以使输出结构更精确，从而提高准确性，同时也产生清晰、可解析的结果**[1](https://github.com/microsoft/guidance)**。

`guidance`通过一个令牌备份模型，然后允许模型向前移动，同时限制它仅生成前缀与最后一个令牌匹配的令牌，从而消除这些偏差。这种“令牌修复”过程消除了令牌边界偏差，并允许自然地完成任何提示。

### 参考资料

<https://github.com/microsoft/guidance>


> 了解更多请访问 <https://yunwei37.github.io/My-AI-experiment/> 或者 Github： <https://github.com/yunwei37/My-AI-experiment>
