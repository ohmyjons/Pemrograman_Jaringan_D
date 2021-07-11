from library import download_broadcast_gambar,get_url_list
import time
import datetime
import threading

TARGET_IP = '192.168.122.0'
TARGET_PORT = 5005


def download_broadcast_semua():
    texec = dict()
    urls = get_url_list()

    catat_awal = datetime.datetime.now()
    for k in urls:
        print(f"download dan broadcast {urls[k]}")
        waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar dan broadcast secara multithread
        texec[k] = threading.Thread(target=download_broadcast_gambar, args=(urls[k], True, TARGET_IP, TARGET_PORT))
        texec[k].start()

    #setelah menyelesaikan tugasnya, dikembalikan ke main thread dengan join
    for k in urls:
        texec[k].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


#fungsi download_broadcast_gambar akan dijalankan secara multithreading

if __name__=='__main__':
    download_broadcast_semua()