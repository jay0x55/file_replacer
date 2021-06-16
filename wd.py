import os

def yup(damn, c):
    for x in c:
        damn = damn.replace(x[0], x[1])
    return damn

def run():
    conf = input("config >>> ")
    dr = input("Folder: ")
    par = []
    print("[+] running ....")

    with open(conf, 'r', encoding="utf-8") as cnf:
        config = cnf.read().split(";")
        if config[-1] == "\n":
            config.pop()
        par = [x.split("&") for x in config]
    for i in os.listdir(dr):
        with open(dr + "/" + i, "r", encoding="utf-8") as content:
            href = yup(content.read(), par)
            content.close()
        with open(dr + "/" + i, "w", encoding="utf-8") as data:
            data.write(href)

    print("\tOK")
    input("\n\npress any key to exit")


if __name__ == '__main__':
    try:
        run()
    except Exception as err:
        print(f"\n\t[!] error: {err}")
        input("\n\npress any key to exit")
