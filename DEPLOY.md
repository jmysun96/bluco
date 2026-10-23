# 배포 — Vercel (공개)

우리 아이 건강수첩은 빌드가 필요 없는 정적 웹앱(PWA)입니다. 누구나 주소로 접속할 수 있고, 휴대폰 홈 화면에 앱처럼 설치할 수 있습니다.

## 구성 파일

| 파일 | 역할 |
|---|---|
| `index.html` | 앱 본체(화면·데이터·계산기 모두 포함) |
| `manifest.webmanifest` | 앱 이름·아이콘·색상 → 홈 화면 설치 |
| `sw.js` | 서비스워커 — 한 번 열면 오프라인에서도 동작 |
| `icons/` | 앱 아이콘 (`python3 scripts/make_icons.py`로 다시 생성) |
| `vercel.json` | 빌드 없이 정적 배포, 보안 헤더, 캐시 설정 |
| `.vercelignore` | 문서·스크립트는 배포에서 제외 |

## Vercel 연결 (처음 한 번)

1. vercel.com → **Add New → Project** → `jmysun96/bluco` **Import**
2. 설정은 그대로 두고 **Deploy** (vercel.json이 정적 배포를 지정)
3. **Settings → Deployment Protection → Vercel Authentication**을 **끄기** (공개 앱이므로)
4. 주소(`https://<프로젝트명>.vercel.app`)를 시크릿 창에서 열어 로그인 없이 보이는지 확인

이후 `main` 브랜치에 커밋하면 자동으로 다시 배포됩니다. 다른 브랜치·PR은 미리보기 주소가 따로 생깁니다.

## 업데이트할 때

- `index.html`을 고친 뒤 `sw.js`의 `VERSION`을 올리면, 이미 설치한 사용자도 다음 접속 때 새 버전을 받습니다.
- 앱은 사용자 정보를 저장하거나 서버로 보내지 않습니다(입력값은 그 화면에서 계산에만 사용).
