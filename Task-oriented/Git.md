# 목차
- [목차](#목차)
- [Git 명령어](#git-명령어)
  - [스태시](#스태시)
    - [스태시 저장](#스태시-저장)
    - [스태시 내용 확인](#스태시-내용-확인)
    - [스태시 불러오기](#스태시-불러오기)
    - [스태시 제거](#스태시-제거)
  - [로그](#로그)
    - [기본 조회](#기본-조회)
    - [시간 기준 조회](#시간-기준-조회)
    - [요약 조회](#요약-조회)
    - [포맷 지정 조회](#포맷-지정-조회)
    - [아스키 그래프 조회](#아스키-그래프-조회)
  - [브랜치](#브랜치)
    - [생성](#생성)
    - [추가](#추가)
    - [병합](#병합)
    - [삭제](#삭제)
- [Git 변경사항 되돌리기 or 버리기](#git-변경사항-되돌리기-or-버리기)
  - [파일 되돌리기](#파일-되돌리기)
  - [모두 되돌리기](#모두-되돌리기)
- [git stash pop \[stash@{index}\]](#git-stash-pop-stashindex)
- [git stash apply \[stash@{index}\]](#git-stash-apply-stashindex)
  - [저장소 종류](#저장소-종류)
    - [origin master](#origin-master)
- [병합 취소](#병합-취소)
- [미추적](#미추적)

# Git 명령어
## 스태시
- 진행중인 현재 Task에 대한 파일 변경 내용을 임시로 기록하는 영역
- 진행 중인 현재의 Task와는 연관성이 떨어지는 다른 Task가 발생하였을 때 현재 Task를 임시로 저장하는 용도로 사용
- [참고사이트](https://mine-it-record.tistory.com/651)

### 스태시 저장
``` bash
git stash push -m "message"
git stash save "message"
git stash # Save 생략
```

### 스태시 내용 확인
- 저장된 Task 목록 확인
``` bash
git stash show
git stash show -p
git stash show stash@{인덱스번호} # stash@{2}에서 2는 index를 의미 stash@{index}
git stash show stash@{인덱스번호} -p  # -p 상세한 내용 확인

git stash list
git stash clear
git stash pop
```

### 스태시 불러오기
- Pop
  - git stash pop stash@{인덱스번호}
  - 인덱스번호 지정하지 않으면 최근 저장된 Task를 불러옴
  - Task를 불러온 후 해당 Task는 목록에서 사라짐
``` bash
git stash pop
git stash pop stash@{인덱스번호}
```
- Apply
  - git stash apply stash@{인덱스번호}
  - Task를 불러온 후에도 해당 Task는 목록에 유지됨

``` bash
$ git stash apply
$ git stash apply stash@{인덱스번호}
```
- --index 옵션
  - 스태시 영역에 올라간 파일의 상태까지 불러옴
``` bash
git stash pop --index
git stash apply --index
```

### 스태시 제거
- git stash drop [stash@{index}]
- index 생략시 최근 Task만 삭제
``` bash
git stash drop
git stash drop stash@{인덱스번호}

# 목록 모두를 삭제
git stash clear
```

## 로그
### 기본 조회
``` bash
# 커밋 이력 상세 조회
git log

# 커밋 이력 중 커밋 ID와 타이틀 메시지만 조회
git log --oneline

# 모든 브랜치 커밋 이력 조회
git log --oneline --decorate --graph --all

# 특정 파일의 변경 커밋 조회
git log --index.html

# diff 를 보여줌
git log -p

# 최근 두 개의 diff를 보여줌
git log -p -2
```

### 시간 기준 조회
- 시간을 기준으로 특정 시점 이후에 생성된 커밋만 보여줌
```bash
git log --since=2.weeks
git log --since="2 years 1 day 3 minutes ago"
```

### 요약 조회
- 파일의 변경/추가/삭제 되었는지 요약
```bash
git log --stat
```

### 포맷 지정 조회
- 출력 내용 Commit 체크섬과 메시지만 출력
```bash
git log --pretty=oneline
# git log --pretty=oneline 출력 예시
# -------------------------------------------------------------
# ca82a6dff817ec66f44342007202690a93763949 changed the version number
# 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7 removed unnecessary test
# a11bef06a3f659402fe7563abf99ad00de2209e6 first commit
# -------------------------------------------------------------
```
- 출력  포맷 정의
```bash
git log --pretty=format:"%h - %an, %ar : %s" 
# --pretty=format:"%h - %an, %ar : %s"  출력 예시
# -------------------------------------------------------------
# ca82a6d - Scott Chacon, 6 years ago : changed the version number
# 085bb3b - Scott Chacon, 6 years ago : removed unnecessary test
# a11bef0 - Scott Chacon, 6 years ago : first commit
# -------------------------------------------------------------
```
  - 자주 쓰는 출력 포맷
    - **%H**: 커밋 해시
    - **%h**: 짧은 길이 커밋 해시
    - **%T**: 트리 해시
    - **%t**: 짧은 길이 트리 해시
    - **%P**: 부모 해시
    - **%p**: 짧은 길이 부모 해시
    - **%an**: 저자 이름
    - **%ae**: 저자 메일
    - **%ad**: 저자 시각. 형식은 –-date=옵션 참고
    - **%ar**: 저자 상대적 시각
    - **%cn**: 커밋한 사람(커미터) 이름
    - **%ce**: 커미터 메일
    - **%cd**: 커미터 시각
    - **%cr**: 커미터 상대적 시각
    - **%s**: 요약
 
### 아스키 그래프 조회
- --graph는 아스키 그래프 보여줌
  - 브랜치 여러 개일 때 직관적으로 이해할 수 있음
```bash
git log --pretty=format:"%h %s" --graph
```

## 브랜치
### 생성
``` bash
# 새 브랜치 생성하기
git branch [새로운 브랜치명]

# 생성된 브랜치로 전환하기
git checkout [새로운 브랜치명]
```

### 추가
- Remote Repo에 생성한 브랜치 추가
``` bash
# 파일 추가
touch new-file.js

# 수정사항 커밋
git add .
git commit -m "message"

# 새 원격 브랜치로 푸시
git push --set-upstream origin [새로운 브랜치명]
```

### 병합
- 모든 Remote Repo 가져오기
``` bash
git fetch origin
```
- 체크아웃 가능한 브랜치 목록 보기
  - 원격 브랜치에는 remotes/origin이라는 접두사가 붙음
``` bash
git branch -a
```
- Remote Repo 브랜치 변경이력 병함
  - 원격 브랜치에는 직접 작업할 수 없음
  - 변경사항 추가하기 위해서는 원격 브랜치의 복사본 필요
``` bash
# 1. [브랜치명]의 새로운 브랜치를 생성
# 2. 새 브랜치로 체크아웃
# 3. 변경 이력을 origin/[브랜치명]에서 가져옴
git checkout -b [새 브랜치명] origin/[브랜치명]
```
- 이후 커밋은 브랜치를 지정할 필요없이 git push 명령어로 실행 가능
``` bash
touch new-file.js
git add .
git commit -m "새 파일 추가"
git push
```
### 삭제
``` bash
git branch -d [브랜치명]
```


- log 종료하려면 Q를 누르면 됨

git tag 붙이기

Lightweight 태그
git tag v0.0.0.3

Annotated 태그
git tag -a v0.0.0.3 -m "Build Version 0.0.3"

태그 추가
https://minsone.github.io/git/git-addtion-and-modified-delete-tag


# Git 변경사항 되돌리기 or 버리기

## 파일 되돌리기
- git checkout -- [filename]

## 모두 되돌리기
- git restore .




---

GIt 명령어
Stash
https://mine-it-record.tistory.com/651
git stash show
git stash list
git stash clear
git stash pop

git stash push -m "message"
git stash save "message"

# git stash pop [stash@{index}]

$ git stash pop
$ git stash pop stash@{2}

# git stash apply [stash@{index}]

$ git stash apply
$ git stash apply stash@{2}

Log
git log //커밋 이력 상세 조회
git log --oneline //커밋 이력 중 커밋 ID와 타이틀 메시지만 조회
git log --oneline --decorate --graph --all // 모든 브랜치 커밋 이력 조회
git log --index.html // 특정 파일의 변경 커밋 조회
git log -p // diff 를 보여준다
git log -p -2 // 최근 두 개의 결과만 diff를 보여준다./

git log --pretty=oneline

git log --pretty=format:"%h - %an, %ar : %s" // 나만의 포맷으로 (아래 참조)
https://kin3303.tistory.com/294

git log --pretty=format:"%h %s" --graph // --graph는 아스키 그래프 보여줌

=> Q 누르면 꺼짐

git tag 붙이기

Lightweight 태그
git tag v0.0.0.3

Annotated 태그

git reset —hard origin/develop

git tag -a v0.0.0.3 -m "Build Version 0.0.3"

태그 추가
https://minsone.github.io/git/git-addtion-and-modified-delete-tag

git checkout

git 브랜치 삭제
git branch -d 브랜치명

git fetch upstream
git merge upstream/main

git cherry-pick

## 저장소 종류
### origin master
- origin: Remote Repo(Repository)의 URL에 대한 alias
- Remote Repo를 처음 생성하면 자동으로 별칭 origin, 초기 상태 브랜치 master가 만들어짐
- origin/master: Remote Repo의 master 브랜치
- master: 지역저장소의 브랜치
```bash
# 원격 레포에 master 브랜치를 생성하고,
# 로컬 레포의 master 브랜치 내용을 원격 레포의 master 브랜치에 보냄
git push -u origin master

# Remote Repo의 origin/master의 내용을 로컬 master로 Fetch
git fetch origin master

git checkout develop
git pull
```
origin/master: 원격저장소의 브랜치 = origin이라는 원격저장소에 있는 master브랜치의 local복사본
git fetch origin master: 원격저장소의 origin의 master를 패치

origin/devlep이 위에 있고 develop이 아래에 있으면,
develop 브랜치에 대한 내 로컬의 복사본이 최신화가 되지 않았음을 의미
pull 땡기면같아짐

https://jmjmjm.tistory.com/60

reset: HEAD의 위치를 현재 커밋에서 과거나 미래로 이동할 수 있음
reset 옵션 세 가지: --soft, --mixed, --hard

- -soft
- HEAD가 특정 커밋(과거 또는 미래)을 새롭게 가리킴
- working 디렉토리와 staging Area는 아무런 영향을 받지 않음
- -mixed
- staging area도 해당 커밋의 모습과 동일하게 변경
- 현재 작업중인 working directory에 아무런 영향 받지 않음
- -hard
- staging area와 현재 작업 중인 working directory도 해당 커밋의 모습과 동일하게 변경


제가 Git을 어설프게 알고 있어서 정리를 좀 해봤습니다.
Sourcetree를 사용하고 있어서 이 명령어가 얼마나 유용할 지는 모르겠지만, 지식을 공유하는 차원에서 공유드려 봅니다.


참고한 사이트
https://mine-it-record.tistory.com/651
https://niklasjang.tistory.com/27
https://seonkyukim.github.io/git-tutorial/git-log/#google_vignette
https://www.freecodecamp.org/korean/news/git-remote-branch-checkout/



























새로운 브랜치 생성
git push origin [새로운 브랜치명]

생성한 브랜치에 최초 Push 할 때,
git push로는 아래 메시지 발생

fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream

기본 브랜치 설정
git push --set-upstream origin [새로운 브랜치명]
https://healthcoding.tistory.com/18


git checkout feature/v1.7
로 체크아웃해서 내용 변경 후

git checkout master
로 다시 체크아웃하고

git checkout feature/v1.7
로 체크아웃하고 돌아와도 feature/v1.7의 변경 내용은 살아있음


master 브랜치에서 test 브랜치를 merge

git checkout master
git merge test

# 병합 취소
머지 작업 취소
git merge --abort


# 미추적
.gitignore 적용
git rm -r --cached .

1. 작성 패턴
- #로 시작하는 라인은 주석, 무시
- 표준 glob 패턴을 따름
- 디렉토리는 끝에 슬래시(/)를 사용해 표현
- 느낌표(!)로 시작하는 경우 예외로 처리

파일 하나만 무시
fileName,txt

특정 디렉토리의 특정 파일 무시
fileDirectory/fileName.txt

특정 디렉토리의 모든 파일 무시
fileDirectory/

특정 확장자 가진 모든 파일 무시
*.txt

현재 경로의 fileName 무시
/fileName.txt

특정 경로의 모든 fileName 무시
fileDirectory/**/fileName.txt

예외
!fileName.txt

https://growingarchive.tistory.com/244



Unstaged된 파일 비교
git diff

Stagin Area에 있는 파일 비교 => git add로 변경사항을 추가하였다면 이것으로 비교해야 됨
git diff --staged
git diff --cached

브랜치간 비교
git diff [브랜치명1] [브랜치명2]
git diff [브랜치명1] origin[브랜치명2]

커밋 간 비교
git diff [커밋 해시값1] [커밋 해시값2]
-> 커밋 해시값은 git log로 확인 가능

커밋 사이를 비교
git diff [커밋 해시값1]...[커밋 해시값2]

git diff 531c1d06412a57ef050d6372e36d6921169495f4 af35084e7f9fce61ddcede3545f56802b30f3d62

git diff 531c1d06412a57ef050d6372e36d6921169495f4...af35084e7f9fce61ddcede3545f56802b30f3d62


