# StudyAlgorithm

## [실전알고리즘강좌 by 동빈나](https://www.youtube.com/playlist?list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz)
>source: https://www.youtube.com/playlist?list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz

### 정렬(Sorting)

* __선택정렬__
  * 복잡도: O(N^2)
  * 가장 작은 것을 맨 앞으로 보내는 과정 반복
  
* __버블정렬__
  * 복잡도: O(N^2)
  * 바로 옆 값과 비교하여 작은 값을 앞으로 보내는 과정 반복 
  * 즉석에서 계속 교체하기 때문에 가장 비효율적
  
* __삽입정렬__
  * 복잡도: O(N^2)
  * 앞은 정렬됐다고 가정, 숫자를 적절한 위치에 삽입
  * 필요할 때에만 Swap이 일어남 -> O(N^2) 중엔 가장 빠름
  
* __퀵정렬__
  * 복잡도: O(N*logN) but 최악은 O(N^2)
  * 기준값(피벗)을 중심으로 왼/오른쪽에 값을 정렬한다.
