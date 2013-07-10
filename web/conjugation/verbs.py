import random
from conjugation import mongo

class Verbs():
    @classmethod
    def total(cls):
        return mongo.db.verbs.count()

    @classmethod
    def get_random_verb(cls, temp):
        total_verbs = cls.total()
        random_verbs = random.randrange(total_verbs - 1)
        return mongo.db.verbs.find({'temps.' + temp: {'$exists': True } }).skip(random_verbs).limit(1)[0]

    @classmethod
    def get_verb_pronouns(cls, verb):
        # Subject pronouns: http://en.wikipedia.org/wiki/French_personal_pronouns
        PRONOUNS = ['Je', 'Tu', 'Il/Elle', 'Nous', 'Vous', 'Ils/Elles']  
        PRONOUNS_CONTRACTED = ['J\'', 'Tu', 'Il/Elle', 'Nous', 'Vous', 'Ils/Elles']  

        first_letter = verb[0]
        return PRONOUNS_CONTRACTED if first_letter in 'aeiuoh' else PRONOUNS

    @classmethod
    def is_conjugation_correct(cls, temp, verb, form):
        verb_db = mongo.db.verbs.find({'_id' : verb, 'temps.' + temp: {'$exists': True } })[0]
        inflections = []
        for item in form.items():
            if 'conjugation' in item[0]: 
                inflections.append(item)

        inflections = sorted(inflections)
        temp = verb_db['temps'][temp]
        import ipdb; ipdb.set_trace()
        return True
