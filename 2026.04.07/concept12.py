"""
css파일 연결방법

1) static이라는 폴더 생성
2) static폴더안에 보통 style.css 파일생성
3) 사용하고자 하는 .html 파일에 <title> 아래쪽에
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
4) gpt, gemini등 css파일 작성 연결문 작성 삽입 <-- 프롬포트를 정확히 작성해야함

ex)
result.html에 css 연결하는 링크와 css파일 작성해주고 삽입해줘
범위에 css 연결하는 링크와 css파일 작성해주고 삽입해줘
범위 혹은 파일의 오류의 원인을 알려주고 수정해줘
"""