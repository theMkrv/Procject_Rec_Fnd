#Project by Makarov A.
import random
from termcolor import colored
import time


def big_list(min_num, max_num, cnt_lst):
    global zum_bin
    zum = []
    zum_bin = []
    for i in range(cnt_lst):
        zum.append(random.randint(min_num, max_num))
    for u in zum:
        zum_bin.append(bin(u))
    return zum_bin

def non_recourse(zum_bin, fndng_num):
    try:
        mid = len(zum_bin) // 2
        low = 0
        high = len(zum_bin) - 1

        while zum_bin[mid] != fndng_num and low <= high:
            if fndng_num > zum_bin[mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        if low > high:
            return None
        else:
            return mid
    except:
        return None


def recourse(zum_bin, fndng_num, step, cnt_lst):
    try:
        if step > cnt_lst:
            return None
        else:
            mid = (len(zum_bin)) // 2
            if fndng_num == zum_bin[mid]:
                return mid
            elif fndng_num < zum_bin[mid]:
                return recourse(zum_bin, fndng_num, step, mid - 1)
            else:
                return recourse(zum_bin, fndng_num, mid + 1, cnt_lst)
    except:
        return None


def main():
    try:
        strt = time.time()
        min_num = int(input("Введите минимальное значение: "))
        max_num = int(input("Введите максимальное значение: "))

        if min_num > max_num:
            print(colored("Минимальное значение не может быть больше максимального ;(", "red"), "\n" +
                  "Попробуйте снова)")
            main()

        cnt_lst = int(input("Введите количество эллиментов в списке (max = 995): "))
        if cnt_lst > 995:
            print(colored("Кололичество элемементовтов не может превышать 995 ;(", "red"), "\n" +
                  "Попробуйте снова)")
            main()

        fndng_num = bin(int(input("Какое число хочешь найти?: ")))
        step = 0

        big_list(min_num, max_num, cnt_lst)

        print("Позиция:", non_recourse(zum_bin, fndng_num))
        print("Время работы программы итериррированием:", str(time.time() - strt) + ' сек.')

        print("Позиция:", recourse(zum_bin, fndng_num, step, cnt_lst))
        print("Время работы программы рекурсией:", str(time.time() - strt) + ' сек.')

    except:
        print(colored("Что-то пошло не так ;(", "red"), "\n" +
              "Попробуйте снова)")
        main()


if __name__ == '__main__':
    main()
