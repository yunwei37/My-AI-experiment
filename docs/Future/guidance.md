# Guidance: A Programming Language for Natural Language

TLDR:

*Recently, Microsoft* released a guiding language called *Guidance* designed to control the behavior of *LLMs* (Large Language Models). This language offers high flexibility and customization, providing a convenient and reliable way to manage tasks related to LLMs. Guidance addresses the following issues:

- Ensures the generation of correct YAML or JSON formats, or any other arbitrary formats, while saving on token costs
- Allows for simpler DSL compared to Python code in LangChain to achieve more complex and precise results through multi-step outputs

"Guidance" and "LangChain" are both designed to help users effectively utilize Large Language Models (LLMs). They share some functional similarities, but their implementation ideas and user experiences differ significantly. Guidance resembles a form of "natural language programming," combining precise DSL with the output from large models for a holistic performance.

Here is an analysis of these two projects:

### Guidance

"Guidance" is a guiding language for controlling large language models. Its main goal is to allow users to control modern language models more efficiently and effectively, rather than through traditional prompts or chain-based controls.

Its main features include:

- Provides a simple and intuitive syntax based on Handlebars templates
- Supports a rich variety of generation, selection, conditional, and tool usage output structures
- Allows streaming processing in Jupyter/VSCode Notebooks like a playground
- Offers intelligent seed generation caching
- Supports role-based chat models (e.g., ChatGPT)
- Easy integration with Hugging Face models, including guidance acceleration, token treatment for optimized prompt boundary, and using regex pattern guidelines to enforce formatting

Guidance use cases include:

1. **Rich Output Structures:** **`Guidance`** allows interleaving of generation and prompting during execution, making output structures more precise while generating clear and parsable results. For example, it can identify whether a given sentence contains an anachronism (a statement that is impossible due to non-overlapping time periods). Using **`guidance`**, this task can be achieved through a simple two-step prompt that includes a hand-crafted chain of thought sequence.
2. **Ensuring Effective Syntax:** **`Guidance`** can ensure that the output generated by language models adheres to a specific format, which is crucial when using the output of a language model as input for other systems. For instance, if we want the language model to generate a JSON object, we need to ensure that the output is valid JSON. With **`guidance`**, we can accelerate inference speed and ensure the generated JSON is always valid. Here’s an example of using **`guidance`** to produce a game character profile with perfect syntax.
3. **Role-based Chat Models:** **`Guidance`** supports modern chat models like ChatGPT and Alpaca by automatically mapping role labels to the correct tokens or API calls of the current LLM. The README provides an example of using role-based guidance to achieve simple multi-step reasoning and planning.

### LangChain

"LangChain" is a software development framework designed to simplify the process of creating applications using large language models (LLMs). Its use cases largely align with those of language models, including document analysis and summarization, chatbots, code analysis, etc.

LangChain's main features include:

**📃 LLM and Prompt:**

This includes prompt management, prompt optimization, a universal interface for all LLMs, and common tools for handling LLMs.

**🔗 Chains:**

Chains go beyond a single LLM invocation and involve sequences of calls (whether invoking LLMs or different tools). LangChain provides standard interfaces for chains, extensive integration with other tools, and end-to-end chains for common applications.

**📚 Data Augmented Generation:**

Data augmented generation involves a specific type of chain that first interacts with external data sources to gather data for the generation step. Examples include summarizing long texts and answering questions based on specific data sources.

**🤖 Agents:**

Agents involve LLMs making decisions, selecting actions, observing results, and repeating the process until completion. LangChain provides standard interfaces for agents, a set of agents to choose from, and end-to-end examples of agents.

**🧠 Memory:**

Memory refers to maintaining the state between calls of chains/agents. LangChain offers standard interfaces for memory, a set of memory implementations, and examples of chains/agents that use memory.

**🧐 Evaluation:**

[BETA] Generative models are challenging to evaluate with traditional metrics. A novel evaluation method is to use the language model itself for evaluation. LangChain provides some prompts/chains to assist with this task.

### Comparison of Guidance and LangChain

"Guidance" and "LangChain" both aim to enhance the use and control of large language models. The primary difference lies in their focus and usage scenarios.

"Guidance" focuses on more effectively controlling the generation process of language models, providing a more natural way to organize the flows of generation, prompting, and logical control. This is mainly suitable for scenarios where generation, prompting, and logical control are interleaved in a continuous process, such as chat-based applications or applications requiring text with specific structure.

"LangChain," on the other hand, is a more comprehensive framework that offers a complete set of tools and interfaces for developing and deploying applications based on large language models. It includes the whole process from data acquisition, processing, model invocation, to result presentation. So, if you aim to develop a complete application based on language models, "LangChain" might be a better choice.

Thus, while these two projects relate to large language models, their focus and application scenarios differ. The choice depends on your specific needs and usage scenarios.

### Guidance Example JSON

Generating precise JSON results:

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

- Ensures the JSON is error-free
- Saves a significant amount of token cost, making generation time and price about half of directly generating YAML

Using LLaMA 2B, the above prompt usually takes a bit more than 5.6 seconds to complete on an A7 GPU. If we were to run the same prompt suitable for a single invocation (the standard practice today), it would take about 5 seconds to complete (4 seconds for token generation, 1 second for prompt processing). *This means the guidance acceleration results in a 2x speedup over the standard approach for this prompt.* The exact speedup factor depends on the specific prompt format and model size (the larger the model, the greater the benefit). Currently, acceleration is only supported for transformer LLMs.

Note, this formatting control is effective for not just JSON, but for any other languages or formats such as YAML. It can be greatly beneficial for developing complex applications or generating DSL.

A more complex example, which also involves using the **`{{#select}}...{{or}}...{{/select}}`** command for control flow selection:

```python
import guidance

# set the default language model used to execute guidance programs
guidance.llm = guidance.llms.OpenAI("text-davinci-003")

# define the few-shot examples
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

This code aims to define and execute a program using guidance that tackles a specific problem: Given a sentence, tell me whether it contains an anachronism (i.e., whether it could have happened based on the time periods associated with the entities).

Firstly, the `import guidance` statement imports the guidance library.

Then, it sets the default Large Language Model (LLM) used, `guidance.llm = guidance.llms.OpenAI("text-davinci-003")`. In this case, it uses OpenAI's "text-davinci-003" model.

A set of "few-shot examples" are defined, showing how the model handles the problem. Each example consists of a sentence (`input`), the entities involved and their time information (`entities`), the reasoning (`reasoning`), and whether an anachronism is present (`answer`).

Next, a guidance program (`structure_program`) is defined. This program first displays the few-shot examples and then tackles a real question. The guidance program uses Handlebars template syntax for scripting. For example, `{{#each examples}}` and `{{~/each}}` iterate over the examples. The `{{gen}}` command is used to generate text, and the `{{#select}}` and `{{/select}}` commands are used for making selections.

Finally, the program is executed. The input includes the few-shot examples (`examples`) and a real problem (`input`). The execution result (`out`) is an executed program object that can be further processed or analyzed.

Overall, this example shows how to use the guidance library to address a specific problem. The library makes controlling large language models more efficient and effective, allowing not only for text generation but logical decision-making as well.

### Principles of Guidance

**`Guidance`** is a library for controlling Large Language Models (LLMs) like GPT-3 or GPT-4. It is designed to make controlling language models more efficient and effective. This is achieved through writing guidance programs that allow you to interleave text generation, prompting, and logic control into a continuous flow that matches how language models process text.

Guidance programs use simple and intuitive syntax based on the Handlebars template language but have some unique features. They have a unique linear execution order that directly corresponds to the token sequence handled by the language model. This means at any point during execution, the language model can be used to generate text (using the **`{{gen}}`** command) or to make logic control flow decisions (using the **`{{#select}}...{{or}}...{{/select}}`** command). The interleaving of generation and prompting can make the output structure more precise, improving accuracy while also producing clear and parsable results.

Guidance employs a token backup model and allows the model to move forward while restricting it to generate tokens that only match the prefix of the last token, thus eliminating these biases. This "token fixing" process eliminates token boundary bias and allows any prompt to be naturally completed.

> For more interesting AI experiments and insights, please visit my AI experiment and throughts website <https://yunwei37.github.io/My-AI-experiment/> and github repo: <https://github.com/yunwei37/My-AI-experiment>
