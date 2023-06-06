import requests

class ClaudeClient:
    def __init__(self, host='127.0.0.1', port=8088):
        self.url = f'http://{host}:{port}'

    def stream_chat(self, prompt):
        data = {'prompt': prompt}
        response = requests.post(self.url + '/claude/stream_chat', json=data)
        print(response.text)

    def reset(self):
        requests.post(self.url + '/claude/reset')

    def chat(self, prompt):
        data = {'prompt': prompt}
        response = requests.post(self.url + '/claude/chat', json=data)
        print(response.text)

if __name__ == '__main__':
    client = ClaudeClient()
    client.stream_chat('给我关于c语言的介绍')
    client.reset()
    client.chat('周末有什么好玩的?')