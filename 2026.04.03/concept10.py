"""
범례지정(Legend) : 그래프에 데이터의 종류를 표시하기 위한 텍스트
legend() : 그래프에 범례 표시
xlim() : x축이 표시되는 범위 지정[xmin, xmax]
ylim() : y축이 표시되는 범위 지정[ymin, ymax]
axis() : x,y축이 표시되는 범위 지정[xmin, xmax, ymin, ymax]
입력 값이 없으면 자동으로 지정

plot() 함수의 marker="s", "D"
plot() 함수의 color = "색상"
대표색상
'b' : blue, 'g' : green, 'r' : red, 'y' : yellow, 'k' : black, 'w' : white

xticks(), yticks() : 각각 x축, y축 눈금 설정

scatter() : 산점도 시각


"""
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [3, 6, 9, 12], marker="s") #네모 모양
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.xlim([0, 5])      
plt.ylim([0, 15])    

plt.show()

plt.plot([1,2,3,4],[1,5,9,15],marker="D") #다이야 모양
plt.axis([0,6,0,20]) #x축시작 0~6, y축시작 0~20
plt.show()

plt.plot([1, 2, 3, 4], [2.0, 3.0, 5.0, 10.0], 'r') #빨강색
plt.plot([1, 2, 3, 4], [2.0, 2.8, 4.3, 6.5], color = 'violet') #보라색
plt.plot([1, 2, 3, 4], [2.0, 2.5, 3.3, 4.5], color = 'green') #초록색

plt.xlabel('X-Label')
plt.ylabel('Y-Label')

plt.show()

x = [1, 2, 3]
years = ['2022', '2023', '2024']
values = [300, 100, 700]

plt.bar(x, values, color=['r', 'g', 'b'], width=0.4)
#plt.bar(x, values, color=['r', 'g', 'b'], width=0.8)

plt.xticks(x, years) #x축 눈금을 년도에 표시

plt.show()