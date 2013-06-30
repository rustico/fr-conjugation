from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class ConjugasionSpider(BaseSpider):
    name = 'conjugaison'
    start_urls = ['http://www.collinsdictionary.com/dictionary/french-english/conjugation/dormir']
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        conjugations = hxs.select('//div[@class="conjugation" or @class="conjugation nomargin"]')
        for conjugation in conjugations:
            temp = conjugation.select('h3/text()').extract()
            inflections = conjugation.select('ul/li/text()').extract()
            if inflections:
                print(temp, inflections)
                break

    def get_start_urls():
        verbs = [
        'abandonner',
        'accepter',
        'accompagner',
        'acheter',
        'adorer',
        'agir',
        'aider',
        'aimer',
        'aller',
        'amener',
        'amuser',
        'appartenir',
        'appeler',
        'apporter',
        'apprendre',
        'approcher',
        'apprecier',
        'arranger',
        'arriver',
        'arreter',
        'asseoir',
        'assurer',
        'attaquer',
        'attendre',
        'attraper',
        'avancer',
        'avoir',
        'baiser',
        'battre',
        'blesser',
        'boire',
        'bosser',
        'bouger',
        'bruler',
        'cacher',
        'calmer',
        'casser',
        'cesser',
        'changer',
        'chanter',
        'charger',
        'chercher',
        'chier',
        'choisir',
        'commencer',
        'comprendre',
        'compter',
        'conduire',
        'connaitre',
        'construire',
        'continuer',
        'coucher',
        'couper',
        'courir',
        'couvrir',
        'couter',
        'craindre',
        'crever',
        'crier',
        'croire',
        'creer',
        'danser',
        'demander',
        'descendre',
        'devenir',
        'deviner',
        'devoir',
        'dire',
        'diriger',
        'discuter',
        'disparaitre',
        'donner',
        'dormir',
        'douter',
        'durer',
        'decider',
        'decouvrir',
        'defendre',
        'degager',
        'depecher',
        'deranger',
        'desirer',
        'desoler',
        'detester',
        'detruire',
        'diner',
        'echapper',
        'ecouter',
        'ecrire',
        'embrasser',
        'emmener',
        'emporter',
        'empecher',
        'enfuir',
        'engager',
        'enlever',
        'entendre',
        'entrer',
        'envoyer',
        'epouser',
        'esperer',
        'essayer',
        'etre',
        'etudier',
        'eviter',
        'excuser',
        'exister',
        'expliquer',
        'faire',
        'falloir',
        'fatiguer',
        'fermer',
        'ficher',
        'filer',
        'finir',
        'forcer',
        'foutre',
        'frapper',
        'fuir',
        'fumer',
        'gagner',
        'garder',
        'grandir',
        'habiter',
        'ignorer',
        'imaginer',
        'importer',
        'inquieter',
        'installer',
        'interesser',
        'inviter',
        'jeter',
        'jouer',
        'jurer',
        'laisser',
        'lancer',
        'laver',
        'lever',
        'liberer',
        'lire',
        'lacher',
        'maintenir',
        'manger',
        'manquer',
        'marcher',
        'marier',
        'mener',
        'mentir',
        'mettre',
        'monter',
        'montrer',
        'moquer',
        'mourir',
        'meriter',
        'naitre',
        'obliger',
        'obtenir',
        'occuper',
        'offrir',
        'oser',
        'oublier',
        'ouvrir',
        'paraitre',
        'pardonner',
        'parier',
        'parler',
        'partager',
        'partir',
        'passer',
        'payer',
        'penser',
        'perdre',
        'permettre',
        'plaire',
        'plaisanter',
        'pleuvoir',
        'porter',
        'poser',
        'poursuivre',
        'pousser',
        'pouvoir',
        'prendre',
        'prier',
        'profiter',
        'promettre',
        'proposer',
        'proteger',
        'prouver',
        'preferer',
        'preparer',
        'presenter',
        'prevenir',
        'prevoir',
        'quitter',
        'raconter',
        'ramener',
        'rappeler',
        'rater',
        'ravir',
        'recevoir',
        'recommencer',
        'reconnaitre',
        'refuser',
        'regarder',
        'regretter',
        'rejoindre',
        'remarquer',
        'remercier',
        'remettre',
        'remonter',
        'rencontrer',
        'rendre',
        'rentrer',
        'reposer',
        'reprendre',
        'respecter',
        'respirer',
        'ressentir',
        'ressembler',
        'rester',
        'retenir',
        'retirer',
        'retourner',
        'retrouver',
        'revenir',
        'revoir',
        'rire',
        'risquer',
        'realiser',
        'recuperer',
        'reflechir',
        'regler',
        'reparer',
        'repondre',
        'repeter',
        'reussir',
        'reveiller',
        'rever',
        'sauter',
        'sauver',
        'savoir',
        'sembler',
        'sentir',
        'servir',
        'signer',
        'signifier',
        'sonner',
        'sortir',
        'souffrir',
        'souhaiter',
        'souvenir',
        'suffire',
        'suivre',
        'supposer',
        'supporter',
        'surveiller',
        'separer',
        'taire',
        'tenir',
        'tenter',
        'terminer',
        'tirer',
        'tomber',
        'toucher',
        'tourner',
        'traiter',
        'travailler',
        'traverser',
        'trainer',
        'tromper',
        'trouver',
        'tuer',
        'utiliser',
        'valoir',
        'vendre',
        'venir',
        'virer',
        'vivre',
        'voir',
        'voler',
        'vouloir',
        'verifier', ]