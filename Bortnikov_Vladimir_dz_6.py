#Задание 1

def parse_log(pth_file="./nginx_logs.txt"):
    if pth_file:
        with open(pth_file,"r") as file:
            for line in file:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[1]
                rsp,pth,_ = rsp_and_pth.split(" ")
                with open("nginx.txt", "a") as out_file:
                    out_file.writelines(f"{ip} {rsp} {pth}" + "\n")
                print (rsp,pth)

pth_file="./nginx_logs.txt"
parse_log(pth_file)

#Задание 3

import json
from my_utils import gen_zip

def groping(
        output_pth="./out.txt",
        user_pth="./users.txt",
        hobby_pth="./hobby.txt"):



    if not (user_pth or hobby_pth):
        return -1

    user_lines = None
    hobby_lines = None

    with open(user_pth, "r") as user_file:
        user_lines = user_file.readlines()

    with open(hobby_pth, "r") as hobby_file:
        hobby_lines = hobby_file.readlines()

    if len(user_lines) < len(hobby_lines):
        return 1

    group = {}

    for fio, hobby in gen_zip (user_lines, hobby_lines):
        fio = fio.replace("\n", "").replace(",", " ")
        group[fio] = hobby.replace("\n", "") if hobby else None


    with open(output_pth, "w+") as out_file:
        out_file.writelines(json.dumps(group))

    return 0

groping(output_pth="./out.txt", user_pth="./users.txt", hobby_pth="./hobby.txt")

#Задание 6