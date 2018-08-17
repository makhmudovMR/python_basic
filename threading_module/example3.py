import threading
import os
import urllib.request
from threading import Thread
from queue import Queue


class Downlaoder(Thread):
    """Stream file loader"""
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        """Init thread"""
        while True:
            # get url from queue
            url = self.queue.get()

            # download file
            self.download_file(url)

            # send the signal about task done
            self.queue.task_done()

    def download_file(self, url):
        """Download files"""
        handle = urllib.request.urlopen(url)
        fname = os.path.basename(url)

        with open(fname, 'wb') as f:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break

                f.write(chunk)


def main(urls):
    """Start programm"""
    queue = Queue()

    # start stream and queue
    for i in range(5):
        t = Downlaoder(queue)
        t.setDaemon(True)
        t.start()

    for url in urls:
        queue.put(url)

    queue.join()

if __name__ == '__main__':
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

    main(urls)