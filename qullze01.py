#컴퓨터가 생각하는 수를 맞추기
#기회는 6번
#6번 이후에는 정답을 출력한다.
import random as r

root = tk.Tk()
root.geometry("200x200")

q_num = r.randint(1,100)
print("----숫자 맞추기---", q_num)

for num in range(1,7):
    u_ans = int(input("%d번째 예상 숫자: "% num))
    if u_ans == q_num:
        print("정답이야!!")
        break
    if u_ans > q_num:
        print("더 작은 수를 넣어봐!!")
    else:
        print("더 큰 수를 넣어봐!")
if num == 6:
    print("정답은 %d!!" % q_num)

