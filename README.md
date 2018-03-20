# EC2 deploy project

AWS의 EC2배포를 연습하는 프로젝트입니다.
`.secret` 폴더내의 파일로 비밀 키를 관리합니다.


## requirements

- Python  < 3.7
- django > 2.0.3

## Installation

```
pip install -r requirements.txt
```


## Secrets

**`.secrets/base.jason`**

```json
{
    "SECRET_KEY": "<Django settings SECRET_KEY value>"
}
```