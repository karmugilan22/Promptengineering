import tiktoken
def count_tokens(text,model="gpt-4o-mini"):
    encoding=tiktoken.encoding_for_model(model)
    token =encoding.encode(text)
    return len(token)
prompt="expalin me how to learn machcine learning."
token_count=count_tokens(prompt)
print(prompt)
print(f"Number of Token count: {token_count}")