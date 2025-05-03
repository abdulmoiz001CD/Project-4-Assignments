import time
def main():
    for _ in range(10,0,-1):
        if _ == 0:
         time.sleep(1)
         print(f"liftoff")
        else:
         print(f"{_}")
         time.sleep(1)


if __name__ == "__main__":
   main()