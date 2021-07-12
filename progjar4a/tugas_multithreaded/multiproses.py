from file_client_cli import remote_get
import time
import datetime
from multiprocessing import Process

def mengunduh():
    texec = dict()
    # urls = get_url_list()
    catat_awal = datetime.datetime.now()
    fileName = 'pokijan.jpg'
    for n in range(100):
        print(f"mendownload GET {[n]}")
        waktu = time.time()
        #mengistruksikan eksekusi fungsi download gambar secara multiprocess
        texec[n] = Process(target=remote_get, args=(fileName,))
        texec[n].start()
    #setelah menyelesaikan tugasnya, dikembalikan ke main process dengan join
    for k in range(100):
        texec[n].join()
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


#fungsi download_gambar akan dijalankan secara multi process
if __name__=='__main__':
    mengunduh()