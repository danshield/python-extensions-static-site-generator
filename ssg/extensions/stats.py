from ssg import hooks
import time

start_time = None
total_writtn = 0

@hooks.register("start_build")
def start_build():
    global start_time = time.localtime()

@hooks.register("total_written")
def written():
    global total_written += 1

@hooks.register("stats")
def stats():
    final_time = time.localtime() - start_time
    average = final_time / total_written if total_written > 0 else 0

    report = "Converted: {} - Time: {:.2f} sec - Avg: {:.4f} sec/file"
    report.format(total_written, final_time, average)