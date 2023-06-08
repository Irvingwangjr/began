import requests
import json


class ClaudeClient:
    def __init__(self, host='127.0.0.1', port=8088):
        self.url = f'http://{host}:{port}'

    def stream_chat(self, prompt):
        data = {'prompt': prompt}
        response = requests.post(self.url + '/claude/stream_chat', json=data)
        return response

    def reset(self):
        response = requests.post(self.url + '/claude/reset')
        return response.text

    def chat(self, prompt):
        data = {'prompt': prompt}
        response = requests.post(self.url + '/claude/chat', json=data)
        return response.text


if __name__ == '__main__':
    client = ClaudeClient()
    re = client.reset()
    print(re)
