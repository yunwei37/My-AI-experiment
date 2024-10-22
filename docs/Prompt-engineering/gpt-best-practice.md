Here's the English translation of the document you provided:

---

# OpenAI's Newly Released GPT Best Practices: Strategies and Tactics for Implementing Large Language Model Applications

In June this year, OpenAI updated its official documentation with an article on strategies and methods to improve the effectiveness of GPT. This article contains six core strategies, some practical prompt cases, and technologies such as knowledge retrieval and code execution to optimize GPT model best practices. By using these best practices, users can better utilize GPT models and improve their effectiveness and performance.

Most of the examples mainly target the GPT-4 model, but they also hold significant reference value for other models.

This article is primarily translated and organized from OpenAI's official documentation, available at: <https://platform.openai.com/docs/guides/gpt-best-practices>

> Some related open-source resource repositories:
>
> - A comprehensive guide, papers, lectures, notebooks, and resources on prompt engineering: <https://github.com/yunwei37/Prompt-Engineering-Guide-zh-CN>
> - Examples and Chinese guides for using the OpenAI API: <https://github.com/yunwei37/openai-cookbook-zh-cn>
> - On security issues of large language models: collections of tools and cases on prompt adversarial attacks and defenses: <https://github.com/yunwei37/prompt-adversarial-collections>
>
> More related reference materials are provided at the end of the article.

## Six Strategies to Improve Results

### Writing Clear Instructions

GPT cannot read your mind. If their output is too lengthy, ask for a concise reply. If their output is too simplistic, request professional-level writing. If you dislike a format, demonstrate the format you want to see. The less GPT has to guess what you want, the greater the likelihood you'll get it.

Strategy:

- Include details in the query to get more relevant answers.
- Ask the model to play a specific role.
- Use delimiters to clearly indicate different parts of the input.
- Specify the steps required to complete the task.
- Provide examples.
- Specify the expected length of the output.
- Provide reference text.

### Providing Reference Text

GPT can confidently fabricate incorrect answers, especially when asked about peculiar topics, citations, and URLs. Just as a note can help students achieve better scores in exams, providing reference text to GPT can help it respond with less fabrication.

Strategy:

- Instruct the model to use reference text for answering.
- Direct the model to respond using citations from the reference text.

### Breaking Down Complex Tasks into Simpler Subtasks

Just as software engineering involves breaking down complex systems into a set of modular components, tasks submitted to GPT should also follow this method. Error rates are generally higher for complex tasks. Moreover, complex tasks can often be redefined as a series of simpler workflow tasks, where the output of early tasks builds the input for subsequent tasks.

Strategy:

- Use intent classification to identify the most relevant instructions from a user query.
- For a conversational application requiring very long interactions, summarize or filter previous dialogues.
- Summarize long documents paragraph by paragraph and build a full summary recursively.

### Giving GPT Enough Time to "Think"

If asked to calculate 17 multiplied by 28, you might not know the answer immediately, but you can work it out given time. Similarly, GPT makes more reasoning errors when it tries to answer questions immediately than when it takes time to think about the answer. Prompting a step-by-step reasoning process before arriving at an answer can help GPT reason more reliably to arrive at the correct answer.

Strategy:

- Instruct the model to work out the solution itself before drawing conclusions.
- Hide the model's reasoning process using internal monologue or a series of queries.
- Ask the model if it missed out on anything in previous queries.

### Using External Tools

Supplement GPT's shortcomings by providing the outputs of other tools. For example, a text retrieval system can provide GPT with relevant document information. A code execution engine can aid GPT in performing mathematical calculations and code executions. If a task can be performed more reliably or efficiently through a tool rather than GPT, offload it for optimal results.

Strategy:

- Use embedding-based search for efficient knowledge retrieval.
- Use code execution for more accurate calculations or calling external APIs.

### Systematically Testing Changes

If you can measure it, improving performance becomes easier. In certain cases, modifications to prompts may result in better performance on isolated examples but poorer overall performance on a more representative gamut of examples. Thus, defining a comprehensive test suite (also known as “evaluation”) may be required to ensure changes have a positive impact on performance.

Strategy:

- Evaluate model outputs against standard reference answers.

## Specific Examples

Each strategy can be implemented through specific tactics. These tactics aim to provide ideas to try. They are by no means exhaustive; feel free to experiment with creative ideas not listed here. The article provides some prompt examples for each concrete strategy and tactic.

### Strategy: Writing Clear Instructions

### **Tactic: Including Details in Queries for More Relevant Responses**

To obtain highly relevant replies, make sure to request any critical details or context. Otherwise, you will leave the model guessing your meaning.

| Poor Instruction | Better Instruction |
| --- | --- |
| How to add numbers in Excel? | How do I sum a row of dollar amounts in Excel? I want to automatically total rows for the entire worksheet, with all totals appearing in a column labeled "Total" on the right side. |
| Who's the president? | Who was the president of Mexico in 2021? How often are elections held? |
| Write code to calculate the Fibonacci sequence. | Write a TypeScript function to calculate the Fibonacci sequence efficiently. Comment the code in detail, explaining the purpose of each part and why it's written that way. |
| Summarize the meeting minutes. | Summarize the meeting minutes in one sentence. Then, list the speakers and their main points in a markdown list. Lastly, list any actions or next steps suggested by the speakers (if any). |

### **Tactic: Asking the Model to Play a Role**

System messages can be used to specify the role the model should play in its responses.

```
USER
Write a thank you note to my bolt supplier, thanking them for delivering on schedule and at short notice. This enabled us to fulfill an important order.

SYSTEM
When I request help writing something, you must include at least one joke or witticism per paragraph.

```

### **Tactic: Using Delimiters to Clearly Mark Different Parts of the Input**

Delimiters like triple quotes, XML tags, or section headings can help mark parts of the text that need to be processed differently.

```
USER
Compose a haiku using the text in the triple quotes.

"""Insert text here"""

```

```
SYSTEM
You’ll receive a pair of essays on the same topic (separated with XML tags). First, summarize each article's argument. Then indicate which article made a better argument and explain why.

USER
<article>Insert the first article here</article>

<article>Insert the second article here</article>

```

```
SYSTEM
You’ll be given a thesis abstract and a proposed title. The paper title should give readers a good idea of the thesis topic while also being attention-grabbing. If the title doesn’t meet these criteria, propose 5 alternatives.

USER
Abstract: Insert the abstract here

Title: Insert the title here

```

For simple tasks like this one, using delimiters might not impact the output quality. However, as tasks become more complex, clarifying task details becomes increasingly important. Don’t make GPTs work hard to understand what exactly you require.

### **Tactic: Specifying the Steps Required to Complete Tasks**

Certain tasks are best specified as a series of steps. Writing these steps explicitly can make them easier for the model to follow.

```
SYSTEM
Respond to user input using the following step-by-step instructions.

Step 1 - The user will provide you text in triple quotes. Prefix "Summary: " and summarize the text in one sentence.

Step 2 - Translate the summary from step 1 into Spanish and prefix with "Translation: ".

```

### **Tactic: Providing Examples**

In general, it is more efficient to provide general instructions applicable to all examples rather than demonstrate every variant of a task using examples. However, in some cases, providing examples might be easier. For example, if you intend the model to mimic a response style that's challenging to describe explicitly. This is known as "few-shot" prompting.

```
SYSTEM
Answer in a consistent style.

USER
Teach me about patience.

ASSISTANT
The river that carves the deepest canyons springs from a humble source; the grandest symphony arises from a solitary note; the most intricate tapestry begins with a single thread.

USER
Teach me about the ocean.

Open in Playground

```

### **Tactic: Specifying the Desired Output Length**

You can request a specific output length from the model. Target output lengths can be specified by word count, sentence count, paragraph count, bullet point count, and so on. However, note that instructing the model to produce a specific number of words is not highly precise. The model is more reliably able to produce outputs with specific numbers of paragraphs or bullet points.

```
USER
Summarize the text divided by triple quotes in approximately 50 words.

"""Insert text here"""

```

```
USER
Summarize the text within triple quotes in 2 paragraphs.

"""Insert text here"""

```

```
USER
Summarize the text using 3 bullet points inside triple quotes.

"""Insert text here"""

```

### Strategy: Providing Reference Text

### **Tactic: Instructing the Model to Answer Questions Using Reference Text**

If we can provide the model with trustworthy information relevant to the current query, we can instruct the model to compose its answers using the provided information.

```
SYSTEM
Use the provided article, delimited by triple quotes, to answer the question. If the answer cannot be found in the article, write "I could not find an answer."
USER
<Insert article, with each article delimited by triple quotes>

Question: <Insert question>

```

Given GPT has a limited context window, in order to apply this strategy, we need some way to dynamically locate information related to the posed question. Embeddings can be used to achieve efficient knowledge retrieval. Please check the strategy "Use embedding-based search to achieve efficient knowledge retrieval" for more details on how to achieve this.

### **Tactic: Instructing the Model to Answer Using Citations from the Reference Text**

If the input has been augmented with relevant knowledge, it's straightforward to instruct the model to add citations from the provided document to its answer. Note that it can also be programmed to verify the citations in the output by string matching within the provided documents.

```
SYSTEM
You’ll receive a document and a question in triple quotes. Your task is to answer using only the provided document and to cite the document paragraphs you used. If the document doesn’t contain the needed information, simply write: "Insufficient information." If the answer to the question is provided, it must be annotated with citations. Use the following format to cite the relevant paragraphs: ({"citation": …}).
USER
"""<Insert document>"""

<Insert question>

```

### Strategy: Breaking Down Complex Tasks into Simpler Subtasks

### **Tactic: Using Intent Classification to Identify the Most Relevant Instructions for a User Query**

For tasks requiring a multitude of independent instruction sets to handle diverse situations, it might be fruitful to first classify the query and use the classification to determine which instructions are needed. This can be achieved by defining fixed categories and hardcoding task-related instructions for the classified types of queries. This process can also be applied recursively to break the task down into a series of stages. This approach has the advantage that only those instructions that are necessary for the next stage of task execution are included with each query, potentially leading to a lower error rate than executing a whole task in one query. It may also result in lower costs, since larger prompts cost more to run (see pricing information).

Suppose for example, for a customer service application, the query might be helpfully classified as follows:

```
SYSTEM
You will receive a customer service query. Classify each query into a primary and secondary category. Provide your output in json format with the primary and secondary keywords.

Primary categories: Billing, Technical Support, Account Management, or General Inquiry.

Billing secondary categories:
- Cancel or Upgrade
- Add Payment Method
- Charge Explanation
- Dispute Charge

Technical Support secondary categories:
- Troubleshoot
- Device Compatibility
- Software Updates

Account Management secondary categories:
- Password Reset
- Update Personal Information
- Account Closure
- Account Security

General Inquiry secondary categories:
- Product Information
- Pricing
- Feedback
- Request to Speak with a Human
USER
I need to get my internet to work again.

```

Based on the classification of the customer query, a more specific set of instructions could be provided to the GPT model to handle the next step. For example, suppose the customer needs help with "Troubleshoot."

```
SYSTEM
You will receive a customer service query that requires troubleshooting in a technical support setting. Assist the user by:

- Confirming that all cables are securely connected to/from the router. Note that cables often become loose over time.
- If all cables are secured and the issue persists, ask which router model they’re using
- Now suggest how they should restart their equipment:
-- If it’s model MTD-327J, suggest pressing the red button and holding it for 5 seconds, then waiting 5 minutes before testing the connection.
-- If it’s model MTD-327S, suggest unplugging and plugging back in, and then waiting 5 minutes before testing the connection.
- If the issue persists even after the device restart and a 5-minute wait, connect them to IT Support by outputting {"IT support requested"}.
- If users start asking questions unrelated to this topic, confirm if they want to end the current troubleshooting chat and categorize their request based on the predefined scheme:

<Insert the above primary/secondary category scheme>
USER
I need to get my internet to work again.

```

Note, the model has been instructed to emit a special string when there is a change in the state of the conversation. This allows us to transform our system into a state machine, where the state determines which instructions are injected. By tracking states, knowing which instructions are relevant in that state, and what state transitions are permitted from that state, we can set up guardrails around the user experience, which can be hard to achieve otherwise using a less structured approach.

### **Tactic: Summarizing or Filtering Previous Dialogue in Conversational Applications with Very Long Conversations**

Due to GPT's fixed context length, conversations between a user and the assistant cannot continue indefinitely if the entire dialogue is included in the context window.

One way to solve this is summarizing the first few rounds of dialogue. Once the input size reaches a predetermined threshold length, it could trigger a query that summarizes part of the dialogue, and a summary of the previous dialogues can be kept in the system message. Alternatively, previous dialogues can be summarized asynchronously throughout the duration of the interaction.

Another solution is to dynamically select the previous parts of the dialogue most relevant to the current query. See the tactic "Utilize embedding-based search to achieve efficient knowledge retrieval."

### **Tactic: Summarizing Long Documents in Stages and Recursively Building a Full Summary**

Given GPT's fixed context lengths, they cannot be used to summarize more than their context length minus the length of the generated summary in a single query.

To summarize a very long document, such as a book, we can use a series of queries to summarize each section of the document. The section summaries can be concatenated and summarized to produce a summary of the summaries. This process can be done recursively until the entire document is summarized. If it is necessary to use information about earlier parts to understand later sections, a useful trick might be including a running summary of the content at the time of summarizing those parts. OpenAI has examined the effectiveness of such a program for summarizing books in previous research, using a variant of GPT-3.

### Strategy: Giving GPT Time to "Think"

### **Tactic: Guiding the Model to Work Out the Solution Before Hastily Drawing Conclusions**

Sometimes, we achieve better results by explicitly instructing the model to engage in reasoning from first principles before drawing conclusions. For example, imagine we want the model to evaluate a student's solution to a math problem. The most straightforward approach is to ask if the student's solution is correct.

```
SYSTEM
Judge if the student's solution is correct.

USER
Problem Statement: I’m building a solar power installation, and I need help calculating the financials.
- Land costs $100 per square foot
- I can buy solar panels for $250 per square foot
- I’ve agreed to pay a fixed annual fee of $100,000 for maintenance, plus $10 per square foot
What's the total cost for the first year of operation, expressed as a function of the area (square feet)?

Student’s Solution: Let x be the area of the installation in square feet.
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000

ASSISTANT
The student’s solution is correct.

```

However, the student's solution is incorrect! We can successfully prompt the model to notice the mistake by first prompting it to generate its own solution.

```
SYSTEM
Solve the problem yourself first, then compare your solution to the student's solution to assess its correctness. Do not judge the student’s solution until you have solved the problem yourself.

USER
Problem Statement: I’m building a solar power installation, and I need help calculating the financials.
- Land costs $100 per square foot
- I can buy solar panels for $250 per square foot
- I’ve agreed to pay a fixed annual fee of $100,000 for maintenance, plus $10 per square foot
What's the total cost for the first year of operation, expressed as a function of the area (square feet)?

Student’s Solution: Let x be the area of the installation in square feet.
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000

ASSISTANT
Let x be the area of the installation in square feet.
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 10x
Total cost: 100x + 250x + 100,000 + 10x = 360x + 100,000

The student’s solution is not correct. They made an error in calculating the maintenance cost, using 100x instead of 10x. The correct total cost for the first year should be 360x + 100,000.

```

### **Tactic: Using Internal Monologue or a Series of Queries to Conceal the Model's Reasoning Process**

The previous tactic demonstrates that models sometimes need to reason out a question in detail before answering a particular question. For certain applications, exposing the reasoning process leading to the final answer may not be suitable for sharing with the user. For instance, in a tutoring application, we may wish to encourage the student to arrive at an answer independently, but the model’s reasoning might reveal the answer to the student.

Internal monologue is a tactic that can be used to address this issue. The idea of internal monologue is to guide the model to format parts of the output intended to be hidden from the user, making it easy to parse. Then, parse the output and present only the visible parts to the user.

```
SYSTEM
Follow the steps below to respond to the user query.

Step 1 - Solve the problem yourself first. Do not rely on the student's solution, which could be wrong. Keep all work for this step inside triple quotes (""").

Step 2 - Compare your solution with the student's and assess if the student's solution is correct. Keep all work for this step inside triple quotes (""").

Step 3 - If the student made a mistake, figure out a hint you can give them without revealing the answer. Keep all work for this step inside triple quotes (""").

Step 4 - If the student made an error, provide the hint to the student from the previous step (outside the triple quotes). Write "Hint:" instead of "Step 4 - ...".

USER
Problem Statement: <Insert problem description>

Student's Solution: <Insert student's solution>

```

Alternatively, this could be achieved through a series of queries, where the outputs of every query except the last one are hidden from the end user.

First, we can have the model solve the problem first.

As this initial query doesn’t require the student's solution, it can be omitted. This provides the additional advantage of eliminating the possibility of the model’s answer being biased by the student’s attempted solution.

```
USER
<Insert problem description>

```

Next, we can have the model assess the correctness of the student's solution using all available information.

```
SYSTEM
Compare your own solution with the student's solution, and assess if the student's solution is correct.

USER
Problem Statement: """<Insert problem description>"""

Your Solution: """<Insert model-generated solution>"""

Student’s Solution: """<Insert student’s solution>"""

```

Finally, we can have the model use its own analysis to construct a helpful tutor's response.

```
SYSTEM
You're a math tutor. If the student made an error, provide a hint without revealing the answer. If the student didn't make errors, provide an encouraging comment.

USER
Problem Statement: """<Insert problem description>"""

Your Solution: """<Insert model-generated solution>"""

Student’s Solution: """<Insert student’s solution>"""

Analysis: """<Insert model-generated analysis from previous step>"""

```

### **Tactic: Asking the Model if It Missed Anything in Previous Queries**

Suppose we are using the model to list excerpts from a source text that are related to a specific question. After listing each excerpt, the model needs to determine whether it should start writing another or should stop. If the source document is large, the model will typically stop too early, failing to list all relevant excerpts. In such cases, better performance can usually be obtained by prompting the model to find what it missed in previous queries using a follow-up query.

```
SYSTEM
You will be given a document in triple quotes. Your task is to select excerpts that are relevant to the following question: "What significant paradigm shifts have occurred in the history of AI?"

Ensure that excerpts contain enough relevant context to explain them—in other words, don't extract small snippets missing important context. Provide your output in the following JSON format:

[{"excerpts": "..."},
...
{"excerpts": "..."}]

USER
"""<Insert document>"""

ASSISTANT
[{"excerpts": "The model writes an excerpt here"},
...
{"excerpts": "The model writes another excerpt here"}]

USER
Are there other relevant excerpts? Note not to duplicate excerpts. And ensure
the new excerpts are indeed relevant to the question and haven't been covered in old ones.

ASSISTANT
[{"excerpts": "The model writes an excerpt here"},
...
{"excerpts": "The model writes another excerpt here"}]

```

Note that if the document is particularly long, this tactic might need to be applied repeatedly.

### Strategy: Using External Tools

### **Tactic: Utilizing Embedding-Based Search to Achieve Efficient Knowledge Retrieval**

The model can leverage external sources of information provided as an input. This can help the model generate more substantiated and up-to-date responses. For instance, if a user asks a specific question about a movie, adding high-quality information about the film (such as cast, director, etc.) to the model’s input might be useful. Embeddings can be used to achieve efficient knowledge retrieval to dynamically add relevant information to the model input at runtime.

Text embeddings are vectors that measure the relevance of text strings to one another. Similar or related strings will be closer to each other than unrelated ones. This fact, combined with the existence of fast vector search algorithms, means embeddings can be used to implement efficient knowledge retrieval. Specifically, a text corpus can be chunked, each chunk embedded, and then stored. Given a query, it can be embedded, and vector search can be performed to identify text chunks most relevant to the query (i.e., closest in embedding space).

An implementation example can be found in the OpenAI Cookbook. Refer to the tactic "Instruct the model to use retrieved knowledge to answer queries" for examples on how to minimize the probability of model-generated factual inaccuracies using knowledge retrieval.

### **Tactic: Using Code Execution for More Accurate Calculations or External API Calls**

We cannot rely on GPT to accurately perform arithmetic or long calculations independently. In needed cases, the model can be guided to write and execute code instead of performing calculations itself. Specifically, the model can be instructed to place code to be executed in a distinct format, such as triple backticks. After generating output, the code can be extracted and executed. Finally, if necessary, the output from the code execution engine (such as a Python interpreter) can be used for the model’s next query input.

```
SYSTEM
You can write and execute Python code by placing it in triple backticks, such as ```code here```. Use this to perform calculations.
USER
Find all the real roots of the following polynomial: 3*x**5 - 5*x**4 - 3*x**3 - 7*x - 10.

```

Another good use of code execution is calling external APIs. If the model is guided on the proper usage of an API, it can write code that uses this API. Guidance can be provided via documentation and/or code examples on how to use the API.

```
SYSTEM
You can write and execute Python code by placing it in triple backticks. Note also, you can use the following module to help the user send messages to a friend:

```python
import

 message
message.write(to="John", message="Hey, want to meetup after work?")

```

Warning: Executing code generated by the model is inherently unsafe and any application wishing to do so should take precautions. Specifically, a sandboxed code execution environment is needed to limit the damage that untrusted code may cause.

### Strategy: Systematically Testing Changes

At times, it is challenging to determine whether a change—for example, a new instruction or a new design—makes your system better or worse. Observing a few examples might suggest which option is better, but it is hard to distinguish a real improvement from chance in small sample sizes. It might be that the change improves performance on some inputs while it degrades performance on others.

Evaluation programs (or "evaluations") are useful for optimizing system design. A good evaluation has the following characteristics:

- Representative of real-world usage (or at least diverse)
- Contains many test cases to achieve greater statistical power (see the table below as a guide)
- Easy to automate or replicate

| Detected Difference | Sample Size Needed for 95% Confidence |
| --- | --- |
| 30% | ~10 |
| 10% | ~100 |
| 3% | ~1,000 |
| 1% | ~10,000 |

Evaluations of outputs can be performed by computers, humans, or a mix of both. Automation of evaluations can use objective criteria (for example, questions with a single correct answer) as well as some subjective or fuzzy criteria where model outputs are evaluated through queries to other models. OpenAI Evals is an open-source software framework that provides tools for creating automated evaluations.

In cases where many equally satisfactory high-quality possible outputs exist (for example, for questions with long answers), model-based evaluation might be useful. The boundary between which functions can be practically evaluated via model-based evaluations and which need human assessment is blurry and is shifting continually as models become increasingly capable. We encourage experimentation to determine how well model-based evaluations work for your use cases.

### **Tactic: Evaluating Model Outputs against Standard Reference Answers**

Suppose the correct answer to a question should refer to a specific set of known facts. Then we can use model queries to compute how many of the necessary facts are included in the candidate answer.

For example, using the following system message:

```
SYSTEM
You will get a piece of text bounded by triple quotes that should be an answer to a question. Check if the following information is directly included in the answer:

- Neil Armstrong was the first person to step on the moon.
- Neil Armstrong stepped on the moon for the first time on July 21, 1969.

For these points, execute the following steps:

1 - Restate the point.
2 - Provide a quote from the answer that is closest to the point.
3 - Consider whether an uninformed reader can infer the point directly after reading the quote. Provide reasoning before making a decision.
4 - Write "yes" if the answer to 3 is affirmative; otherwise, write "no."

Finally, provide a count of the number of "yes" answers. Present this count as {"count": <insert count here>}.

```

Here is an example where both points are satisfied:

```
SYSTEM
<insert system message above>
USER
"""

Neil Armstrong is known for becoming the first person to set foot on the moon. This historic event took place on July 21, 1969, as part of the Apollo 11 mission.

"""

```

Here is an example of an input that fulfills one point:

```
SYSTEM
<insert system message above>
USER
"""

Neil Armstrong made history when he stepped off the lunar module, becoming the first person to walk on the moon.

"""

```

And here's an example of input not fulfilling any of the points:

```
SYSTEM
<insert system message above>
USER
"""

In the summer of '69, a grand journey was made,
Apollo 11 set forth, like a legend’s brazen hand.
Armstrong stepped forth, and history unfurled,
He declared 'one small step,' for a new world's brand.

"""

```

This type of model-based evaluation has many possible variations. Consider the variant below, which tracks the type of overlap between the candidate answer and the gold-standard answer and whether the candidate answer contradicts any part of the gold-standard answer.

```
SYSTEM
Conduct the following steps.

Step 1: Reason through whether the submitted answer compares to the expert answer as: disjoint, subset, superset, or having equal information sets.

Step 2: Reason through whether the submitted answer contradicts any part of the expert answer.

Step 3: Provide a JSON object in the following structure: {"containment": "disjoint" or "subset" or "superset" or "equal", "contradiction": True or False}

```

Here's an example of an input where the answer quality is poor:

```
SYSTEM
<insert system message above>
USER
Question: """What is Neil Armstrong’s most famous event, and when did it happen? Assume UTC time."""

Submitted Answer: """Did he walk around on the moon?"""

Expert Answer: """Neil Armstrong is most known for being the first person to set foot on the moon. This historic event occurred on July 21, 1969, as part of NASA’s Apollo 11 mission. The famous words Armstrong spoke upon stepping on the

lunar surface—'That's one small step for man, one giant leap for mankind'—remain widely quoted to this day. 
"""

```

Here's an example of good quality input and answer:

```
SYSTEM
<insert system message above>
USER
Question: """What is Neil Armstrong’s most famous event, and when did it happen? Assume UTC time."""

Submitted Answer: """Around 02:56 UTC on July 21, 1969, Neil Armstrong became the first person to set foot on the moon's surface, marking a significant achievement in human history. Approximately 20 minutes later, Aldrin joined him. """

Expert Answer: """Neil Armstrong is most known for being the first person to set foot on the moon. This historic event took place on July 21, 1969, as part of the Apollo 11 mission. """

```

## Related Resources

- **OpenAI Official Blog: Prompt Engineering Best Practices with OpenAI API:** A detailed guide on building an AI application, from prompt engineering to vector databases, fine-tuning, etc. <https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api>

This article mainly targets GPT-3 and might be relatively outdated but a good choice for getting started.

- **Microsoft's Concepts and Learning Materials on Building AI Apps:** A detailed guide on building an AI application, from prompt engineering to vector databases, fine-tuning, etc. <https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/advanced-prompt-engineering>

Here are some related open-source resource repositories:

- A comprehensive guide, papers, lectures, notebooks, and resources on prompt engineering: <https://github.com/yunwei37/Prompt-Engineering-Guide-zh-CN>
- Examples and Chinese guides for using the OpenAI API: <https://github.com/yunwei37/openai-cookbook-zh-cn>
- On security issues of large language models: collections of tools and cases on prompt adversarial attacks and defenses: <https://github.com/yunwei37/prompt-adversarial-collections>