Git 명령어
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
git tag -a v0.0.0.3 -m "Build Version 0.0.3"

태그 추가
https://minsone.github.io/git/git-addtion-and-modified-delete-tag


# Git 변경사항 되돌리기 or 버리기

## 파일 되돌리기
- git checkout -- [filename]

## 모두 되돌리기
- git restore .

# Git Branch

## 체크아웃
- git checkout [브랜치명]

## 삭제
- git branch -d 브랜치명


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

origin master
origin: 원격저장소
master: 지역저장소의 브랜치
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