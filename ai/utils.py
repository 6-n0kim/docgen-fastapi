import re
import json

def extract_json_from_response(response_text):
    """LLM 응답에서 JSON 블록을 추출합니다."""
    # 정규 표현식을 사용하여 ```json ... ``` 블록 찾기
    match = re.search(r"```json\n(.*)\n```", response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # ```json이 없는 경우, 가장 큰 JSON 객체/배열 찾기
    match = re.search(r"\{.*\}|\[.*\]", response_text, re.DOTALL)
    if match:
        return match.group(0).strip()
    return None
