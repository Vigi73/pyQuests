import sqlite3
import xml.etree.cElementTree as ET


def search_location_classic(f='Пескарь', b='Озеро'):
    '''Поиск в базе по Базе и рыбе'''
    conn = sqlite3.connect("DataBase.db")
    cursor = conn.cursor()

    sql = f"SELECT BasesFishCont.CountFish, Fishes.Name, Bases.Name, BasesFishCont.MinWeight, " \
          f"BasesFishCont.MaxWeight, Locations.Name, Bait.Name  " \
          f"FROM  Bait, Locations, Bases, Fishes, BasesFishCont  WHERE BasesFishCont.IDCatchBait = Bait.ID AND " \
          f"BasesFishCont.IDCatchyLocation = Locations.ID AND BasesFishCont.IDBases = Bases.ID AND " \
          f"BasesFishCont.IDFish = Fishes.ID AND Fishes.Name='{f}' AND Bases.Name = '{b}'"

    cursor.execute(sql)
    temp = cursor.fetchall()

    return temp


def all_fish(f='Пескарь'):
    '''Поиск в базе по рыбе'''
    conn = sqlite3.connect("DataBase.db")
    cursor = conn.cursor()

    sql = f"SELECT BasesFishCont.CountFish, Fishes.Name, Bases.Name, BasesFishCont.MinWeight, BasesFishCont.MaxWeight, " \
          f"Locations.Name, Bait.Name FROM  Bait, Locations, Bases, Fishes, BasesFishCont  " \
          f"WHERE BasesFishCont.IDCatchBait = Bait.ID AND BasesFishCont.IDCatchyLocation = Locations.ID " \
          f"AND BasesFishCont.IDBases = Bases.ID AND BasesFishCont.IDFish = Fishes.ID AND Fishes.Name='{f}'"

    cursor.execute(sql)
    temp = cursor.fetchall()
    return temp


def all_fish_bait(bait='Пескарь'):
    conn = sqlite3.connect("DataBase.db")
    cursor = conn.cursor()

    sql = f"SELECT BasesFishCont.CountFish, Fishes.Name, Bases.Name, BasesFishCont.MinWeight, BasesFishCont.MaxWeight, " \
          f"Locations.Name, Bait.Name FROM  Bait, Locations, Bases, Fishes, BasesFishCont  " \
          f"WHERE BasesFishCont.IDCatchBait = Bait.ID AND BasesFishCont.IDCatchyLocation = Locations.ID " \
          f"AND BasesFishCont.IDBases = Bases.ID AND BasesFishCont.IDFish = Fishes.ID AND Bait.Name='{bait}'"

    cursor.execute(sql)
    temp = cursor.fetchall()
    return temp


def get_safari(fish=""):
    conn = sqlite3.connect("DataBase.db")
    cursor = conn.cursor()

    sql = f"SELECT BasesFishCont.CountFish, Fishes.Name, Bases.Name, BasesFishCont.MinWeight, BasesFishCont.MaxWeight, " \
          f"Locations.Name, Bait.Name FROM  Bait, Locations, Bases, Fishes, BasesFishCont  " \
          f"WHERE BasesFishCont.IDCatchBait = Bait.ID AND BasesFishCont.IDCatchyLocation = Locations.ID " \
          f"AND BasesFishCont.IDBases = Bases.ID AND BasesFishCont.IDFish = Fishes.ID AND Fishes.Name='{fish}'"

    cursor.execute(sql)
    temp = cursor.fetchall()

    max_count_fish = 0
    for i in temp:
        if i[0] > max_count_fish:
            max_count_fish = i[0]

    for i in temp:
        if i[0] == max_count_fish:
            return i


def get_mutants(m, f):
    tree = ET.parse('mutants.xml')

    for i, elm in enumerate(tree.findall('Mutant[Name="Линь"][Map="Пахра"]'), start=1):
        print(i, f'{elm[0].text} {elm[1].text} {elm[1].text}')