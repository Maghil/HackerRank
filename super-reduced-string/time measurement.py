import mine, suggested
import time

if __name__ == "__main__":
    start_mine_time = time.perf_counter()
    mine.superReducedString("aaabccddd")
    end_mine_time = time.perf_counter()
    start_suggested_time = time.perf_counter()
    suggested.superReducedString("aaabccddd")
    end_suggested_time = time.perf_counter()
    mine_time = (end_mine_time - start_mine_time) * 10**6
    suggested_time = (end_suggested_time - start_suggested_time) * 10**6
    print(f"{mine_time:.3f}")
    print(f"{suggested_time:.3f}")

