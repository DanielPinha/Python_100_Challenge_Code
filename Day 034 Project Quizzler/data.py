import requests

NUMBER_OF_QUESTIONS = 10
SCIENCE_COMPUTER_CATEGORY = 18
TRUE_FALSE_QUESTION = 'boolean'

trivia_param = {
    'amount': NUMBER_OF_QUESTIONS,
    'category': SCIENCE_COMPUTER_CATEGORY,
    'type': TRUE_FALSE_QUESTION,
}

trivia_data = requests.get(url='https://opentdb.com/api.php', params=trivia_param)
trivia_data.raise_for_status()

question_data = trivia_data.json()['results']
