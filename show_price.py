import sys
PRICE_FILE = "./bakery.csv"

def my_gen(start=-1, end=-1):

    def file_reader(start=-1, end=-1):

        with open(PRICE_FILE, "r", encoding="utf-8") as price_list:

            if start > 0:
                for _ in range(start - 1):
                    price_list.readline()

            if end > 0:
                for _ in range(abs(end-start)):
                    yield price_list.readline().replace("\n", "")
            else:
                for line in price_list:
                    yield line.replace("\n", "")

            for line in price_list:
                yield line.replace("\n", "")

    if __name__ == "__main__":
        pass

        start_pos = -1
        end_pos = -1

        if len(sys.argv) >= 2 and sys.argv[1].isdigit():
            start_pos = int(sys.argv[1])

        if len(sys.argv) == 3 and sys.argv[2].isdigit():
            end_pos = int(sys.argv[2])

        for l in file_reader(start_pos, end_pos):
            print(f"{float(l):.2f}")