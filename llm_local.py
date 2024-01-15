import requests
import json

class LLM_local:
    def __init__(self, url, content_type, temperature=0.7, max_token=-1, stream=False):
        self.url = url
        self.content_type = content_type
        self.temperature = temperature
        self.max_token = max_token
        self.stream = stream

    def get_response(self, messages):
        #construct the payload
        headers = self.get_headers()
        data = self.get_data(messages)

        #ask local llm activated by LM Studio
        response = requests.post(self.url, headers=headers, data=json.dumps(data))

        #extract the answer
        llm_answer = response.json()#["choices"][0]["message"]["content"]

        return llm_answer
    
    def get_data(self, messages):
        data = {
            "messages": messages,
            "temperature": self.temperature,
            "max_tokens": self.max_token,
            "stream": self.stream
        }

        return data

    def get_headers(self):
        headers = {
            "Content-Type": self.content_type
        }

        return headers
    
if __name__ == "__main__":
    #test compatible avec LM_studio
    #init
    url = "http://localhost:1234/v1/chat/completions"
    content_type = "application/json" 
    llm = LLM_local(url, content_type)

    #call llm
    system_content = "You are a usefull assistant"
    user_content = "What is order 66"
    messages = [
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ]
    response = llm.get_response(messages)

    import pprint
    pprint.pprint(response)

    response_content = response["choices"][0]["message"]["content"]
    print(f"\n{response_content = }")