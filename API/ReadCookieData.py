import pandas as pd

class ReadCookieData():
  def ReadCookie(filepath):
    object = pd.read_pickle(filepath)
    print(object)