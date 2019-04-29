from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib.request import urlopen as uopen

REGEX = compile(b'#([\d,]+) in Books')
AMZN = 'https://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Pytohn Web Development with Django',
    '0137343419': 'Python Fundamentals',
}

def getRanking(isbn):
    with uopen('{0}{1}'.format(AMZN, isbn)) as page:
        return str(REGEX.findall(page.read())[0], 'utf-8')

def main():
    print('At', ctime(), 'on Amazon...')
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(ISBNs, executor.map(getRanking, ISBNs)):
            print('- %r randking %s' % (ISBNs[isbn], ranking))
    print('全部完成:', ctime())

if __name__ == '__main__':
    main()
    