import time
import emoji

for i in range(10, 0, -1):
    print('{}'.format(i), end='...', flush=True)
    time.sleep(1)

print(emoji.emojize('\n'+':fireworks::sparkler:' * 10))