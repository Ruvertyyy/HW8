try:
     x = int(input("Напиши число "))
     print(10/x)
except ZeroDivisionError:
     print("Не можна ділити на ноль")

except ValueError:
     print("Потрібно ввести число")
else:
    print("Успвшно")
finally:
    print("Кінець")