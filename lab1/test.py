import unittest
import arrow
import requests


class PythonApi(unittest.TestCase):
    
    def test_get_games(self):
        utc = arrow.utcnow()
        res = requests.get('http://127.0.0.1:5000/lab1/api/v1.0/games')

        if res.status_code == 200:
            print("Test 'get_games()' PASS at " + str(utc))
        else:
            print("Test 'get_games()' FAIL at " + str(utc))

    def test_get_game(self):
        utc = arrow.utcnow()
        res = requests.get('http://127.0.0.1:5000/lab1/api/v1.0/games/3')

        if res.status_code == 200:
            print("Test 'get_game()' PASS at " + str(utc))
        else:
            print("Test 'get_game()' FAIL at " + str(utc))

    def test_add_games(self):
        utc = arrow.utcnow()

        game = {"date": "2013-25-05",
                "teams": "Borussia Dortmund - Bayern Munich",
                "score": "1 - 2",
                "city" : "London"
                }

        res = requests.post('http://127.0.0.1:5000/lab1/api/v1.0/games', json=game)

        if res.status_code == 201:
            print("Test 'add_games()' PASS at " + str(utc))
        else:
            print("Test 'add_games()' FAIL at " + str(utc))

    def test_edit_game(self):
        utc = arrow.utcnow()

        game = {"date": "2013-25-05",
                "teams": "Borussia - Bayern",
                "score": "1 - 2",
                "city" : "London"
                #"id": "6"
                }
        res = requests.put('http://127.0.0.1:5000/lab1/api/v1.0/games/6', json=game)
        if res.status_code == 200:
            print("Test 'edit_games()' PASS at " + str(utc))
        else:
            print("Test 'edit_games()' FAIL at " + str(utc))
            
    def test_delete_game(self):
        utc = arrow.utcnow()

        res = requests.delete('http://127.0.0.1:5000/lab1/api/v1.0/games/6')
        if res.status_code == 200:
            print("Test 'delete_games()' PASS at " + str(utc))
        else:
            print("Test 'delete_games()' FAIL at " + str(utc))

if __name__ == "__main__":
    unittest.main()
