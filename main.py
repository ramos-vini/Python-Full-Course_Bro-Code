from multiprocessing import Process, cpu_count
import time


def number_counter(num):
    counter = 0
    while counter < num:
        counter += 1


def main():
    start_time = time.perf_counter()
    a = Process(target=number_counter(100000))
    b = Process(target=number_counter(100000))
    c = Process(target=number_counter(100000))
    d = Process(target=number_counter(100000))
    e = Process(target=number_counter(100000))
    f = Process(target=number_counter(100000))
    g = Process(target=number_counter(100000))
    h = Process(target=number_counter(100000))
    i = Process(target=number_counter(100000))
    j = Process(target=number_counter(100000))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()

    end_time = time.perf_counter()

    print(f"CPU cores: {cpu_count()}")
    total_time = end_time - start_time
    print(f"Program runned in {total_time} seconds")


if __name__ == "__main__":
    main()


