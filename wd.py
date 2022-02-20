import os


def yup(damn, c):
    for x in c:
        if x[0].startswith('\n'):
            x[0] = x[0][1:]
        damn = damn.replace(x[0], x[1])
    return damn


def replace(dr, par):
    allowed_exts = ['html', 'txt']
    for i in os.listdir(dr):
        path = dr + "/" + i
        if os.path.isdir(path):
            replace(path, par)
            continue
        if path.split(".")[-1] not in allowed_exts:
            continue
        with open(path, "r", encoding="utf-8") as content:
            href = yup(content.read(), par)
            content.close()
        with open(path, "w", encoding="utf-8") as data:
            data.write(href)


def run():
    conf = input("config >>> ")
    dr = input("Folder: ")
    print("[+] running ....")

    with open(conf, 'r', encoding="utf-8") as cnf:
        config = cnf.read().split(";")
        if config[-1] == "\n":
            config.pop()
        par = [x.split("&") for x in config]
        replace(dr, par)
    print("\tOK")
    input("\n\npress any key to exit")


if __name__ == '__main__':
    try:
        run()
    except Exception as err:
        print(f"\n\t[!] error: {err}")
        input("\n\npress any key to exit")
