from validator import validate_string
from models import *
from sqlalchemy import *
import os
import unittest
import json

class ValidatorTests(unittest.TestCase):
    def test_failOnEmpty(self):
        self.assertTrue(not validate_string('', allows_empty=False))

    def test_failOnNone(self):
        self.assertTrue(not validate_string(None, allows_none=False))

    def test_failOnInvalidOption(self):
        self.assertTrue(not validate_string('spock', acceptable_values=['rock', 'paper', 'scissors']))

    def test_succeedOnNotEmpty(self):
        self.assertTrue(validate_string('lizard', allows_empty=False))

    def test_succeedOnNotNone(self):
        self.assertTrue(validate_string('lizard', allows_none=False))

    def test_succeedOnValidOptionCaseSensitiveFalse(self):
        self.assertTrue(validate_string('ROCK', acceptable_values=['rock', 'paper', 'scissors']))

    def test_failOnCaseSensitiveTrue(self):
        self.assertTrue(
            not validate_string('ROCK', case_sensitive=True, acceptable_values=['rock', 'paper', 'scissors']))


class ServiceTests(unittest.TestCase):
    def setup(self):
        self.key = "5TKM3A9I44YRV6UMR0ZS"
        self.testDbPath = 'sqlite:///C:/users/Matthew/SkyDrive/Toast/test.db'
        db = create_engine(self.testDbPath, echo=False)
        metadata = MetaData(db)

        db.execute("drop table if exists users");
        db.execute("drop table if exists records");

        users = Table('users', metadata,
            Column('name', String, nullable=False),
            Column('secret', String, nullable=False)
        )
        users.create()
        records = Table('records', metadata,
            Column('user', String, ForeignKey("users.name"), nullable=False),
            Column('start', Integer, nullable=False),
            Column('finish', Integer, nullable=True)
        )
        records.create()
        i = users.insert()
        i.execute({'name': 'Adam', 'secret': '5TKM3A9I44YRV6UMR0ZS'})
        i = records.insert()
        i.execute({'user': 'Adam', 'start': 200, 'finish': 300})
        i.execute({'user': 'Adam', 'start': 400})
        self.service = service.service(self.testDbPath)

    def test_on_off(self):
        self.setup()
        onRequest = json.loads(self.service.on("5TKM3A9I44YRV6UMR0ZS"))
        time = onRequest["data"]["effective"]
        expected = response.response(response.STATUS, {'status': True, 'count': 3, 'last': time, 'started': 200}).json()
        time = json.loads(self.service.off("5TKM3A9I44YRV6UMR0ZS"))["data"]["effective"]
        expected = response.response(response.STATUS,
            {'status': False, 'count': 3, 'last': time, 'started': 200}).json()
        self.assertEqual(self.service.get(), expected)

    def test_invalid_key(self):
        self.setup()


class PageTests(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()