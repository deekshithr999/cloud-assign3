import os
import socket


def count_words(file_path):    
    content = read_from_file(file_path)
    nwords = len(content.split())
    return nwords

def list_top_n_words(file_path, n):

    content = read_from_file(file_path)
    words = content.split()
    dt = {}
    for w in words:
        dt[w] = dt.get(w,0)+1
    wc = list(dt.items())
    wc.sort(reverse=True, key= lambda x: x[1])
    
    #words = [w[0] for w in wc ]
    return wc[:n]

def list_files_at_path(path):
    fs_and_ds = os.listdir(path)
    files = [ fs for fs in fs_and_ds if fs.endswith('.txt')]
    return files

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def write_to_file(fpath, content):
    print("fpath == ", fpath)
    try:
        with open(fpath, 'w') as fd:
            fd.write(content)
    except Exception as e:
        print(f"Error occurred while writing to '{fpath}': {e}")


def read_from_file(fpath):
    try:
        with open(fpath, 'r') as fd:
            content = fd.read()
            return content
    except Exception as e:
        print(f"Error occurred while reading from '{fpath}': {e}")
        return ""


if __name__ == '__main__':
    FILEP = "/home/data/"
    FILEP1, FILEP2 = FILEP+'IF.txt',FILEP+'Limerick-1.txt'
    FILEP3 = "/home/output/result.txt"
    
    content = ""

    #4a
    FILE_PATH = FILEP
    files_lst = list_files_at_path(FILE_PATH)
    tstr = "Files at the path \"{}\": \n".format(FILE_PATH)
    for fname in files_lst:
        tstr +=  "    {} \n".format(fname)
    content += tstr

    #4b,4c 
    cnt1,cnt2 = count_words(FILEP1), count_words(FILEP2)
    tstr = ""
    tstr += "Word Count in \"{}\" : {} \n".format(FILEP1, cnt1)
    tstr += "Word Count in \"{}\": {} \n".format(FILEP2, cnt2)
    tstr += "Combined Word Count  of files in \"{}\" : {} words \n".format(', '.join([FILEP1.split("/")[-1], FILEP2.split("/")[-1]])
                                                                  , cnt1+cnt2)
    content += tstr

    #4d
    FILEP = FILEP1
    nwords = 3
    top_nwords = list_top_n_words(FILEP, nwords)
    tstr = "Top {} words of a file  \"{}\" :\n".format(nwords, FILEP)
    for w,c in top_nwords:
        tstr += "    {}: {} \n".format(w,c)
    content += tstr

    #4e
    ip_address = get_ip_address()
    tstr = "Ip address of the sytem is: {} \n".format(ip_address)
    content += tstr

    #4f
    write_to_file(FILEP3, content)

    #4g
    FILEP = FILEP3
    content = read_from_file(FILEP)
    print("~"*100)
    print(content, end='')
    print("~"*100)

