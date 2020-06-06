from tracks_albums import *


def add_track(lst):
    name = input('Введите название трека: ')
    duration = input('Введите длительность трека: ')
    singer = input('Введите исполнителя трека: ')
    volume = input('Введите громкость трека: ')
    year = input('Введите год выпуска трека: ')
    new_track = Track(name, duration, singer, volume, year)
    lst.append(new_track)
    return lst


def update(lst, album):
    track_result = ''
    for i in lst:
        track_result += str(i)
    all_tracks = track_result
    album.lst_tracks = all_tracks
    return all_tracks


def main():
    tracks = []
    new_album = None
    while True:
        commands = ['1 - Создать альбом',
                    '2 - Добавить трек в альбом',
                    '3 - Удалить трек из альбома',
                    '4 - Включить трек',
                    '5 - Выключить трек',
                    '6 - Изменить громкость трека',
                    '7 - Вывести данные всех треков из альбома',
                    '8 - Вывести информацию об альбоме и треках на экран',
                    '9 - Выйти из программы']
        for i in commands:
            print(i)
        while True:
            try:
                choice = int(input('Введите номер команды от 1 до 9: '))
                if choice < 1 or choice > 9:
                    raise Exception
                break
            except:
                print('Неверный ввод, попробуйте еще раз.')

        if choice == 1:
            name = input('Введите название альбома: ')
            singer = input('Введите исполнителя альбома: ')
            year = input('Введите год выпуска альбома: ')
            new_album = Album(name, singer, year, [])
            print('Новый альбом создан.')
        elif choice == 2:
            add_track(tracks)
            update(tracks, new_album)
            print('Трек добавлен в альбом.')
        elif choice == 3:
            delete = input('Введите номер трека, который хотите удалить: ')
            for i in range(1, len(tracks)+1):
                if int(delete) == i:
                    tracks.remove(tracks[i-1])
                    update(tracks, new_album)
                    print('Трек удален с альбома.')
        elif choice == 4:
            track_on = input('Введите номер трека, который хотите включить: ')
            for i in range(1, len(tracks) + 1):
                if int(track_on) == i:
                    tracks[i-1].switch_on()
                    update(tracks, new_album)
                    print('Трек №' + track_on + ' теперь включен.')
        elif choice == 5:
            track_off = input('Введите номер трека, который хотите выключить: ')
            for i in range(1, len(tracks) + 1):
                if int(track_off) == i:
                    tracks[i-1].switch_off()
                    update(tracks, new_album)
                    print('Трек №' + track_off + ' теперь выключен.')
        elif choice == 6:
            num = int(input('Введите номер трека, у которого вы хотите изменить громкость: '))
            for i in range(1, len(tracks) + 1):
                if num == i:
                    if tracks[i-1].work:
                        value = int(input('Введите желаемую громкость: '))
                        tracks[i-1].volume = value
                        update(tracks, new_album)
                        print('Громкость изменена.')
                    else:
                        print('Включите для начала трек!')
        elif choice == 7:
            print(new_album.lst_tracks)
        elif choice == 8:
            print(new_album)
        elif choice == 9:
            print('Работа программы завершена.Спасибо за уделенное время!:)')
            break


if __name__ == '__main__':
    main()
