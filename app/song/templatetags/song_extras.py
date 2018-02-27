from django import template

register = template.Library()


# django 문서의 custom template을 참조

def ellipsis_line(value, arg):
    lines = value.splitlines()
    # splitlines를 이용해서 strung을 list로 분할
    if len(lines) > arg:
    # 리스트의 길이가 주어진 arg(line수) 보다 길 경우
        return '\n'.join(lines[:arg] + ['...'])
        # 줄바꿈 문자 단위로
        # multi-line string을 분할한 리스트를
        # arg(line수)개수 까지 슬라이싱한 결과를 합침
        # 마지막 요소에는 '...'을 추가
    return value
    # 리스트의 길이가 주어진 arg보다 짧으면 원본을 그대로 리턴


register.filter('ellipsis_line', ellipsis_line)
