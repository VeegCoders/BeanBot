import logging

from operator import itemgetter

logger = logging.getLogger('BeanBot-points')
logger.info('Starting Points module')

class Points:
    def __init__(self, database):
        self.ppdb = database
        self.pps = dict()
        self.pps = self.get_contents()

    def load_pps(self):
        logger.debug('Reading points from database...')
        cur = self.ppdb.cursor()
        with self.ppdb:
            cur.execute("""CREATE TABLE IF NOT EXISTS points
                       (key text NOT NULL UNIQUE, value int NOT NULL)""")
        return self.get_contents()

    def get_contents(self, tablename='points'):
        cur = self.ppdb.cursor()
        for row in cur.execute('select * from {}'.format(tablename)):
            self.pps[row[0]] = row[1]
        return self.pps

    def get_all_scores(self):
        self.get_contents()
        high_score = sorted(self.pps.items(), key=itemgetter(1), reverse=True)[:10]
        low_score = sorted(self.pps.items(), key=itemgetter(1))[:10]
        high = "High scores:\n"
        for k, v in high_score:
            high = high + '<b>' + k + '</b>' + ": " + str(v) + "; "
        low = "\nLow scores:\n"
        for k, v in low_score:
            low = low + '<b>' + k + '</b>' + ": " + str(v) + "; "
        return high, low

    def change_record(self, op, keyword):
        with self.ppdb:
            cur = self.ppdb.cursor()
            if keyword in self.pps:
                if op == 'pp':
                    new_value = self.pps[keyword] + 1
                    oper = 'adding'
                elif op == 'mm':
                    new_value = self.pps[keyword] - 1
                    oper = 'subtracting'
                print("{} in dict, {} one.".format(keyword, oper))
                cur.execute("UPDATE points SET value = ? WHERE key = ?", (new_value, keyword))
            else:
                if op == 'pp':
                    new_value = 1
                elif op == 'mm':
                    new_value = -1
                print("{} not in dict, setting.".format(keyword))
                cur.execute("INSERT INTO points(key, value) VALUES(?, ?)", (keyword, new_value))
        self.get_contents()

