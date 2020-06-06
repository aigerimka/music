class Track:
    """Music track class"""
    def __init__(self, name, duration, singer, volume, year):
        self.name = name
        self.duration = duration
        self.singer = singer
        self._volume = volume
        self.year = year
        self.work = False

    def switch_on(self):
        if not self.work:
            self.work = True
        else:
            print('Музыкальный трек уже включен!')

    def switch_off(self):
        if self.work:
            self.work = False
        else:
            print('Музыкальный трек уже выключен!')

    volume = property()

    @volume.getter
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        if self.work and value > 0:
            self._volume = value
        else:
            self._volume = 0

    @volume.deleter
    def volume(self):
        print('Теперь вы не можете послушать трек из-за отсутствия звука:(')
        del self._volume

    def __str__(self):
        track = 'Название музыкального трека: ' + self.name + '\n'
        track += 'Длительность: ' + self.duration + '\n'
        track += 'Исполнитель: ' + self.singer + '\n'
        track += 'Громкость: ' + str(self._volume) + '\n'
        track += 'Год выпуска: ' + self.year + '\n'
        if self.work:
            track += 'Трек играет.' + '\n'
        else:
            track += 'Трек выключен.' + '\n'
        return track

    def __repr__(self):
        return self.__str__()


class Album:
    """Music album class"""
    def __init__(self, album_name, singer, year, lst_tracks):
        self.album_name = album_name
        self.singer = singer
        self.year = year
        self.lst_tracks = lst_tracks

    def __str__(self):
        album = 'Название альбома: ' + self.album_name + '\n'
        album += 'Исполнитель: ' + self.singer + '\n'
        album += 'Год выпуска: ' + self.year + '\n'
        album += 'Альбом состоит из следующих треков:' + '\n' + self.lst_tracks
        return album

    def __repr__(self):
        return self.__str__()
