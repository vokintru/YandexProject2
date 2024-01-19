import json


def get_lvl(file_name):
    list_ = []
    with open(file_name, "r", encoding="utf-8") as file:
        new = json.load(file)
        BPM = new["tempo"]
        out = new["tracks"][0]["bars"]

    new_out = []
    for i in range(len(out)):
        temp = out[i]
        if temp["notes"]:
            for j in temp["notes"]:
                o1 = int(temp["index"])
                o2 = int(int(j["pos"]) / 100)
                o_glob = o1 * 16 + o2

                new_out.append((o1, o2, j["markers"], BPM))
    return new_out


def fps(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        new = json.load(file)
        out = new["tempo"]
    return out


if __name__ == '__main__':
    out = get_lvl("33787.json")
    for i in out:
        print(i)
        pass
