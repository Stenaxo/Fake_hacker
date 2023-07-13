
import time


def main():
    with open('hack.txt', 'r') as f:
        content = f.read()

    character_per_iteration = 300
    print('\033[32m' + "Press any key to enter in the system")
    input()
    for i in range(0, len(content), character_per_iteration):

        print(content[i:i+character_per_iteration], end = " ", flush = True)
        time.sleep(0.1)
        #input()

if __name__ == '__main__':
    main()