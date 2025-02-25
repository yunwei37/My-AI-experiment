from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI

# Uncomment the following line to use an example of a custom tool
# from paper_discussion.tools.custom_tool import MyCustomTool
from crewai_tools import FileReadTool
from crewai_tools import TXTSearchTool, PDFSearchTool

# Initialize the tool to read any files the agents knows or lean the path for
# file_read_tool = FileReadTool(txt="/workspaces/knowledgeCache/paper/pdf_downloads/AutoRAID.txt")
file_read_tool = FileReadTool()
search_tool = TXTSearchTool()

# Initialize the tool to search within any text file's content the agent learns about during its execution
# search_tool = TXTSearchTool(txt="/workspaces/knowledgeCache/paper/pdf_downloads/AutoRAID.txt")
# search_tool = PDFSearchTool(pdf='/workspaces/knowledgeCache/paper/pdf_downloads/AutoRAID.pdf')
# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# @CrewBase
# class PaperSummaryCrew():
# 	"""PaperSummary crew"""

# 	@agent
# 	def professor(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['professor'],
# 			tools=[file_read_tool, search_tool],
# 			allow_delegation=True,
# 			verbose=True
# 		)

# 	@task
# 	def summary_task(self) -> Task:
# 		return Task(
# 			config=self.tasks_config['summary_task'],
# 			output_file='results/summary.md'
# 		)

@CrewBase
class PaperDiscussionCrew():
	"""PaperDiscussion crew"""

	@agent
	def professor(self) -> Agent:
		return Agent(
			config=self.agents_config['professor'],
			tools=[file_read_tool, search_tool],
			allow_delegation=True,
			verbose=True
		)

	@agent
	def student1(self) -> Agent:
		return Agent(
			tools=[search_tool],
			config=self.agents_config['student1'],
			allow_delegation=True,
			verbose=True
		)
	
	@agent
	def student2(self) -> Agent:
		return Agent(
			tools=[search_tool],
			config=self.agents_config['student2'],
			allow_delegation=True,
			verbose=True
		)

	@agent
	def student3(self) -> Agent:
		return Agent(
			tools=[search_tool],
			config=self.agents_config['student3'],
			allow_delegation=True,
			verbose=True
		)

	@agent
	def student4(self) -> Agent:
		return Agent(
			tools=[search_tool],
			config=self.agents_config['student4'],
			allow_delegation=True,
			verbose=True
		)

	# @task
	# def summary_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['summary_task'],
	# 		output_file='results/summary.md'
	# 	)

	# @task
	# def key_sentences_task(self) -> Task:
	# 	return Task(
	# 		context=[self.summary_task()],
	# 		config=self.tasks_config['key_sentences_task'],
	# 		output_file='results/key_sentences.md'
	# 	)

	@task
	def discussion_task(self) -> Task:
		return Task(
			context=[],
			config=self.tasks_config['discussion_task'],
			output_file='results/discussion.md'
		)

	@task
	def answer_task1(self) -> Task:
		return Task(
			context=[self.discussion_task()],
			agent=self.student1(),
			config=self.tasks_config['answer_task'],
			output_file='results/answers1.md',
		)

	@task
	def answer_task2(self) -> Task:
		return Task(
			context=[self.discussion_task()],
			agent=self.student2(),
			config=self.tasks_config['answer_task'],
			output_file='results/answers2.md',
		)
	
	@task
	def answer_task3(self) -> Task:
		return Task(
			context=[self.discussion_task()],
			agent=self.student3(),
			config=self.tasks_config['answer_task'],
			output_file='results/answers3.md',
		)
	
	@task
	def answer_task4(self) -> Task:
		return Task(
			context=[self.discussion_task()],
			agent=self.student4(),
			config=self.tasks_config['answer_task'],
			output_file='results/answers4.md',
		)

	@task
	def new_question_task1(self) -> Task:
		return Task(
			context=[self.answer_task1(), self.answer_task4()],
			agent=self.student1(),
			config=self.tasks_config['new_question_task'],
			output_file='results/new_question_task1.md',
		)

	@task
	def new_question_task2(self) -> Task:
		return Task(
			context=[self.answer_task2(), self.answer_task3()],
			agent=self.student2(),
			config=self.tasks_config['new_question_task'],
			output_file='results/new_question_task2.md',
		)
	
	@task
	def new_question_task3(self) -> Task:
		return Task(
			context=[self.answer_task3(), self.answer_task2()],
			agent=self.student3(),
			config=self.tasks_config['new_question_task'],
			output_file='results/new_question_task3.md',
		)
	
	@task
	def new_question_task4(self) -> Task:
		return Task(
			context=[self.answer_task4(), self.answer_task1()],
			agent=self.student4(),
			config=self.tasks_config['new_question_task'],
			output_file='results/new_question_task4.md',
		)
	
	@task
	def conclusion_task(self) -> Task:
		return Task(
			context=[self.answer_task1(), self.answer_task2(), self.answer_task3(), self.answer_task4()],
			config=self.tasks_config['conclusion_task'],
			output_file='results/conclusion.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PaperDiscussion crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
			# manager_llm=ChatOpenAI(model="gpt-4o"),
			planning=True,
			planning_llm=ChatOpenAI(model="gpt-4o"),
			memory=True,
			output_log_file='log.txt',
			full_output=True
		)
