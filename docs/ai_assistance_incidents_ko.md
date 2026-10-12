# AI 활용 오류·정정의 상세 기록

[반성문으로 돌아가기](ai_assistance_reflection_ko.md) · [검색 대상과 hash](ai_assistance_review_sources.csv)

기준일: 2026-10-12. 이 문서는 실행 계획이 아닌 회고용 증거 목록이다. 날짜는 기록의 구간 또는
문서 날짜이며 정확한 실행 시각과 다를 수 있다. 중복 사건·후속 정정을 묶은 38개 검토 항목이다.
실패 제출 수, AI 단독 오류 수, 실험 수와 같지 않다. `직접 연결 / 공동 작업 / 구분 필요`는
[반성문의 정의](ai_assistance_reflection_ko.md#이-문서가-다루는-범위)를 따른다.

발생 사실은 당시 원장이 그렇게 기록했음을 뜻한다. 그 기록의 원인 설명까지 검증 완료로 읽지 않는다.
로컬 결과는 보존된 원장·리뷰를 대조했으며 이번에 모델이나 실험을 다시 실행하지 않았다.
개별 Private 점수·최종 선택은 수기 기록이고 원본 export와 독립 대조되지 않았다.

## 사례 목록

| ID | 기록 구간 | 항목 | AI와의 연결 |
|---|---|---|---|
| R01 | 7월–8월 초 | [평가 계약을 뒤늦게 바로잡음](#r01) | 공동 작업 |
| R02 | 7월 | [Gemini 공개 자료 분석 누락](#r02) | 직접 연결 |
| R03 | 8월 초 | [버전이 다른 외부 분석을 구현 근거로 삼을 위험](#r03) | 공동 작업 |
| R04 | 7월 | [초기 제출과 파일의 연결을 복원하기 어려움](#r04) | 공동 작업 |
| R05 | 7월 말–8월 초 | [v4 예산 회계와 추정 overhead를 혼합](#r05) | 공동 작업 |
| R06 | 8월 초 | [미검증 조합을 “열등하지 않음”으로 보장](#r06) | 공동 작업 |
| R07 | 8월 초 | [한 모델 관찰과 제출 평가 범위를 혼동](#r07) | 공동 작업 |
| R08 | 8월 | [형식 오류를 인프라 flake로 단정](#r08) | 구분 필요 |
| R09 | 8월 | [천장과 noise 폭을 확정적으로 반복 해석](#r09) | 공동 작업 |
| R10 | 8월 | [v18의 혼합 변화와 평가 규칙 변경을 원인 증명으로 사용](#r10) | 공동 작업 |
| R11 | 8월 | [타 참가자 영상·점수를 충분한 맥락 없이 역설계](#r11) | 공동 작업 |
| R12 | 대회 중–종료 후 | [Private 위험을 논의했지만 최종 선택을 같은 계열에 집중](#r12) | 공동 작업 |
| R13 | 8월 | [v24: 코드 문자열만 만들고 attack.py를 쓰지 않음](#r13) | 공동 작업 |
| R14 | 8월 | [v24 cap에 다른 형식의 latency 사용](#r14) | 공동 작업 |
| R15 | 8월 | [로컬 multipost 성공에서 hosted 440–490점을 예측](#r15) | 공동 작업 |
| R16 | 8월 | [v26 다중 메시지의 무손실 fallback 가정](#r16) | 공동 작업 |
| R17 | 8월 | [선택 목적과 v27 인과 해석의 정정이 흔들림](#r17) | 공동 작업 |
| R18 | 8월 | [합성 cell 충돌을 실제 문제처럼 사용](#r18) | 공동 작업 |
| R19 | 8월 | [합산 점수로 생성 비용·시도 수를 단정](#r19) | 공동 작업 |
| R20 | 8월 | [관찰할 수 없는 stderr·모델 분기를 확인 과제로 반복](#r20) | 공동 작업 |
| R21 | 8월 | [로컬 후보 수 plateau에서 hosted 우열을 추정](#r21) | 공동 작업 |
| R22 | 8월 25–26일 기록 | [method14 Markdown 코드펜스 복사 오류](#r22) | 구분 필요 |
| R23 | 8월 27일 | [AI가 다른 목표를 최적화하고 기존 카드 재제출을 추천](#r23) | 직접 연결 |
| R24 | 8월 29일 | [replay_floor 산술을 모델별 실험 효과로 오인](#r24) | 공동 작업 |
| R25 | 8월 29일 | [timeout thread 뒤 모델 서버 재사용과 kernel crash](#r25) | 구분 필요 |
| R26 | 8월 30–31일 | [유효한 0을 결측 fallback으로 바꾸는 reporting bug](#r26) | 공동 작업 |
| R27 | 8월 28–31일 | [multipost의 서로 다른 구현을 한 일반론으로 묶음](#r27) | 공동 작업 |
| R28 | 8월 30일 | [5개 카드의 공유 classifier·분기 전제와 비교쌍 누락](#r28) | 공동 작업 |
| R29 | 8월 30–31일 | [harness 이름과 warmed latency를 실환경 증거로 확대](#r29) | 공동 작업 |
| R30 | 8월 31일·9월 2일 | [Kaggle에서 없는 개발 경로·출력 폴더에 의존](#r30) | 공동 작업 |
| R31 | 9월 2일 정정 | [SafeProbe 지표가 실제 scorer와 다른 정의](#r31) | 공동 작업 |
| R32 | 9월 1–2일 | [method80: 2-hop 시제품을 3-hop 후보의 proof로 사용](#r32) | 공동 작업 |
| R33 | 9월 2일 | [method81: 다른 도구·taint 조건을 local proof로 제시](#r33) | 공동 작업 |
| R34 | 9월 2일 | [method82–85: 이상적인 trace와 실제 도달 가능성·gate를 혼동](#r34) | 공동 작업 |
| R35 | 9월 1일 | [다른 AI 채팅의 stale 파일 추천과 method 번호 재사용](#r35) | 직접 연결 |
| R36 | 9월 1일 | [엄격한 반성 리뷰에도 근거 없는 사실·보장이 섞임](#r36) | 공동 작업 |
| R37 | 9월 2일 | [마감 후보의 정적 검증과 실행 준비 상태를 구분](#r37) | 구분 필요 |
| R38 | 10월 11–12일 공개 전 검토 | [사후 공개 문서에서 기전·기여·결과를 과장할 위험](#r38) | 공동 작업 |

## 발생·영향·정정·반성

<a id="r01"></a>

### R01 — 평가 계약을 뒤늦게 바로잡음

기록 구간: 7월–8월 초 · AI와의 연결: **공동 작업**

- **문제:** 존재하지 않는 fixture ID를 사용하는 접근, 모델별 예산 18,000→9,000초 정정, 로컬 4-hop과 실제 8-hop의 차이, severity 3의 실제 가중치 4를 뒤늦게 확인한 기록이 있다.
- **기록된 영향:** 가용 데이터·시간·점수에 관한 잘못된 전제로 실험을 설계했다. fixture 접근 실패는 정상 점수의 증거가 아니며, 각 오류의 손실을 개별 수치로 분리하지 못했다.
- **정정과 한계:** 초기의 “secret을 읽지 않아 실패”라는 설명도 모든 EXFILTRATION에 적용되는 규칙으로 재사용하지 않는다. 현재 채점 설명은 보존된 SDK snapshot에 한정한다.
- **반성할 사항:** AI 분석에 앞서 입력 fixture, 예산 단위, hop, predicate와 severity를 원본 함수에서 확인한다.
- **근거:** [실험 원장 L48–60](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L48-L60) · [실험 원장 L192–203](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L192-L203) · [실험 원장 L351–365](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L351-L365)

<a id="r02"></a>

### R02 — Gemini 공개 자료 분석 누락

기록 구간: 7월 · AI와의 연결: **직접 연결**

- **문제:** 원장은 Gemini Task 2가 대상 15개 중 13개만 처리해 중요한 노트북 2개를 빠뜨렸다고 기록한다.
- **기록된 영향:** 후속 자료 조사와 방향 판단에 불완전한 입력을 사용했다. 누락된 자료를 읽었다면 얻었을 점수나 절약할 시간을 계산할 수는 없다.
- **정정과 한계:** Task 3 등의 후속 분석은 별도 기록이다. 요약의 길이나 구체성이 입력 전체를 읽었다는 증거는 아니다.
- **반성할 사항:** 입력 목록과 완료 목록을 대조하고, 실패·누락·원문 미확인 항목을 명시하게 한다.
- **근거:** [실험 원장 L169–176](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L169-L176) · [실험 원장 L236–238](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L236-L238)

<a id="r03"></a>

### R03 — 버전이 다른 외부 분석을 구현 근거로 삼을 위험

기록 구간: 8월 초 · AI와의 연결: **공동 작업**

- **문제:** PDF 분석의 ctx-key 접근 가능성·taint 설명 등이 현재 코드와 맞지 않았고, 분석 대상 SDK 버전도 달랐다. 기록은 작성자를 Gemini 계열로 추정했지만 확정하지 않는다.
- **기록된 영향:** 잘못된 전제를 구현에 넣을 위험이 있었으나 이 기록에서는 코드 대조로 걸러냈다. 실제 잘못된 제출이 발생했다고 세지 않는다.
- **정정과 한계:** 원문 함수·설치 버전·접근 가능한 인터페이스를 대조한 예방 사례다. upstream 주석의 값과 실제 코드 값도 별도로 확인해야 한다.
- **반성할 사항:** 2차 요약에는 분석 대상 버전과 코드 위치를 요구하고 현재 snapshot과 비교한다.
- **근거:** [실험 원장 L428–431](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L428-L431) · [실험 원장 L830–857](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L830-L857)

<a id="r04"></a>

### R04 — 초기 제출과 파일의 연결을 복원하기 어려움

기록 구간: 7월 · AI와의 연결: **공동 작업**

- **문제:** 초기 요약은 v1의 제출 점수 4.670을 적지만 다른 구간은 해당 버전을 미제출로 적고, 정확한 제출 코드가 불명확하다는 기록도 남긴다.
- **기록된 영향:** 초기 점수를 어느 구현의 효과로 해석해야 하는지 불분명해졌다.
- **정정과 한계:** 현재 CSV의 회고적 이름 매핑만으로 당시 업로드한 바이트가 확인되는 것은 아니다. 이 충돌은 확정적으로 해소하지 못했다.
- **반성할 사항:** 제출 ID·전체 파일 hash·원본 파일·평가 시각을 함께 보존한다.
- **근거:** [실험 원장 L26–27](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L26-L27) · [실험 원장 L56–60](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L56-L60) · [실험 원장 L101–104](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L101-L104)

<a id="r05"></a>

### R05 — v4 예산 회계와 추정 overhead를 혼합

기록 구간: 7월 말–8월 초 · AI와의 연결: **공동 작업**

- **문제:** warmup 미차감, 무조건적인 bank cap, 반복 probe의 예산 사용 등이 기록됐다. 이후 실제 측정 없이 agent factory의 재로딩 비용을 추정하고 안전계수를 중첩했다.
- **기록된 영향:** timeout과 underfill 위험이 함께 생겼다. v4 37.470, relaxed 60.630 등의 관찰은 있으나 각각의 변화가 점수 차이를 얼마나 만들었는지 격리되지 않았다.
- **정정과 한계:** 후속 소스 확인은 모델이 미리 로드된 wrapper 구조를 기록한다. 초기에 추정한 재로딩 설명을 확정 원인으로 유지하지 않는다.
- **반성할 사항:** 관측한 시간·추정한 비용·안전 여유를 별도 항으로 기록한다.
- **근거:** [실험 원장 L136–160](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L136-L160) · [실험 원장 L480–486](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L480-L486) · [실험 원장 L701–706](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L701-L706) · [실험 원장 L935–941](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L935-L941)

<a id="r06"></a>

### R06 — 미검증 조합을 “열등하지 않음”으로 보장

기록 구간: 8월 초 · AI와의 연결: **공동 작업**

- **문제:** v7/v8 조합이 v3보다 나쁠 이유가 없다는 보장과 일일 5-slot 채우기 논리가 있었다.
- **기록된 영향:** 두 조합은 0점으로 기록됐다. 무해한 결합이라는 가정이 실제 제출에서 지지되지 않았다.
- **정정과 한계:** 생성·replay·예산·공유 실패 요인을 검증하지 않은 조합에는 baseline 유지 보장을 붙일 수 없다. 0점의 정확한 hosted 분기는 미확인이다.
- **반성할 사항:** combo는 구성요소의 개별 근거와 상호작용 위험을 따로 적고 슬롯을 채우기 위해 제출하지 않는다.
- **근거:** [실험 원장 L381–395](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L381-L395) · [실험 원장 L492–507](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L492-L507)

<a id="r07"></a>

### R07 — 한 모델 관찰과 제출 평가 범위를 혼동

기록 구간: 8월 초 · AI와의 연결: **공동 작업**

- **문제:** Gemma-only 0 결과로 원인을 확정해 GPT 쪽 검증을 낮게 두었고, v5_gemma_harmony는 “Gemma와 무관”하다는 이유로 삭제 대상으로 다뤘다.
- **기록된 영향:** 이후 모든 제출이 두 모델에서 평가됨을 정정했다. v5_gpt 75.345와 Gemma 계열 58.855 등의 결과는 있어도 모델별 기여가 직접 공개되지는 않았다.
- **정정과 한계:** 한 모델에 대한 관찰은 다른 모델의 기전이나 결합 점수의 분해를 증명하지 않는다.
- **반성할 사항:** 모델별 사실과 cross-model inference를 별도로 표시한다.
- **근거:** [실험 원장 L532–549](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L532-L549) · [실험 원장 L683–693](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L683-L693) · [실험 원장 L703–731](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L703-L731)

<a id="r08"></a>

### R08 — 형식 오류를 인프라 flake로 단정

기록 구간: 8월 · AI와의 연결: **구분 필요**

- **문제:** 일부 Submission Format Error를 서버 flakiness로 읽고 재시도로 해결된다는 설명을 붙였다.
- **기록된 영향:** 재시도 성공은 관찰될 수 있지만 최초 실패가 인프라 원인이라는 증거는 아니다. 이후 v24 파일 작성 누락과 method14 코드펜스 오류는 별도 원인이 확인됐다.
- **정정과 한계:** 모든 형식 오류를 하나의 원인으로 합치지 않는다. 원본 로그 없는 실패는 원인 미상으로 남긴다.
- **반성할 사항:** 로컬 계약 위반, 복사 오류, 인프라 문제, 원인 미상을 나눠 기록한다.
- **근거:** [실험 원장 L935–997](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L935-L997) · [실험 원장 L1475–1491](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1475-L1491) · [실험 원장 L1904–1914](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1904-L1914)

<a id="r09"></a>

### R09 — 천장과 noise 폭을 확정적으로 반복 해석

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** 87–89, 86–89, 약 93 등의 점수 군집으로 재현 가능한 천장을 선언하고, 범위에서 ±1.6·±3.6 등을 noise 폭처럼 사용했다. generation-bound와 replay-bound 판단도 바뀌었다.
- **기록된 영향:** 특정 설명을 다음 실험의 기본 전제로 두거나 다른 축을 조기에 닫는 방향으로 문서가 이동했다. 잘못 닫힌 축의 기회비용은 측정되지 않았다.
- **정정과 한계:** 점수 군집은 관찰이다. 반복·동일 artifact·동일 평가 조건·불확실성 추정 없이 물리적 ceiling이나 confidence interval이 되지 않는다.
- **반성할 사항:** 최고점, 관측 범위, 반복 분산, 가정한 상한을 구분한다.
- **근거:** [실험 원장 L418–450](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L418-L450) · [실험 원장 L877–911](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L877-L911) · [실험 원장 L1121–1171](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1121-L1171) · [실험 원장 L1204–1219](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1204-L1219) · [실험 원장 L1322–1327](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1322-L1327) · [실험 원장 L1493–1511](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1493-L1511)

<a id="r10"></a>

### R10 — v18의 혼합 변화와 평가 규칙 변경을 원인 증명으로 사용

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** FBF, budget fraction 등의 차이를 함께 둔 비교와 평가 규칙 변경 전후 결과로 FBF나 partial scoring의 효과를 확정했다.
- **기록된 영향:** 원인별 효과를 분리할 수 없는 비교가 다음 정책 선택의 근거가 됐다.
- **정정과 한계:** 원장은 중간에 partial score 규칙을 적지만 후반에는 timeout이면 전부 0이라고 적는다. 다른 버전·상황의 규칙을 현재의 단일 사실로 합칠 수 없다.
- **반성할 사항:** 한 주요 요인만 바꾸고 SDK·evaluator 버전과 cutoff 동작을 비교 기록에 고정한다.
- **근거:** [실험 원장 L1261–1303](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1261-L1303) · [실험 원장 L2441–2449](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2441-L2449)

<a id="r11"></a>

### R11 — 타 참가자 영상·점수를 충분한 맥락 없이 역설계

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** 110점의 평가 시점을 잘못 읽어 사용자에게 정정받았고, 영상 제목으로 해당 고득점 방식이라 추정해 탐색 계획을 만들었다.
- **기록된 영향:** 다음 기록에서 영상이 6월·defense track 자료였음을 확인했다. 당시 예상한 +80% 등의 상방은 독립 실행 근거가 없었다.
- **정정과 한계:** 제목·점수·채널명은 구현 증거가 아니다. 이 사례는 경쟁자 방식의 성공 여부와 관계없다.
- **반성할 사항:** 날짜·track·코드·실험 조건을 확인하기 전에는 참고 가설로만 둔다.
- **근거:** [실험 원장 L1329–1366](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1329-L1366) · [실험 원장 L1390–1407](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1390-L1407)

<a id="r12"></a>

### R12 — Private 위험을 논의했지만 최종 선택을 같은 계열에 집중

기록 구간: 대회 중–종료 후 · AI와의 연결: **공동 작업**

- **문제:** 숨겨진 방어의 위험과 hedge 논의가 있었지만 throughput이 양 board에 전이될 것이라는 가정과 “Private도 아마 괜찮다”는 해석이 반복됐다.
- **기록된 영향:** 수기 CSV의 최종 선택 v27_adapt·method39는 Private 0, 미선택 v11_deputy_transfer는 14.605다. 최종 선택 책임은 작성자에게 있다.
- **정정과 한계:** 정확한 Private 결과는 당시 알 수 없었다. AI가 0점을 단독으로 초래했거나 대안을 택하면 메달이 보장됐다는 결론은 불가하다.
- **반성할 사항:** 최종 선택에도 숨은 평가 가정과 선택들 사이의 공유 실패 위험을 남긴다.
- **근거:** [실험 원장 L72–76](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L72-L76) · [실험 원장 L999–1008](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L999-L1008) · [실험 원장 L1046–1064](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1046-L1064) · [실험 원장 L1086–1095](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1086-L1095) · [실험 원장 L1686–1698](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1686-L1698) · [실험 원장 L1740–1742](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1740-L1742) · [수기 제출 표](../results/submissions.csv)

<a id="r13"></a>

### R13 — v24: 코드 문자열만 만들고 attack.py를 쓰지 않음

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** v5–v24 노트북 셀에는 attack.py를 작성하는 마지막 단계가 없었다. 이전에는 남은 수동 파일에 의존했고 전체 셀 교체 후 문제가 드러났다. 사용자가 누락을 지적했다.
- **기록된 영향:** v24 첫 5개가 모두 Submission Format Error. 제출 CSV order 84–88에서도 확인된다. 내부 compile과 로컬 stage0 통과가 최종 산출물 생성을 검증하지 못했다.
- **정정과 한계:** 문서상 전체 셀 검증과 파일 작성 단계로 교정했다. 같은 오류를 공격 가설의 0점으로 해석하면 안 된다.
- **반성할 사항:** 최종 셀을 독립 작업 디렉터리에서 확인하고 산출물 이름·바이트·함수 계약을 검증한다.
- **근거:** [실험 원장 L1475–1491](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1475-L1491) · [수기 제출 표](../results/submissions.csv)

<a id="r14"></a>

### R14 — v24 cap에 다른 형식의 latency 사용

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** plain classifier의 latency로 Harmony 후보 수를 제한해 대표 비용과 cap 계산 대상이 어긋났다.
- **기록된 영향:** blind_cap 61.605, control 87.210이 기록됐다. 원장은 underfill로 설명하지만 실제 hosted 후보별 timing은 없다.
- **정정과 한계:** 측정 대상 불일치는 확인된 설계 문제이며 점수 차이 전체의 단독 원인으로 확정하지 않는다.
- **반성할 사항:** 예산을 제한할 비용은 실제 반환할 형식과 같은 실행 경로에서 측정한다.
- **근거:** [실험 원장 L1503–1514](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1503-L1514)

<a id="r15"></a>

### R15 — 로컬 multipost 성공에서 hosted 440–490점을 예측

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** 로컬 GPU의 8/8 동작과 집계 점수로 추정한 고정 overhead를 사용해 큰 hosted 점수를 예측했다.
- **기록된 영향:** mp4/mp8 제출은 control 88.515보다 낮았다. 로컬 동작 성공에서 점수 전이를 예측하는 연결이 성립하지 않았다.
- **정정과 한계:** 후속 “remote는 한 post만 된다” 설명 역시 직접 hosted trace로 확인된 결론은 아니다. 정확한 parser·model·timing 원인은 미확인이다.
- **반성할 사항:** proxy는 행동 확인에 사용하고 장비·guardrail·replay 비용을 건너뛴 점수 예측을 피한다.
- **근거:** [실험 원장 L1528–1573](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1528-L1573)

<a id="r16"></a>

### R16 — v26 다중 메시지의 무손실 fallback 가정

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** fire되지 않으면 안전하게 single로 접혀 최소 기존 점수에 가까울 것이라는 가정이 있었다.
- **기록된 영향:** M32 38.870, M1 89.550으로 기록돼 해당 구현의 무손실 가정이 지지되지 않았다.
- **정정과 한계:** 한 구현의 실패는 모든 multi-message 방식의 불가능성을 증명하지 않는다. fallback 자체와 그 비용도 측정해야 한다.
- **반성할 사항:** 추가 메시지가 계산량·종료·시간 예산을 바꾸는지 별도로 확인한다.
- **근거:** [실험 원장 L1575–1593](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1575-L1593)

<a id="r17"></a>

### R17 — 선택 목적과 v27 인과 해석의 정정이 흔들림

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** fire_rate만 보던 선택을 fire_rate/latency로 고쳤다는 기록 이후, 다른 구간에서 v27이 다시 fire_rate-only라고 기술됐다. 93.060을 적응 효과로 읽었다가 v28 결과로 “noise 증명”이라고 바꿨다.
- **기록된 영향:** 정확한 버전 연결과 비교 조건이 불분명한 채 적응 정책을 살리거나 버리는 논거가 바뀌었다.
- **정정과 한계:** 다른 구성의 하락은 원래 고점의 효과가 증명됐다는 주장도, noise로 증명됐다는 주장도 뒷받침하지 않는다.
- **반성할 사항:** 비교 파일 hash·목적 함수·동일성부터 확인하고 정정은 새 증거가 허용하는 범위까지만 한다.
- **근거:** [실험 원장 L1620–1623](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1620-L1623) · [실험 원장 L1647–1652](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1647-L1652) · [실험 원장 L1669–1683](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1669-L1683) · [실험 원장 L1807–1822](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1807-L1822)

<a id="r18"></a>

### R18 — 합성 cell 충돌을 실제 문제처럼 사용

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** subagent가 만든 낮은 novelty cell 반례에서 점수 개선 가능성을 계산하고 현실의 URL cell 충돌과 연결했다.
- **기록된 영향:** 현실적인 domain 변형은 69–73대로 낮아졌고, 별도 local gateway에서는 600/600 cell이 고유했다.
- **정정과 한계:** 반례는 버그가 가능함을 보여줄 뿐 원래 후보에서 발생했음을 보여주지 않는다. local unique 결과도 hosted uniqueness 전체를 보증하지 않는다.
- **반성할 사항:** 합성 반례, 실제 입력 재현, hosted 관찰을 분리한다.
- **근거:** [실험 원장 L1700–1725](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1700-L1725) · [실험 원장 L1762–1767](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1762-L1767)

<a id="r19"></a>

### R19 — 합산 점수로 생성 비용·시도 수를 단정

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** 약 93점에서 두 번의 generation·prefill 하한을 추정하고, forum의 200–250 관찰을 채점 상한처럼 읽었다. 점수/0.09를 후보·시도 수로 넓혀 사용했다.
- **기록된 영향:** generation인지 replay인지, 어디를 줄여야 하는지에 관한 방향 결정이 측정하지 않은 비용 분해에 의존했다.
- **정정과 한계:** 단계별 timing 없는 역산은 가정이다. 0.09는 severity-5 finding과 신규 cell 등의 조건 아래의 관계이며 반환·시도 횟수의 일반 공식이 아니다. “first 200–250만 채점” 규칙은 확인되지 않았다.
- **반성할 사항:** 집계 점수에서 식별할 수 없는 내부 비용은 unknown으로 두고 조건부 계산의 조건을 적는다.
- **근거:** [실험 원장 L1727–1779](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1727-L1779) · [실험 원장 L2108–2124](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2108-L2124)

<a id="r20"></a>

### R20 — 관찰할 수 없는 stderr·모델 분기를 확인 과제로 반복

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** 제출 UI에서 stderr가 보이지 않는다는 기록 뒤에도 [RANK]·chosen 로그를 읽으면 selection과 모델 분기가 판명된다는 제안이 다시 등장했다.
- **기록된 영향:** 실제 가능한 관찰을 확보하지 못한 채 기대한 로그에 의존해 원인을 판정하려 했다.
- **정정과 한계:** log 확인 요청이 실제 확인 완료 기록은 아니다. 합산 점수와 같은 창의 baseline만으로도 정확한 두 모델 기여는 식별되지 않을 수 있다.
- **반성할 사항:** 가능한 관측 수단부터 확인하고 증거가 없으면 분기·기여를 미확인으로 남긴다.
- **근거:** [실험 원장 L887–890](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L887-L890) · [실험 원장 L1654–1659](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1654-L1659) · [실험 원장 L1953–1956](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1953-L1956) · [S02 원문 L160–181](#s02)

<a id="r21"></a>

### R21 — 로컬 후보 수 plateau에서 hosted 우열을 추정

기록 구간: 8월 · AI와의 연결: **공동 작업**

- **문제:** 로컬 결과들이 180개 cap에 붙은 상태에서 blind 구현이 빨라 보인다는 이유로 제출 우선순위를 높였다.
- **기록된 영향:** Kaggle method1 89.1, blind 87.435 관찰은 그 로컬 우선순위를 지지하지 않았다.
- **정정과 한계:** cap에 묶인 반환 수와 빠른 generation이 replay finding이나 최종 점수 순위와 같지는 않다. 반전의 정확한 기전은 미확인이다.
- **반성할 사항:** 상한에 포화된 지표를 비교력이 있는 지표로 취급하지 않는다.
- **근거:** [실험 원장 L1836–1902](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1836-L1902)

<a id="r22"></a>

### R22 — method14 Markdown 코드펜스 복사 오류

기록 구간: 8월 25–26일 기록 · AI와의 연결: **구분 필요**

- **문제:** 코드 셀에 ```가 함께 붙여넣어져 SyntaxError가 났다. 원본 실패 노트와 통합 원장의 기록 날짜는 다르게 나타난다.
- **기록된 영향:** KaggleError로 끝났으며 해당 공격 전략은 이 제출에서 평가되지 않았다.
- **정정과 한계:** 사용자 입력·전달 형식의 오류다. AI 알고리즘 실패나 Kaggle 인프라 실패로 분류하지 않는다.
- **반성할 사항:** 복사 가능한 raw 파일과 설명 문서를 구분하고 최종 셀의 문법을 확인한다.
- **근거:** [실험 원장 L1904–1914](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1904-L1914) · [S07 원문 L3–12](#s07)

<a id="r23"></a>

### R23 — AI가 다른 목표를 최적화하고 기존 카드 재제출을 추천

기록 구간: 8월 27일 · AI와의 연결: **직접 연결**

- **문제:** 기록의 AI 재검토는 method21/22 재제출 추천을 철회하며, 작은 최고점 갱신 확률을 최적화했지만 사용자는 +10/100+ 구조 변화를 원했다고 인정했다.
- **기록된 영향:** 슬롯 배분 제안이 요청한 목적과 어긋났다. 추천 철회 기록은 있으나 그 추천대로 실제 중복 제출했다고 단정하지 않는다.
- **정정과 한계:** 기존 채점 artifact의 재추천과 새 가설을 구분해야 한다. 목표를 맞추는 것만으로 새 계획의 상방이 증명되는 것은 아니다.
- **반성할 사항:** 목표 값·배치 목적·동일 artifact 금지·공유 실패 위험을 AI 요청에 먼저 고정한다.
- **근거:** [실험 원장 L1920–1923](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1920-L1923) · [S01 원문 L17–53](#s01)

<a id="r24"></a>

### R24 — replay_floor 산술을 모델별 실험 효과로 오인

기록 구간: 8월 29일 · AI와의 연결: **공동 작업**

- **문제:** probe의 floor 1.55/1.80/2.05가 실제 latency를 덮어 반환 수를 결정했다. 41→48/36, 평균 42와 +0.09가 반복돼 모델별 replay 개선으로 읽혔다.
- **기록된 영향:** 생산 코드에 없는 floor를 넣는 5개 카드 계획의 근거가 됐다. 검토가 이 승격을 반박했다.
- **정정과 한계:** floor 배정을 뒤집어도 평균 41.81로 같다. score가 findings의 상수배이고 findings=returned인 구간은 새 독립 정보가 아니다. 당시 리뷰는 raw JSON을 직접 보지 못했고 소스와 전사 집계값을 대조했다. 리뷰의 부모 대비 점수 상한·hosted 병목 단정까지 모두 확인된 사실로 수용하지 않는다.
- **반성할 사항:** 실제 baseline을 포함하고 label swap·상수 지배·실패 가능한 성공 규칙을 검사한다.
- **근거:** [실험 원장 L1993–2013](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1993-L2013) · [S02 원문 L21–78](#s02) · [S02 원문 L184–189](#s02)

<a id="r25"></a>

### R25 — timeout thread 뒤 모델 서버 재사용과 kernel crash

기록 구간: 8월 29일 · AI와의 연결: **구분 필요**

- **문제:** control은 반환 96·replay 완료 63·점수 5.67을 냈고 timeout 후 다음 profile 시작 때 GGML_ASSERT/DeadKernelError가 났다.
- **기록된 영향:** 다음 tail profile은 평가되지 않았다. 그 결과로 tail prompt의 성능을 기각할 수 없었다.
- **정정과 한계:** 종료되지 않은 daemon thread와 같은 서버의 다음 요청이 겹쳤을 가능성이 원문에 기록됐다. 확정된 thread trace는 없으므로 probable 구현 원인으로 남긴다. 동기 cutoff로 수정한 기록이 있다.
- **반성할 사항:** deadline 반환과 작업 종료를 구분하고 자원 정리가 끝나기 전 다음 실험을 시작하지 않는다.
- **근거:** [S03 원문 L16–57](#s03)

<a id="r26"></a>

### R26 — 유효한 0을 결측 fallback으로 바꾸는 reporting bug

기록 구간: 8월 30–31일 · AI와의 연결: **공동 작업**

- **문제:** `(blocked_rate or 1.0)`가 유효한 0.0을 1.0으로 바꿔 H6 결과를 collapsed_single로 보고했다.
- **기록된 영향:** 실제로는 0-post인데 다른 실패 형태처럼 분류했다. 판정 문구와 해석이 잘못됐다.
- **정정과 한계:** reporting 수정 후에도 실패한 실제 gate를 성공으로 뒤집지 않는다. 보고 오류 교정은 전략 개선의 증거가 아니다.
- **반성할 사항:** 0·None·empty row를 구분하고 지표 계산에 경계 입력을 넣어 확인한다.
- **근거:** [실험 원장 L2041–2077](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2041-L2077)

<a id="r27"></a>

### R27 — multipost의 서로 다른 구현을 한 일반론으로 묶음

기록 구간: 8월 28–31일 · AI와의 연결: **공동 작업**

- **문제:** same-generation multi-call, multi-message, multi-hop sequential post를 multipost 하나로 묶어 초반에는 dead, 후반에는 breakthrough로 크게 해석했다. Gemma 제약을 GPT ceiling으로 넓혔다.
- **기록된 영향:** 일부 탐색을 닫거나 반대로 특정 구조에 집중하는 설명이 만들어졌다. 실제 잃은 가능한 최고점은 측정되지 않았다.
- **정정과 한계:** 당시 주요 반성 리뷰는 모델별 관찰과 구현별 실패로 범위를 좁혔다. 이후 “multi-message 미실험” 표현도 앞선 v26 기록과 함께 읽어야 한다.
- **반성할 사항:** 실험명에 구현·모델·환경·기각 범위를 포함한다.
- **근거:** [실험 원장 L1575–1593](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L1575-L1593) · [실험 원장 L2145–2158](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2145-L2158) · [S04 원문 L9–29](#s04) · [S04 원문 L31–59](#s04)

<a id="r28"></a>

### R28 — 5개 카드의 공유 classifier·분기 전제와 비교쌍 누락

기록 구간: 8월 30일 · AI와의 연결: **공동 작업**

- **문제:** 53–57 계획은 독립 구조 5개라기보다 k·ordering 변형이었다. 정적 model-name 훅이 없는데 per-model 분기를 전제했고, selector의 빈 row는 single fallback을 남겼다. 원인 해석용 same-window anchor도 빠졌다.
- **기록된 영향:** 한 미검증 부품이 배치 전체를 좌우하며, 결과가 나와도 어디서 차이가 났는지 알기 어려운 설계였다. 검토가 수정을 요구했다.
- **정정과 한계:** anchor는 결합 점수 비교를 돕지만 모델별 정확한 분해를 보장하지 않는다. 리뷰가 순서 점수 차이를 GPT 비용으로 단정한 부분도 추론이다. score_max endgame에서 항상 control이 필수라는 일반 규칙으로 확대하지 않는다.
- **반성할 사항:** 실제로 가능한 분기·공유 실패 요인·배치 목적을 점검하고 해석에 필요한 비교를 남긴다.
- **근거:** [S05 원문 L25–58](#s05)

<a id="r29"></a>

### R29 — harness 이름과 warmed latency를 실환경 증거로 확대

기록 구간: 8월 30–31일 · AI와의 연결: **공동 작업**

- **문제:** resolved_harness=board_remote를 실제 board timing처럼 읽었다. k8의 warmed 결과를 cold outlier가 포함된 single baseline과 비교했고, 후반 k8 두 번째 6–7초대 관찰로 100% 신뢰를 주장했다.
- **기록된 영향:** 조건이 다른 속도 비교와 재현성 과장이 후보 승격의 근거가 됐다. 첫 실행의 91.3/167.4초도 원장에 남아 있다.
- **정정과 한계:** 원문 후속 대조는 board_remote가 로컬 모델 서버와 parser의 조합일 수 있음을 정정했다. timing·모델·환경의 동일성은 label만으로 확인되지 않는다.
- **반성할 사항:** cold/warm, 반복 수, tail latency와 실제 resolved backend를 함께 보존한다.
- **근거:** [실험 원장 L2415–2449](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2415-L2449) · [S05 원문 L50–53](#s05) · [S06 원문 L132–141](#s06)

<a id="r30"></a>

### R30 — Kaggle에서 없는 개발 경로·출력 폴더에 의존

기록 구간: 8월 31일·9월 2일 · AI와의 연결: **공동 작업**

- **문제:** compile은 통과했지만 Kaggle의 /kaggle/working에서 codex/ 경로의 prompt를 읽다가 FileNotFoundError가 났다. 9월 2일 method80 probe에서도 파일 경로와 output directory 문제가 반복됐다.
- **기록된 영향:** 행동·점수를 얻기 전 실행이 멈췄으며 추가 수정·재전달이 필요했다.
- **정정과 한계:** prompt inline과 mkdir 규칙으로 수정한 기록이 있다. 규칙을 문서에 추가한 것만으로 모든 과거 script가 검증된 것은 아니다.
- **반성할 사항:** 배포 환경에 없는 외부 파일을 제거하고 입력·출력 계약을 실제 전달 artifact에서 확인한다.
- **근거:** [실험 원장 L2206–2244](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2206-L2244) · [실험 원장 L2541–2542](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2541-L2542)

<a id="r31"></a>

### R31 — SafeProbe 지표가 실제 scorer와 다른 정의

기록 구간: 9월 2일 정정 · AI와의 연결: **공동 작업**

- **문제:** timeout_free_n은 SDK timeout 결과가 아니라 loop 진입 수, unique_cells는 get_score_cell_hash 결과가 아니라 index, score_norm 역시 실제 scorer 정의와 달랐다.
- **기록된 영향:** clean_avoid 우위·fixed-k 기각·method69 예약 등에 사용한 근거가 철회됐다. 측정 정의 오류는 실험 결과 해석을 직접 무효화했다.
- **정정과 한계:** 정정은 선택한 결론을 withdrawn/inconclusive로 처리한다. 행동이 더 느렸다는 제한적 관찰만 남기며 다른 후보가 새롭게 우월하다고 선언하지 않는다.
- **반성할 사항:** metric 이름과 생성 코드를 연결하고 valid scorer·hash·timeout 함수를 사용했는지 확인한다.
- **근거:** [실험 원장 L2486–2502](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2486-L2502)

<a id="r32"></a>

### R32 — method80: 2-hop 시제품을 3-hop 후보의 proof로 사용

기록 구간: 9월 1–2일 · AI와의 연결: **공동 작업**

- **문제:** 2-hop email 계열 probe의 성공 관찰을 다른 prompt·3-hop의 dynamic-secret 후보에 연결해 최우선 후보로 삼았다.
- **기록된 영향:** 실제 method80에 가까운 후속 로컬 검증에서는 GPT 0이 기록됐다. 과거 시제품의 성공이 새 전체 흐름에 전이되지 않았다.
- **정정과 한계:** 이 결과는 해당 로컬 후보의 실패다. 새 도구·hop·prompt의 실제 도달 가능성은 각각 검증해야 한다.
- **반성할 사항:** 시제품에서 완성 후보로 바뀐 모든 단계를 명시하고 hash가 같은 후보로 end-to-end 질문을 검증한다.
- **근거:** [실험 원장 L2510–2520](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2510-L2520) · [실험 원장 L2550–2553](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2550-L2553)

<a id="r33"></a>

### R33 — method81: 다른 도구·taint 조건을 local proof로 제시

기록 구간: 9월 2일 · AI와의 연결: **공동 작업**

- **문제:** local proof와 rank 1 설명이 붙었지만 실제 probe는 email CD를 확인했고 후보의 http EXFIL·taint trigger와 달랐다. 8-hop chain도 미검증 전제가 남았다.
- **기록된 영향:** 사용자가 근거 범위를 지적하고 inconclusive로 재판정했다. 기록의 우선순위 추천은 전체 후보의 성공 근거가 없었다.
- **정정과 한계:** 설명에 “proof”가 있어도 검사한 도구·predicate·trigger·모델 실행이 다른 증거라면 승격할 수 없다.
- **반성할 사항:** 검증 주장 옆에 실제 검사 대상과 빠진 조건을 적는다.
- **근거:** [실험 원장 L2522–2540](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2522-L2540)

<a id="r34"></a>

### R34 — method82–85: 이상적인 trace와 실제 도달 가능성·gate를 혼동

기록 구간: 9월 2일 · AI와의 연결: **공동 작업**

- **문제:** 합성 trace에서 guardrail과 3 predicate의 조건 충족을 100% proof로 설명했다. method83 동의어의 성공 gate 전에 84/85를 제작했다.
- **기록된 영향:** 후속 로컬에서 83·87은 양 모델 0, 84/85 CD는 aborted/falsified로 기록됐다. method85의 첫 marker 일부 결과는 전체 흐름의 성공과 구분된다.
- **정정과 한계:** 합성 입력이 함수를 통과하는 것과 모델이 그 입력을 생성하는 것은 다른 질문이다. 사전 제작 자체의 비용은 선택일 수 있지만 성공 gate를 통과한 후보로 취급해서는 안 된다.
- **반성할 사항:** predicate unit proof와 모델 도달 가능성 검증을 분리하고 downstream 승격을 upstream gate 뒤에 둔다.
- **근거:** [실험 원장 L2543–2548](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2543-L2548) · [실험 원장 L2555–2573](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2555-L2573)

<a id="r35"></a>

### R35 — 다른 AI 채팅의 stale 파일 추천과 method 번호 재사용

기록 구간: 9월 1일 · AI와의 연결: **직접 연결**

- **문제:** 다른 채팅의 AI가 과거 method76–78 이름을 새 제출처럼 제안했다. 동일 method 번호 아래 새 구현이 덮여 stale 위험도 기록됐다.
- **기록된 영향:** 이름만으로 최신 후보와 채점 이력을 구분할 수 없었다. 권고와 실행이 어긋날 위험이 발생했다.
- **정정과 한계:** 그 추천대로 모두 제출했거나 정확히 동일 바이트를 재제출했다는 뜻은 아니다. 번호보다 path·hash·현재 원장이 우선이다.
- **반성할 사항:** 새 채팅은 현재 상태 문서부터 읽고 정정·채점 registry·hash를 확인한다.
- **근거:** [실험 원장 L2427–2438](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2427-L2438)

<a id="r36"></a>

### R36 — 엄격한 반성 리뷰에도 근거 없는 사실·보장이 섞임

기록 구간: 9월 1일 · AI와의 연결: **공동 작업**

- **문제:** 한 리뷰는 gpt_oss의 모델 계보, 특정 control token의 전용성, 전체 고득점 카드의 오염, 두 모델 점수 180/7 분해를 단정했다. 낮은 multipost 점수만으로 candidate당 1회 채점이라고 선언하고 3,000–4,000개 제출의 고득점을 보장했다.
- **기록된 영향:** 교정처럼 보이는 새 설명이 또 다른 실험 방향의 전제가 될 위험이 있었다. 해당 추천의 실제 후속 인과관계는 이 기록으로 확정하지 않는다.
- **정정과 한계:** 이 발췌는 사실로 인용하는 것이 아니다. 두 모델 trace가 없고, method39는 여러 format을 선택하는 코드이며, 보존된 scorer의 finding/cell 계산도 candidate당 1회라는 단정과 구분된다. 역산된 수치와 미래 성능은 미확인이다.
- **반성할 사항:** 정정 문서에도 원자료·코드·반례를 요구하고 강한 표현을 검증 완료 표식으로 읽지 않는다.
- **근거:** [S08 원문 L3–31](#s08) · [method39 코드 해설](code_walkthrough.md#what-per-model-means-in-method39) · [현재 채점 설명](scoring_mechanics.md)

<a id="r37"></a>

### R37 — 마감 후보의 정적 검증과 실행 준비 상태를 구분

기록 구간: 9월 2일 · AI와의 연결: **구분 필요**

- **문제:** method88–92는 compile·AST·SHA 검사가 기록됐지만 evaluator runtime 검증은 없었다.
- **기록된 영향:** CSV 마지막 5행은 2개 Succeeded (after deadline), 3개 Submission Format Error다. 이 상태의 원인을 특정 코드 오류로 확정할 로그는 없다.
- **정정과 한계:** 마감에 정적 검사만으로 후보를 만들었을 수는 있지만 실행 성공·정상 채점 보장이 아니다. 실패는 AI 단독 원인으로 귀속하지 않는다.
- **반성할 사항:** 마감 의사결정에도 검증 수준·미검증 계약·늦은 채점 위험을 남긴다.
- **근거:** [실험 원장 L2575–2582](https://github.com/AhnJG/kaggle-ai-agent-security-postmortem/blob/06f520e28fb57e8940267fd3fa80c0755a1fba51/docs/experiment_log_ko.md?plain=1#L2575-L2582) · [수기 제출 표](../results/submissions.csv)

<a id="r38"></a>

### R38 — 사후 공개 문서에서 기전·기여·결과를 과장할 위험

기록 구간: 10월 11–12일 공개 전 검토 · AI와의 연결: **공동 작업**

- **문제:** 공개 전 검토는 hidden guardrail 확정, 대회 중 Private 결과를 알았다는 서술, 메달 보장, 모든 실험의 사전 등록·측정 유효성, AI 기여 비율·고정 역할, 공개 코드 계보·라이선스 범위 등을 교정했다.
- **기록된 영향:** 실험 실패 뒤에도 회고 문서가 실제보다 확신·독창성·검증 수준을 높여 보이게 할 수 있었다. 수정된 표현은 현재 문서에 반영돼 있다.
- **정정과 한계:** 이들은 공개 문서 품질 문제이며 대회 중 실패의 원인으로 소급하지 않는다. 초기 문장별 AI 작성자도 확정되지 않았다. 표·registry subset·probe 설치 한계도 출처 범위대로 읽는다.
- **반성할 사항:** 회고에서도 관찰·추론·unknown과 upstream·AI 지원·소유자 결정을 분리한다.
- **근거:** [공개 전 검토·수정 원장](publication_review_ko.md) · [기여와 결정 책임](agentic_research_workflow.md#contributions-and-decision-ownership)

## 개발 검토 문서의 원문 발췌

S01–S08은 원본 개발 폴더의 자체 검토 문서에서 발췌했다. 원본 전체는 이 저장소에 포함하지 않는다.
원문 hash는 2026-10-12에 읽은 파일 전체의 SHA-256이다. 번호와 문구를 보존하되 행 끝 공백을 제거하고, 사용자 로컬
절대 경로는 `<development-archive>/` 또는 `<local-file>`로 치환했다. hash는 이 발췌문 자체의 hash가 아니다.
아래의 제출 권고·명령·단정은 **당시 기록**이며, 현재 실행 지시나 이 회고의 확인된 결론이 아니다.
특히 S02·S05의 집계 점수 역산·모델별 원인 단정과 S08의 주장은 사례 본문의 한계를 함께 읽어야 한다.

<a id="s01"></a>

### S01 — submit_plan_10plus_corrected_2026-08-27.md

- 원본 경로: `codex/submit_plan_10plus_corrected_2026-08-27.md`
- 원본 SHA-256: `0030ebaaa71d5ce5d080b7ae2bc4986df270057df81457d6bcdc8aae7954ac77`

원본 L17–53:

```text
17: ## 한 줄 verdict
18:
19: 이전 추천은 **틀렸다.** 이유는 `P(92.385를 조금 넘길 확률)`을 최적화했지, 사용자가 원한 **`+10 / 100+` 구조 점프 확률**을 최적화하지 않았기 때문이다.
20:
21: ---
22:
23: ## 왜 이전 추천이 잘못됐는가
24:
25: ### 1. 목표 함수를 잘못 잡았다
26:
27: - 잘못 잡은 목표:
28:   - `P(max score > 92.385)`
29: - 사용자의 실제 목표:
30:   - `P(score >= 102.385)` 또는 최소 `P(score >= 100)`
31:
32: 이 차이는 작지 않다.
33: `method21`, `method22`는 첫 번째 목표에는 의미가 있지만, 두 번째 목표에는 거의 의미가 없다.
34:
35: ### 2. `method21`, `method22`는 밴드 안 재추첨 카드다
36:
37: - 직접 관찰:
38:   - `method21 = 92.385`
39:   - `method22 = 89.910`
40:   - 최근 문서들 자체가 `a_pre_imp` 계열은 대체로 `89~93` 밴드에 갇힌다고 정리한다.
41: - 결론:
42:   - 이 둘은 최고점을 `1~2`점 더 뽑을 수는 있어도,
43:   - 지금 원하는 `+10 / 100+` 목표엔 맞지 않는다.
44:
45: ### 3. 따라서 이번 계획에서는 `method21`, `method22`를 완전히 뺀다
46:
47: - `banked score`가 있으니 낮게 나와도 손해는 없다는 논리는 맞다.
48: - 하지만 그 말이 곧 **밴드 안 재추첨 카드에도 슬롯을 써도 된다**는 뜻은 아니다.
49: - 이번 배치의 슬롯은 **밴드 밖으로 나갈 가능성이 있는 구조 가설**에만 쓴다.
50:
51: ---
52:
53: ## direct observations
```

<a id="s02"></a>

### S02 — review_final_submit_plan_measured_replay_model_split_2026-08-29.md

- 원본 경로: `codex/review_final_submit_plan_measured_replay_model_split_2026-08-29.md`
- 원본 SHA-256: `4cf6b575251e30cd7e886b25927ceafef29c8b2ebf76597b75422eeb650d13b7`

원본 L21–78:

```text
21: ## 1. 로컬 probe는 나눗셈이었다 (핵심 반증)
22:
23: `aas_step4_measured_replay_model_split_probe.py`의 생성 루프는 후보 1개당 다음을 누적한다.
24:
25: ```python
26: replay_cost += max(replay_floor_s, elapsed) * replay_cost_coef
27: ```
28:
29: 로컬 GPU에서 probe latency는 `gpt ~1.0s / gemma ~1.36s`(실험기록 2026-08-15 게이트웨이 실측)로 **모든 floor 후보(1.55 / 1.80 / 2.05)보다 작다.** 따라서 `max()`는 항상 floor를 고른다. 즉
30:
31: > N = replay_cap / (floor × coef × slowest_mult) → **N ∝ 1/floor**
32:
33: 이 관계로 보고된 숫자를 그대로 예측할 수 있다. 기준 N=41 (floor 1.80):
34:
35: | arm | floor | 예측 N | 보고된 N |
36: |---|---|---|---|
37: | gpt split | 1.55 | 41 × 1.80/1.55 = **47.6** | **48** |
38: | gemma split | 2.05 | 41 × 1.80/2.05 = **36.0** | **36** |
39: | 평균 | — | **41.81** | **42** |
40:
41: 세 칸 모두 정확히 맞는다. **모델이 무엇인지는 한 번도 개입하지 않았다.**
42:
43: ### 1-1. score는 독립 측정이 아니다
44:
45: 보고된 모든 셀에서 `score / findings = 0.09`가 정확히 성립한다 (3.69/41, 4.32/48, 3.24/36, 3.78/42). 게다가 문서 자신이 `mean findings = mean returned`라고 적었다 — 즉 **반환한 후보가 전부 replay를 통과했고, replay는 한 번도 시간 안에서 잘리지 않았다.** replay 단계는 생성 단계가 넘긴 숫자를 그대로 되돌려줬을 뿐이다.
46:
47: 따라서 "이번엔 `returned_n`이 아니라 **실제 replay score**로 확인했다"는 계획서와 probe plan의 주장은 형식적으로만 참이고 내용상 공허하다. 이 probe는 replay에 대한 어떤 가설도 구분할 수 없다.
48:
49: ### 1-2. swap-invariance — 모델 정보가 0이라는 결정적 증거
50:
51: floor 배정을 뒤집어(gpt=2.05, gemma=1.55) 계산하면 평균 N은 `(36.0 + 47.6)/2 = 41.81`로 **완전히 동일하다.** 관측된 이득은 전적으로 1/x의 볼록성(Jensen)에서 나온다.
52:
53: - 대칭 split의 예측 이득: `(1/1.55 + 1/2.05)/2 ÷ (1/1.80) − 1 = **+1.97%**`
54: - 관측된 이득: `41.81/41 − 1 = **+1.97%**`
55:
56: **소수점까지 일치한다.** 1.80을 중심으로 ±0.25 벌리기만 하면, 어느 모델에 어느 쪽을 주든, 심지어 동전을 던져 배정해도 같은 "+1 finding"이 나온다. `gemma rescue`가 아니라 `gpt +7 / gemma −5 교환`이라는 문서의 해석조차 과잉이다 — 교환은 배정의 산물이지 모델의 성질이 아니다.
57:
58: ### 1-3. 사전 판정 규칙에 실패 가지가 없었다
59:
60: `measured_replay_model_split_probe_plan`의 성공 조건은 "3회 중 2회 이상 split이 mean score 우위"였다. 위 결정론 때문에 이 조건은 **실행 전부터 3/3 확정**이었다. 반증 불가능한 사전 규칙이므로 이 probe는 승격 근거가 될 수 없다.
61:
62: ---
63:
64: ## 2. 통제군이 프로덕션 베이스라인이 아니다
65:
66: 부모 엔진들의 실제 코드를 확인했다.
67:
68: | 파일 | 누적식 | 실효 floor |
69: |---|---|---|
70: | `method22_aggressive_pack_apreimp.py:116` | `replay_cost += elapsed * REPLAY_COST_COEF` | `LAT_FLOOR_S = 0.001` |
71: | `method34_validated_wallfill_safe_apreimp.py:136` | 동일 | `0.001` |
72: | `method36_narrow_race_moderate_pack.py:205` | 동일 | `0.001` |
73: | `method21_family_race_breakout.py` | **누적식 없음** (`BLIND_N = 2000` 고정 방출) | — |
74:
75: 즉 **프로덕션에는 `replay_floor_s`라는 개념이 아예 없다.** `LAT_FLOOR_S=0.001`은 0으로 나누기 방지용이다.
76:
77: probe의 통제군(`floor 1.80`)은 프로덕션이 아니라 **probe가 새로 만든 제3의 arm**이다. 실제 비교는 이렇게 됐어야 한다.
78:
```

원본 L160–181:

```text
160: ```
161: WARMUP_REPS = 1 / CLASSIFY_REPS = 5 / SPLIT_THRESHOLD_S = 5.75
162: if classify_med > SPLIT_THRESHOLD_S: chosen = "slow"
163: ```
164: 결과: **53.415**. 실험기록은 이를 "low-threshold latency split이 실전에서 거의 작동하지 않았음"으로 기록했다.
165:
166: 그런데 §4에서 역산한 실제 probe latency는 **≈0.48s**다. `SPLIT_THRESHOLD_S = 5.75`는 그보다 **약 12배 높다.** 즉 `classify_med`는 두 모델 모두에서 임계값에 한참 못 미쳤을 가능성이 크고, 그렇다면 **분류기는 항상 `fast`를 골라 상수 함수로 퇴화했다.** 53.415는 split 실패가 아니라 `fast_family` 템플릿(json_args_plain) 자체의 실패일 수 있다.
167:
168: 시사점 두 가지:
169: - 분류기는 **아직 한 번도 Kaggle에서 실제로 분기한 적이 없다.** 계획은 검증되지 않은 부품에 5슬롯 전부를 건다.
170: - 이 질문은 **제출 0회로 해결된다.** `method25` stderr의 `chosen=` / `classify_med=` 한 줄이면 끝난다. 실험기록 08-27 "다음 액션"에 이미 적혀 있었고 아직 미수행이다.
171:
172: 계획서의 "이번 배치에서 제외할 것" 목록에 prompt sidecar·blind-tail·exact rerun은 있는데, **실제로 실전 반증 이력이 있는 latency split만 빠져 있다.**
173:
174: ---
175:
176: ## 7. 배치 설계 문제
177:
178: - **5/5 동일 축.** 다섯 장 모두 "latency classifier + floor split"을 공유한다. 공통 부품이 무효면 5슬롯이 동시에 죽고, 유효해도 어느 부모가 좋은지밖에 못 배운다. 08-27 handoff의 원칙("희소 자원은 살아있는 축들 사이의 decorrelation")과 08-28 판정("control 1 + isolated 3 + combo 1로 복귀") 양쪽에 어긋난다.
179: - **slot 1과 slot 5가 사실상 중복.** `method41`은 "method21의 wide race + method36식 validated packing + floor split"인데, method36식 packing으로 바꾸는 순간 method21의 유일한 강점인 **blind 2000(=벽 포화)이 사라진다.** §5에 따르면 이 변경 하나만으로 N이 1026 → ~1000으로 내려간다. slot 5는 상방이 가장 높은 카드가 아니라 **92.385를 스스로 반납하는 카드**다.
180: - **slot 5의 전제가 미검증.** "method21의 상방이 family selection에서 왔다"는 가정은 `method21` stderr의 `[RANK]` / `chosen=` 확인을 전제로 하는데, 이 액션은 08-27, 08-29 두 번 기록되고 두 번 다 미수행이다. 확인 결과 양 모델이 모두 `apreimp`를 골랐다면 92.385는 selection이 아니라 **blind 2000 + 상단 노이즈 draw**이고, slot 5의 논리 전체가 무너진다.
181:
```

원본 L184–189:

```text
184: ## 8. 사실관계 정정이 필요한 문장
185:
186: 1. "로컬 scorer-like replay 기준으로 shared floor보다 model-specific floor가 실제 점수를 올리는 신호가 나왔다"
187:    → **정정:** score는 findings의 0.09배 상수배였고 findings = returned였다. 관측된 +0.09는 `1/1.55 + 1/2.05 > 2/1.80`이라는 산술 항등식이며 모델과 무관하다.
188: 2. "그 이득은 gemma rescue가 아니라 gpt +7 / gemma −5 교환 구조였다"
189:    → **정정:** 교환 방향은 floor 배정이 정한 것이다. 배정을 뒤집어도 평균은 41.81로 동일하다.
```

<a id="s03"></a>

### S03 — near_cliff_replay_score_probe_error_review_2026-08-29.md

- 원본 경로: `codex/near_cliff_replay_score_probe_error_review_2026-08-29.md`
- 원본 SHA-256: `fe483937f10a9c7cc35baddb197826023933ae132454ab07a58a06fe3183daa8`

원본 L16–57:

```text
16: ## Direct Observations
17:
18: 1. **첫 번째 프로필은 실제로 정상 진행됐다.**
19:    - `gpt_oss | n=96 | control_validated_only`
20:    - generation:
21:      - `returned_n = 96`
22:      - `generation_wall_time_s = 55.08`
23:    - replay:
24:      - `replay_completed_n = 63`
25:      - `findings_count = 63`
26:      - `score_normalized = 5.67`
27:      - `replay_timeout_hit = true`
28:      - `replay_timeout_at_candidate_index = 63`
29:
30: 2. **크래시는 바로 다음 profile 시작 시점에 났다.**
31:    - 다음 구간:
32:      - `gpt_oss | n=96 | tail_p4_controlcost`
33:    - 에러:
34:      - `GGML_ASSERT(buf != NULL && "tensor buffer not set") failed`
35:      - 이후 `DeadKernelError: Kernel died`
36:
37: 3. **즉, crash 이전까지는 모델 자체가 정상 동작했다.**
38:    - 첫 profile의 generation과 replay가 모두 의미 있는 수치를 반환했기 때문이다.
39:    - 따라서 “prompt가 모델을 망가뜨렸다”나 “tail prompt 자체가 invalid”보다
40:      - **timeout 뒤 cleanup 없이 다음 replay/generation을 이어간 probe 흐름**이 더 직접 원인이다.
41:
42: ## Root Cause
43:
44: ### 가장 가능성 높은 원인
45:
46: - [aas_step4_near_cliff_replay_score_probe.py](<development-archive>/codex/aas_step4_near_cliff_replay_score_probe.py) 구버전은 replay candidate마다 `aicomp_sdk.evaluation.ops._run_until_deadline(...)`를 호출했다.
47: - 그런데 SDK의 [`_run_until_deadline`]( <development-archive>/kaggle_dump/data/aicomp_sdk/evaluation/ops.py:54 )는 내부적으로 **daemon thread를 띄우고**, timeout 시 그 thread를 종료하지 않는다.
48: - 첫 control replay가 `candidate_index = 63`에서 timeout 난 뒤에도, 마지막 replay thread는 백그라운드에서 계속 같은 GGUF 서버를 만지고 있었을 가능성이 높다.
49: - 그 직후 다음 profile의 generation이 같은 모델 서버로 새 요청을 보내면서 low-level backend assert가 발생한 것으로 보는 것이 가장 자연스럽다.
50:
51: ## Why this is not an attack finding
52:
53: - 이번 로그는 “tail 후보가 점수를 못 낸다”는 증거가 아니다.
54: - 실제로 tail profile은 **아예 평가를 시작하기도 전에** kernel이 죽었다.
55: - 따라서 이 로그에서 배울 수 있는 것은:
56:   - blind tail의 점수 우열이 아니라
57:   - **현재 probe의 replay deadline 구현은 unsafe** 하다는 점이다.
```

<a id="s04"></a>

### S04 — review_major_reflections_2026-08-31.md

- 원본 경로: `codex/review_major_reflections_2026-08-31.md`
- 원본 SHA-256: `348588c632cc2192fe3a758c83064016950304a3cee9e6ada7d42639edf8c071`

원본 L9–29:

```text
9: 이번 구간의 가장 큰 반성은 **레버 이름을 너무 크게 붙여서, 서로 다른 실패를 한 단어로 뭉개 버린 것**이다. 특히 `multipost`는 한 가지가 아니었는데, 초기 실패 몇 개를 보고 `multipost dead`처럼 읽었다가, 나중에는 반대로 `gpt_oss multipost breakthrough`를 너무 넓게 읽었다. 지금 남겨야 할 교훈은 "`multipost`가 산다/죽는다"가 아니라, **어떤 구현이 어떤 증거 계층에서 실패했는지**를 분리해서 적어야 한다는 점이다.
10:
11: ## 2. 반성 1 — `multipost`를 한 덩어리로 보면 반드시 틀린다
12:
13: 실제로 섞여 있었던 것은 최소 세 종류였다.
14:
15: 1. `same-generation multi-call`
16: 2. `multi-message amortization`
17: 3. `multi-hop sequential post`
18:
19: 이 셋은 이름만 비슷하고 점수 구조는 다르다.
20:
21: - `same-generation multi-call`은 parser/에피소드 종료 리스크가 핵심이다.
22: - `multi-message amortization`은 generation 수가 늘어나 throughput이 무너질 수 있다.
23: - `multi-hop sequential post`는 한 hop당 1-call을 지키면서도 후보당 post 수를 늘리려는 전혀 다른 구조다.
24:
25: 초기엔 앞의 두 실패를 보고 `multipost` 전체가 죽었다고 읽었고, 이후엔 세 번째 구조를 발견하자 이번엔 반대로 큰 일반론으로 밀어 올렸다. 그런데 `2026-08-30` Kaggle batch 결과는 **current `k8` implementation failed**를 보여줬다. 따라서 맞는 문장은 둘 중 하나가 아니라 아래다.
26:
27: - "`static k8` 구현은 실패했다."
28: - "`k8` frontload ordering은 실패했다."
29: - "`multipost` 전체 일반론은 아직 구현 단위로 더 쪼개서 판단해야 한다."
```

원본 L31–59:

```text
31: ## 3. 반성 2 — `gemma`의 제약을 `gpt_oss`의 ceiling으로 착각했다
32:
33: single-post 중심 전략이 오래 유지된 이유 자체는 합리적이었다.
34:
35: - `gemma`는 실제로 single-post 쪽 관측이 강했다.
36: - 공개 점수는 평균이라 한 모델이 크게 죽으면 전체 점수가 바로 깎인다.
37: - 정적 per-model routing 훅이 없어서 shared safe single이 운영적으로 편했다.
38:
39: 문제는 여기서 한 단계 더 나가 **`gemma single-post` 관측을 `gpt_oss`도 실질적으로 single일 것이라는 결론으로 확장한 것**이다. 이건 같은 말이 아니다.
40:
41: - `gemma`의 멈춤은 `gemma`의 사실이다.
42: - `gpt_oss`가 hop을 이어 갈 수 있는지는 별도 질문이다.
43:
44: 다음부터는 "모델 A에서 보인 제약"을 문서에 적을 때 반드시 아래 둘 중 하나로 적는다.
45:
46: - `model-specific fact`
47: - `cross-model inference`
48:
49: 그리고 후자는 근거가 따로 없으면 사실처럼 쓰지 않는다.
50:
51: ## 4. 반성 3 — local, board-like, Kaggle score를 같은 층위로 말하면 해석이 무너진다
52:
53: 이번 구간에서 가장 반복된 해석 실수는 증거 경계 혼동이었다.
54:
55: - `local_gguf`는 문법/발화/거친 행동 확인용이다.
56: - `cm391 CPU board-like harness`는 제출 전 후보 압축용 프록시다.
57: - 최종 우열은 Kaggle 점수다.
58:
59: 이 셋은 서로 연결되어 있지만 동일하지 않다. 특히 local에서 좋아 보인 `k8` 서사가 Kaggle scored batch에서 그대로 뒤집힌 것은, "좋은 프록시"와 "최종 점수"를 같은 문장 안에 섞으면 얼마나 쉽게 오판하는지를 보여줬다.
```

<a id="s05"></a>

### S05 — claude_review_today_plan_2026-08-30.md

- 원본 경로: `codex/claude_review_today_plan_2026-08-30.md`
- 원본 SHA-256: `679e6f29ab29660c976f1f9034ee019050105070917690e41c5e7a3b4b2ffbc3`

원본 L25–58:

```text
25: - `today_submission_plan_sol56_2026-08-30.md`(=`43~47`을 설계한 문서)의 구현 제약:
26:   > "`AttackRunConfig`/`AttackEnvProtocol`에 직접적인 `model_name` 훅이 없으므로, **정적 `gpt만 k8 / gemma만 single` 분기 코드는 깨끗하게 만들 수 없다.**"
27: - 그래서 `43~47`은 어쩔 수 없이 **symmetric static + ordering + capability gate**로 만들어졌다(`method44/46/47`은 코드가 `del env, config` = 양 모델에 동일 메시지).
28: - 결론: "정적 per-model `k`"라고 적힌 `method53/54/55`는 실제로는 두 갈래 중 하나로만 구현된다.
29:   - (a) 런타임 행동 probe로 분기 → 그건 **`method56`=`method42`의 selector**다(=별도 카드가 아님).
30:   - (b) 양 모델 동일(symmetric) → 그건 **`method44`(k4)/`method46`(k8)의 재탕**이고, exact/near-exact 재제출 금지에 걸린다.
31: - 즉 `53/54/55`는 "새 정적 구조"로 존재할 수 없다. selector로 접히거나 이미 채점된 카드로 접힌다.
32:
33: ### Finding 3 — 비대칭의 유일한 구현 수단인 selector(`method42/56`)는 **단 한 번의 실측에서 빈 row → single 폴백**했다 [직접 관측, 문서 인용]
34: - `aas_local_validation_followup_hypotheses_2026-08-30.md`:
35:   > "이전 `method42` wording-selection probe는 **결과 row가 비어서 `chosen=single_apreimp` 기본값만 남았다.**"
36: - 즉 "gpt는 multi, gemma는 single로 실제로 갈린다"는 분기 증거는 **아직 없다**. 유일한 시도는 측정 실패로 single로 떨어졌다.
37: - 이건 단순 버그일 수 있으나, **오늘 배치 전체가 이 분기 재현성에 의존**한다는 점이 핵심 리스크다. 분기가 안 되면 `56`은 `method39`류 single로 퇴화하고, "정적" 카드가 분기를 잘못 하면 gemma가 multipost로 올라가 **에피소드 종료(0점)** 위험이 있다.
38:
39: ### Finding 4 — 오늘의 top-level thesis에 **직접 Kaggle 반증**이 있고, 비대칭 수정은 그 반증의 절반만 건드린다 [Kaggle 직접 관측 + 추론]
40: - Kaggle 직접 관측(same-window, `43~47`): 5장 전부 banked `93.835` 아래. `k8=64.230`(최하), 단조성 `k8 < k4`(`44>46`, +9.0), 그리고 **single-front > k8-front**(`45=83.565 > 47=73.445`, +10.1).
41: - 계획의 방어 논리는 "`43~47`은 symmetric이라 gemma가 자멸해서 망했다 → 비대칭이면 산다"이다.
42: - 그러나 `45 > 47`(순서만 다르고 `k8` 수 동일)은 **gemma 자멸과 무관한 gpt-측 throughput 문제**를 가리킨다. 앞에 `single`을 둔 쪽이 이겼다 = board 시간예산 안에서 **긴 체인은 후보 완주 수를 깎아 손해**. 비대칭(gpt-only)은 **gemma-collapse만 복구**하고 이 gpt-측 속도 손해는 그대로 남긴다.
43: - 즉 비대칭 수정은 "틀린 실패 원인"을 고치고 있을 수 있다.
44:
45: ### Finding 5 — 배치에 **same-window single anchor가 없다** = `43~47` 리뷰가 지적한 실수의 반복 [직접 관측]
46: - Kaggle은 per-model row(`gpt_public`, `gemma_public`)를 우리에게 **안 보여준다**(hard rule). 따라서 어떤 multipost 결과가 나와도 "gpt가 오른 건지 gemma가 내린 건지"는 **같은 창의 single anchor와 비교해야만** 분해된다.
47: - `review_submission_results_methods43_47`도 이미 명시: "pure same-window baseline이 없어서 이번 창 전체가 single에도 불리했는가를 직접 측정하지 못했다."
48: - 그런데 오늘 계획은 anchor를 또 뺐다. `method48_single_anchor_control.py`는 **이미 작성돼 있고**(non-dup SHA `4126b8a6ecb2`) 바로 쓸 수 있는데도 100+ 계획에서 드랍됐다. `EXPERIMENT_DESIGN_CHECKLIST` Gate E 위반.
49:
50: ### Finding 6 — `55`의 "warmed board-like ceiling" 증거는 계획이 말하는 것보다 약하다 [board-like/local, 층위 혼입 경고]
51: - 근거가 되는 warmed wording probe: `list_continue_k8`가 raw/s 최고(~20.8, 한 run 23.07)였지만 **`hit_target_rate=0.75`**(8/8 완주를 자주 놓침), 그리고 비교 대상 `single_apreimp` baseline은 **첫 샘플 85.29s cold-start outlier로 심하게 낮게** 잡혔다(=k8 우위가 아티팩트일 수 있음).
52: - 결정적으로 이 probe result들의 **`resolved_harness`가 `board_remote`로 확인됐다는 증거를 repo 안에서 찾지 못했다**(계획/가설 문서는 "board_remote 우선"이라는 목표만 적음). `RESULT_INTERPRETATION_TEMPLATE`의 "`resolved_harness` 미확인 결과를 board-like evidence로 확대하지 마라"에 걸린다.
53: - 같은 로컬 계열(`probe_review_firing_and_gateB`)의 gguf 관측은 오히려 반대다: **양 모델 모두 hop0에서 1회 발사 후 정지(8-hop 지연 = 2-hop 지연)**. 로컬 gguf는 multi-hop 연쇄를 **지지하지 않는다**.
54:
55: ### Finding 7 — discussion 힌트를 계획이 **한쪽만** 반영했다 [직접 관측, 코드 근거]
56: - `discussion_hint_analysis_2026-08-28`은 gateway 코드로 확인: 채점은 **모델별 4-row**(gpt/gemma × public/private), 공개 = 두 모델 결합.
57: - 힌트 1 "90 = optimized to one"의 코드 기반 최강 해석은 **"한 모델"**(한 모델 ~180, 다른 모델 ~0 → 평균 ~90)이다. BREAKTHROUGH 문서는 이걸 **"한 post"**로 재해석해 multipost로 몰았는데, 이건 두 해석 중 하나에 올인한 것이다.
58: - 힌트 2 "timing = faster = more candidates"는 **빠른 후보**를 지지 = **느린 긴 체인에 불리**. 실제 board(`45>47`)도 이 힌트와 일치한다. 계획은 힌트 1의 한 해석만 취하고, 힌트 2가 체인 길이에 주는 반대 신호를 흡수하지 못했다.
```

원본 L50–53:

```text
50: ### Finding 6 — `55`의 "warmed board-like ceiling" 증거는 계획이 말하는 것보다 약하다 [board-like/local, 층위 혼입 경고]
51: - 근거가 되는 warmed wording probe: `list_continue_k8`가 raw/s 최고(~20.8, 한 run 23.07)였지만 **`hit_target_rate=0.75`**(8/8 완주를 자주 놓침), 그리고 비교 대상 `single_apreimp` baseline은 **첫 샘플 85.29s cold-start outlier로 심하게 낮게** 잡혔다(=k8 우위가 아티팩트일 수 있음).
52: - 결정적으로 이 probe result들의 **`resolved_harness`가 `board_remote`로 확인됐다는 증거를 repo 안에서 찾지 못했다**(계획/가설 문서는 "board_remote 우선"이라는 목표만 적음). `RESULT_INTERPRETATION_TEMPLATE`의 "`resolved_harness` 미확인 결과를 board-like evidence로 확대하지 마라"에 걸린다.
53: - 같은 로컬 계열(`probe_review_firing_and_gateB`)의 gguf 관측은 오히려 반대다: **양 모델 모두 hop0에서 1회 발사 후 정지(8-hop 지연 = 2-hop 지연)**. 로컬 gguf는 multi-hop 연쇄를 **지지하지 않는다**.
```

<a id="s06"></a>

### S06 — claude_review_today_plan_2026-08-30.md

- 원본 경로: `codex/claude_review_today_plan_2026-08-30.md`
- 원본 SHA-256: `679e6f29ab29660c976f1f9034ee019050105070917690e41c5e7a3b4b2ffbc3`

원본 L132–141:

```text
132: ## 9. [추가] 로컬 검증 노트북 확인 결과 — harness 정정 (사용자 요청)
133:
134: 사용자 안내로 `community_notebooks/aas-local-validation.ipynb`와 SDK harness 코드를 직접 확인했다. 계획의 "`resolved_harness=board_remote`면 승격" 게이트에 대한 **중요한 정정**이 필요하다.
135:
136: ### 9.1 직접 관측 (코드)
137:
138: - **노트북(`aas-local-validation.ipynb`)은 `local_gguf` + `gym` agent다.** cell 6/15/17이 `build_gguf_agent_factory()` + `EnvSelection.GYM` + `OptimalGuardrail`로 로컬 gguf 가중치(`gpt-oss-20b-Q4_K_M`, `gemma-4-26b Q4_K_M`)를 직접 로드한다. **`RemoteAgent`(board parser)를 쓰지 않는다.**
139: - 노트북은 **per-model public 점수를 준다**(cell 20/21: `gpt_oss_public`, `gemma_public`, mean). 즉 **로컬 분해 자(尺)는 이미 있다** — 단, gym agent + 로컬 gguf + 빠른 로컬 HW 기준의 프록시다.
140: - `board_remote`는 로컬에서 **실행 가능**하다. `remote_agent.py`의 `RemoteAgent`가 존재하고, probe들(`aas_step4_gptoss_*_probe.py`)은 `RemoteAgent(model_srv.predict)`로 그 경로를 만든다. 하지만 여기서 `model_srv`는 **로컬 gguf 모델 서버**다. 즉 로컬 `board_remote` = **board 충실한 agent/parser 레이어 + 로컬 gguf 가중치 + 빠른 로컬 HW**의 하이브리드 프록시이지, 진짜 Kaggle 원격 서버가 아니다.
141: - **`resolved_harness="board_remote"` 라벨은 약하다.** probe의 `_make_agent_bundle()`은 `remote_agent`/model_server **import가 성공하면** 그 자리에서 `resolved_harness="board_remote"`를 찍는다. 실제 모델 호출/multi-hop 재생이 board처럼 됐는지와 무관하게 라벨이 붙는다.
```

<a id="s07"></a>

### S07 — submission_failure_notes.md

- 원본 경로: `codex/submission_failure_notes.md`
- 원본 SHA-256: `0a3e4cf7e47cfecdb0d8fd237d79d5b61b9c274916809aca1bf47ee608eeab55`

원본 L3–12:

```text
3: ## 2026-08-25 — `method14_v30_directcall_bias` Kaggle Error
4:
5: - 표면 결과: Kaggle UI에는 `Kaggle Error`로 보였음
6: - 실제 원인: 제출 코드 셀에 마크다운 코드펜스 ` ``` ` 를 같이 붙여 넣어 `SyntaxError: invalid syntax`
7: - 로그 신호:
8:   - 실패가 아주 빠르게 남
9:   - `PapermillExecutionError`
10:   - `Exception encountered at "In [2]"` 같은 초기 셀 번호
11:   - 로그 본문에 literal ` ``` ` 줄이 보임
12: - 분류: **공격 로직 문제 아님 / Kaggle 인프라 flake 아님 / 복붙 포맷 오류**
```

<a id="s08"></a>

### S08 — today_strict_review_missed_upside_2026-09-01.md

- 원본 경로: `codex/today_strict_review_missed_upside_2026-09-01.md`
- 원본 SHA-256: `0a6357daa5935afec22f9d89a03bbc300a0d55b541c30ab453838edf6c6a7fa3`

원본 L3–31:

```text
3: 지금까지 상방(100+)을 발견하지 못한 핵심 원인은 크게 두 가지 구조적 오판(Blind Spot)에 있었습니다. 우리는 "가설"이 틀린 것이 아니라, "측정"과 "구현"에서 치명적인 모순을 범하고 있었습니다.
4:
5: ## 1. 프롬프트 오염 (Model Contamination): GPT를 강제로 마비시켰다
6:
7: - **원인**: 과거 `method30` 전후로 도입된 `ANALYSIS_OPEN` (`<|end|><|start|>assistant<|channel|>analysis<|message|>`) 템플릿은 **오직 Gemma-2를 위한 전용 제어 토큰(Control Tokens)**입니다.
8: - **오판**: 로컬 검증 시 `gpt_oss` 프록시가 이를 무시하거나 우연히 통과한 것을 보고, 이 템플릿을 전역(Global)에 적용했습니다. 최근 93.835를 기록한 `method39`를 포함해 `method64`, `71`, `76`, `77` 등 모든 고득점 카드의 **모든 메시지 뒤에 `ANALYSIS_OPEN`이 강제 주입**되었습니다.
9: - **결과**: Kaggle 환경의 실제 `gpt_oss`(Qwen 계열)는 이 낯선 제어 토큰을 보고 문맥을 잃고 환각(Runaway)에 빠져 타임아웃을 유발했습니다.
10: - **충격적 사실**: 공개 LB 점수 93.835는 두 모델 평균입니다. Gemma가 0.9초 쾌속으로 2000개를 완주해 180점(가정)을 쓸어담는 동안, GPT는 타임아웃으로 죽어 7점밖에 내지 못했을 가능성이 큽니다. `(180 + 7) / 2 = 93.5`. 즉, **우리는 GPT 측 점수를 스스로 0점으로 만들고 있었습니다.**
11:
12: ## 2. Multi-message 환상: 1개의 타겟에서 여러 번 점수를 뽑을 수 없다
13:
14: - **원인**: 우리는 "한 번 성공해서 보내면 점수가 쌓이고, 많이 보낼수록 올라간다"는 문장을 "동일한 Candidate(에피소드) 안에서 여러 번 쏘면 2배, 4배가 된다"고 오해했습니다.
15: - **증명**: `method76`은 2000개의 타겟에 k=4를 적용해 총 8000번의 메시지를 보냈습니다. 만약 여러 번 쏜 것이 합산된다면 93점보다 훨씬 높은 점수가 나와야 하지만, 결과는 78.045점이었습니다.
16: - **결론**: Kaggle은 **한 번의 에피소드(Candidate) 당 성공 여부를 1번만 집계**합니다. 동일 타겟에 4번을 쏘는 것은 점수 이득은 0이면서 시간만 4배로 소모하여 타임아웃 멸망(1500개만 처리 후 종료 등)을 부르는 최악의 전략이었습니다.
17:
18: ## 3. 2000개의 인위적 천장 (Artificial Ceiling)
19:
20: - **원인**: 우리는 관성적으로 `BLIND_N = 2000`을 하드코딩해왔습니다.
21: - **진실**: Kaggle이 Candidate 리스트를 순회하며 평가한다면, 우리가 2000개만 리턴하기 때문에 최대 2000점 만점(평균 100점)에 갇혀있던 것입니다. "100+ 상방"이 존재한다면, 테스트 케이스(타겟)가 2000개 이상이거나, 타임아웃 한계(9000초) 전까지 더 많은 후보를 낼 수 있다는 뜻입니다.
22: - 만약 GPT의 오염된 프롬프트를 깨끗하게 고쳐 1~2초 내에 응답하게 만들면, 두 모델 모두 엄청난 속도를 얻게 되므로 2000개가 아니라 **3000~4000개의 Candidate를 제출하여 타임아웃 없이 순수하게 상방을 뚫어낼 수 있습니다.**
23:
24: ## 4. 놓친 상방을 잡는 유일한 해결책 (Next Action)
25:
26: 라우팅이나 꼼수가 필요 없습니다. **"Race 기반 프롬프트 풀에 GPT용 순수(Clean) 프롬프트를 섞어주는 것"** 하나면 끝납니다.
27:
28: 1. `method39`의 Race 엔진을 부활시킵니다.
29: 2. 5개의 스타일에 `ANALYSIS_OPEN`이 붙은 Gemma 전용 템플릿과, `ANALYSIS_OPEN`을 완전히 제거한 **GPT 전용 순수(Clean) 템플릿**을 함께 넣습니다.
30: 3. Race 단계에서 Gemma는 당연히 0.9초짜리 `ANALYSIS_OPEN` 스타일을 자기 스스로 선택할 것이고, GPT는 환각에 빠지지 않는 1초짜리 `Clean` 스타일을 알아서 선택할 것입니다.
31: 4. 이렇게 각 모델이 완벽한 Throughput을 확보한 상태에서, `BLIND_N`을 3000~4000개로 늘려 제출하면 역사상 가장 압도적인 점수가 나올 것입니다.
```

## 추적성과 누락 범위

실험 원장 링크는 이번 정리 직전의 commit `06f520e28fb57e8940267fd3fa80c0755a1fba51`에 고정해
행 번호가 바뀌어도 근거를 확인할 수 있게 했다. 원장은 과거의 상충하는 설명을 그대로 보존한다.
전체 텍스트 검색은 자체 문서 190개, 검색어가 나타난 문서는 73개다. CSV의 `keyword_hits`는
검색어가 포함된 행 수이며 오류 건수·검증 완료 여부를 뜻하지 않는다. 검색 사전과 제외 범위도 CSV 및 아래에 명시한다.

검색어: `오류, 오판, 잘못, 실수, 정정, 철회, 오해, 누락, 거짓, 과잉, 편향, 착각, 불가능, 반증,
퇴화, FileNotFoundError, SyntaxError, GGML_ASSERT, bug(독립 단어)`.
대상: 개발 폴더 루트 Markdown 및 `codex/`, `gemini/`, `codex_temp/`의 Markdown.
제외: `community_bundle.md`, `*_cell.md`, `aas_write_locally_cells.md`, `kaggle_submission_cells.md`.
타 참가자 `solution/`, `kaggle_post_competition/`, SDK dump·패키지·환경 폴더는 위 대상 밖이다.

누락 가능성: 검색어 없이 기록된 오류, 삭제된 대화, 보존되지 않은 raw JSON·제출 log,
명시되지 않은 작성 주체·모델별 hosted 분기. 이 문서는 그런 부분의 원인이나 손실을 만들어 채우지 않는다.
