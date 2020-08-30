from iterator_old_2 import CountryURL
from generator_old_2 import MD5Generator, file
from decorator_2 import decor_logger
from decorator_2 import LOG_PATH

countryURL1 = CountryURL()
#countryURL1.__init__()
countryURL1.__next__()
md5_generator = MD5Generator(file)

@decor_logger(LOG_PATH)
def md5_gen():
    while True:
        print(next())




