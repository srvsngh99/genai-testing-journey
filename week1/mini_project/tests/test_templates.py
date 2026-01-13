from prompt_formatter.templates import PromptTemplate

my_template = PromptTemplate("You are a {role}. Please {task}.")
result = my_template.fill(role="helpful assistant", task="summarize this text")
print(result)