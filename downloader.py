import requests


def download(url,progress_bar,file_name,root):
    response = requests.get(url,allow_redirects=True,stream=True)
    file_size = response.headers.get('content-length', None)


    f = open(file_name,'wb')
    try:
        if file_size is None:
            f.write(response.content)
            progress_bar['value'] = 100
        else:
            file_size = int(response.headers.get('content-length', None))
            downloaded = 0
            for data in response.iter_content(chunk_size=max(int(file_size / 1000), 1024 * 1024)):
                downloaded += len(data)
                f.write(data)
                progress_bar['value'] = (downloaded / file_size) * 100
                root.update_idletasks()
        f.close()
    except:
        f.close()
