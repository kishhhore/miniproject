from ai21 import AI21Client

client = AI21Client(api_key="4eT4o4XUrYxW3mJAoNkriN8ybuDpHZXK")
def answerr_genai(prompt):
    # Call AI21 API to summarize text
    response= client.completion.create(
    model="j2-ultra",
    prompt=prompt,
    num_results=1,
    max_tokens=200,
    temperature=0.1,)
    
    # st = response['completions'][0]['data']['text']
    # st = response['completions'][0]['data']['text']
    st = response.completions[0].data.text
    print(st)
answerr_genai("What is the capital of France?")    
