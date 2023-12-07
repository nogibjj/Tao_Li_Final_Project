import requests

def extract(url="https://github.com/BistduwohlnichtganzbeiTrost/imdb-movies/blob/main/movie.csv", 
            file_path="movie.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path