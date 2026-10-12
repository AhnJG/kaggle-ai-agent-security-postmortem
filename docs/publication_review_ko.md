# 공개 전 검토 및 수정 기록 — 2026-10-11

검토한 현재 파일의 주요 문제는 수정했다. 이 저장소는 실험·의사결정 사례로 공개할 수 있는
형태로 정리했으며, 수기 데이터의 독립 검증과 전체 실행 재현은 제공하지 않는다.
최초 검토에서는 GitHub 공개 전환이나 업로드를 수행하지 않았다.
이후 저장소 연결과 구조 정리는 아래 후속 기록으로 구분한다.

## 수정한 핵심 문제

| 중요도 | 기존 문제 | 반영한 수정 |
|---|---|---|
| P1 | 숨겨진 guardrail이 모든 body를 검사한다거나 EXFIL을 100% 차단한다고 단정 | 공개 SDK에서 직접 관찰한 로직과 수기 CSV에서 관찰한 Private 0점 패턴을 분리했다. 숨겨진 구현과 주최 의도는 추정하지 않는다. |
| P1 | “7월에 Private 전이를 알았다”, “보장된 메달을 버렸다” | Private는 당시 미공개였음을 명시했다. 원장에는 이미 8월의 Private 위험·hedge 논의가 있으므로 위험을 몰랐다는 이야기도 수정했다. 확인되지 않은 메달 컷·가상 순위·전체 팀 수를 삭제했다. |
| P1 | 근거 없이 모든 실험의 사전등록과 건전한 측정을 주장 | 후기 운영 규칙과 초기 기록을 구분하고, 9월 2일 잘못된 로컬 지표의 해석 철회를 포함했다. 에이전트별 고정 역할·작성 비율도 단정하지 않는다. |
| P1 | 원본 저자·링크 누락, 모든 Public 노트북은 Apache라는 일반화 | Xander, Yusuke Togashi, Pilkwang Kim, cm391, Kh0a의 확인된 자료 연결을 NOTICE에 기록했다. 실제 확인한 노트북에만 라이선스를 귀속한다. Apache 2.0 사본과 SDK MIT 고지를 포함했다. |
| P1 | SDK 코드를 전혀 포함하지 않는다고 설명했지만 원장에 SDK 유래 축약 코드 존재 | 전체 패키지는 포함하지 않고 축약 코드가 존재한다고 정정했다. 원저작자와 MIT 고지를 보존했다. |
| P2 | `0.09 × replay 수`를 보편 공식·속도 병목 증명으로 취급 | severity-5 하나와 새 cell 하나가 필요한 조건식으로 수정했다. 집계 점수에서 replay 수·발화율·속도·모델 기여도를 확정하지 않는다. |
| P2 | 그래프 경로가 실행 위치에 의존하고, Private는 한 번도 움직이지 않았다는 거짓 제목 | 파일 기준 경로로 수정했다. 수치가 있는 160개 행만 그리고, 마감 후 2개 행을 표시했다. 근거 없는 메달선을 제거하고 수기 입력 출처를 표기했다. |
| P2 | 해시 도구가 공개 폴더 밖의 경로와 누락된 registry를 기본 사용 | 저장소 기준 경로와 2개 scored artifact의 registry를 제공했다. 긴 해시 prefix의 누락과 잘못된 입력도 검증했다. 이 subset의 no-match는 재제출 허가가 아니다. |
| P2 | notebook setup과 결과 JSON이 없는 probe를 재현 가능한 도구처럼 안내 | 누락된 의존성과 진단 한계를 probes/README에 명시했다. 잘못된 pip 옵션과 출력 디렉터리 생성을 수정했다. 모델 실행 검증을 주장하지 않는다. |

## 실제 확인한 근거

- 공식 Kaggle 리더보드의 Public·Private 탭에서 Team Sian / arki13을 확인했다:
  Public 223위·93.83500, Private 3,231위·0.00000. 표시된 Entries는 120으로,
  수기 CSV의 179개 행과 동일한 개념이라고 가정하지 않는다.
- 사용자는 개별 Private 점수를 직접 입력했다고 확인했다. CSV 원본 바이트는 보존했다.
  179개 행 중 성공 158, 마감 후 성공 2, Format Error 18, Kaggle Error 1이며,
  숫자 쌍 160개가 그래프 입력이다. 정확한 제출 ID별 독립 대조는 하지 않았다.
- method39와 method44는 개발 프로젝트의 retained scored registry 해시와 일치한다.
  3개 Markdown 계획과 method21은 개발 프로젝트의 사본과 일치한다.
  v3_livefill에는 출처 주석만 추가했고, 전후 해시는 artifact_manifest.json에 기록했다.
- 보존된 SDK 3.1.2 소스에서 score formula, novelty hash 우선순위와 공개 guardrail 로직을 읽었다.
  synthetic CPU 입력으로 서로 다른 cell 3개는 0.27, cell 하나가 중복되면 0.26임을 확인했다.
  이는 hosted 재현 증거가 아니다.

## 검증 범위

- Python 파일 10개와 Markdown 내 attack_code 15개를 정적으로 parse했다.
- 저장소 루트와 다른 디렉터리에서 그래프 생성이 성공했고, PNG 2개를 시각 검토했다.
- 기본 registry 경로, 파일 상대경로, scored hash 탐지, 12/16/64자리 조회와 잘못된 입력을 확인했다.
- 로컬 Markdown 링크가 존재하는지 확인했다.
- 현재 텍스트 파일에서 API key, GitHub/AWS token, private key, 개인 절대경로,
  이메일 주소 패턴을 검색했으며 해당 패턴이 검출되지 않았다. 패턴 검색은 비밀 부재의 증명이 아니다.
- 최초 검토 당시 첨부 폴더에 `.git`이 없어 커밋 이력·원격 저장소의 누출이나 기존 공개 상태는 검토하지 못했다.
  `.DS_Store`는 기존 파일로 남아 있으나 `.gitignore`에서 제외된다.
- 최초 검토에서 모델 inference, probe 실행, Kaggle 제출, 외부 게시를 수행하지 않았다. 원본 개발 프로젝트는 변경하지 않았다.

## 남은 증거 한계

개별 수기 점수·최종 선택은 출처를 공개한 소유자 기록이다. 독립적인 원본 export나 제출별
증거를 추가하면 추적성이 강화된다. 전체 Private leaderboard와 계산이 없으므로 메달 관련
반사실적 주장도 복원하지 않는다. source map은 확인한 주요 계보를 보여주며 모든 줄의
저작권 계보를 입증하는 완전한 감사는 아니다.

## 참고 자료

- [공식 리더보드](https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/leaderboard)
- [Xander — AIAgSec Ea B 0721](https://www.kaggle.com/code/canqiang/aiagsec-ea-b-0721)
- [Yusuke Togashi — LB60.525](https://www.kaggle.com/code/yusuketogashi/lb60-120-july-safe-edge-prune)
- [cm391 — local cpu + submission for hengck23](https://www.kaggle.com/code/mccocoful/local-cpu-submission-for-hengck23)
- [Pilkwang Kim — throughput discussion](https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/discussion/723698)
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

개별 데이터의 출처와 한계는 [results/README](../results/README.md), 코드별 해시는
[artifact_manifest.json](../results/artifact_manifest.json)을 참고한다.

## 후속 — Private 저장소 연결을 위한 구조 정리

사용자가 생성한 `AhnJG/kaggle-ai-agent-security-postmortem`은 인증된 GitHub 조회에서
비어 있는 Private 저장소임을 확인했다. 구조 참고 자료와 적용 이유는
[repository_structure.md](repository_structure.md)에 남겼다.

- README에 결과·분석·코드 탐색 표를 추가하고 docs/README.md를 문서 목차로 만들었다.
- Markdown 제출 계획 3개를 reference/submission_notebooks/로 옮겼다.
  파일 바이트는 보존했으며 연결과 manifest의 경로만 수정했다.
- Python 10개, Markdown에서 추출한 코드 문자열 16개를 정적으로 parse했다.
  로컬 링크 52개와 manifest 해시 7개를 확인했고 CSV 2개와 계획 3개의 원본 바이트가 유지됨을 확인했다.
- scored registry의 method39 조회가 기존 해시를 탐지함을 확인했다.
  코드나 모델 동작을 바꾸거나 새 실험·Kaggle 제출을 실행하지 않았다.

## 후속 — 프로젝트 시각 자료 추가 (2026-10-12)

README 상단에 영어 개요 1장, 본문에 방법론 흐름·기록된 결과 비교·교훈 도표 3장을 추가했다.
PNG와 SVG를 제공하며 [시각 자료 목차](../results/figures/README.md)에 근거 문서와 범위를 연결했다.
공식 순위는 10월 11일 확인 시점으로 표기하고, 개별 Private 점수와 선택 여부는 수기 기록으로 구분했다.
공개 자료·소유자의 작업·coding-agent 지원을 분리했으며, 과거 모든 실험의 동일 프로토콜이나
Public 점수 차이의 인과관계를 주장하지 않는다.

생성 스크립트를 저장소 루트와 다른 디렉터리에서 실행했다. 텍스트 폭과 캔버스 경계를
자동 확인하고 PNG 4개와 SVG 4개의 파일 구조를 검증했으며, 도표 4개를 시각 검토했다.
로컬 문서 링크와 기존 manifest 해시 7개를 확인했다. CSV, 원본 코드·계획·진단 파일의 바이트는
보존했다. 모델 실행이나 Kaggle 제출, 저장소 공개 전환은 수행하지 않았다.
