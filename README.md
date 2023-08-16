# cufeed-scrapper

## 사용 기술
- Python 3.10.x
- Framework: Django 4.1.7
- Database: MariaDB 15.1
- Infra: AWS EC2 t2.nano instance x 1 (Running MariaDB)

## 전체적인 서비스의 구도
- 내가 보고 싶은 뉴스의 키워드를 구독형으로 등록한다.
- 등록된 키워드로 뉴스가 새로 등록될때마다 알림을 보내준다.
- 내가 구독 중인 키워드를 타인이 볼 수 있도록 공개 할 수 있도록 공간을 제공한다.
- 타인이 등록한 키워드를 자신도 구독할 수 있는 기능을 제공한다.
- 가장 많이 구독한 키워드, 가장 많이 검색한 키워드, 가장 많은 키워드를 등록한 유저 등 랭크 보드를 제공한다.
- 뉴스 RSS 피드를 시작으로 여러 컨텐츠로 확장한다.

## cufeed-scrap-server 역할
뉴스 검색어를 API로 요청받아 데이터를 쌓는 역할

### 적재 중인 데이터
- 뉴스 타이틀
- 뉴스 링크 주소
- 뉴스 적재 시 사용된 키워드
- 뉴스 적재 시각

### 추후 얻고자 하는 데이터
- 어떤 키워드로 뉴스를 검색하는가?
- 어떤 키워드의 뉴스가 얼마나 올라오는가?
- 어떤 사람이 어떤 키워드를 주로 구독하는가?

### AS-IS
- 서비스에 달려있는 API 엔드포인트를 직접 호출해서 DB 데이터 적재 
- Endpoint: /api/{vendor}/{keyword} 
- vendor: 뉴스 공급업체 (현재는 google만 유효)
- keyword: 뉴스 검색 키워드

### TO-BE (phase-1)
- DB Queue를 구현하여 Batch를 돌려 적재하는 방식으로 개선
- DB Queue에 적재하는 서비스는 cufeed-service 백엔드 서비스를 별도로 구현한다.
- Batch 주기는 초기 30초 주기로 설정하고 추후 조정

### TO-BE (phase-2)
- DB Queue에서 Message Broker로 교체
- Message Broker 고려 대상: RabbitMQ, Kafka
- cufeed-scrap-server는 Message Broker에 Produce된 데이터를 Comsume하여 처리하는 방식으로 Pub/Sub 형태로 구현한다.

