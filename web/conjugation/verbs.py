# -*- coding: utf-8 -*-
import random
from conjugation import mongo

class Verbs():
    @classmethod
    def total(cls):
        return mongo.db.verbs.count()

    @classmethod
    def get_random_verb(cls, temp, mode):
        total_verbs = cls.total()
        random_verbs = random.randrange(total_verbs - 1)
        return mongo.db.verbs.find({'temps.temp': temp, 'temps.mode' : mode }).skip(random_verbs).limit(1)[0]

    @classmethod
    def get_verb_pronouns(cls, verb):
        # Subject pronouns: http://en.wikipedia.org/wiki/French_personal_pronouns
        PRONOUNS = ['Je', 'Tu', 'Il/Elle', 'Nous', 'Vous', 'Ils/Elles']  
        PRONOUNS_CONTRACTED = ['J\'', 'Tu', 'Il/Elle', 'Nous', 'Vous', 'Ils/Elles']  

        first_letter = verb[0]
        return PRONOUNS_CONTRACTED if first_letter in u'aeiuohé' else PRONOUNS

    @classmethod
    def is_conjugation_correct(cls, temp, mode, verb, inflections):
        verb_db = mongo.db.verbs.find({'_id' : verb, 'temps.temp' : temp, 'temps.mode': mode })[0]
        inflections_db = cls.get_verb_inflections(verb_db, temp, mode)
        is_correct = True
        corrections = [None] * len(inflections)
        pronouns = cls.get_verb_pronouns(verb)
        for i in range(len(inflections)):
            # je parle ->  jeparle != jeparle <- je + ParLe
            if(inflections_db[i].replace(' ', '') != u'{0}{1}'.format(pronouns[i], inflections[i]).lower()):
                is_correct = False
                corrections[i] = inflections_db[i]

        return (is_correct, corrections)

    @classmethod
    def get_verb_inflections(cls, verb, temp, mode):
        for item in verb['temps']:
            if item['temp'] == temp and item['mode'] == mode:
                return item['inflections']

        return None
