# Python-laskin decoraattorilla
Laskimen teko Pythonilla hyödyntäen Decoraattoria tulostuksessa.

## Ominaisuudet
* Koodista löytyy peruslaskutoimitukset: summa-, erotus-, kerto- ja jakolasku.
* Toteutus on tehty hyödyntäen decoraattor-ominaisuutta tulostuksessa.
* Tulostukset suoritetaan omassa funktiossaan "printing_result", jolloin jokainen funktio keskittyy vain yhteen tehtävään.

## Käyttöohje
1. Varmista, että koneelle on asennettu Python.
2. Aja tiedosto käyttäen komentoa: "python laskin.py".
3. Valitse haluamasi laskutoimitus (1-4).
4. Anna kaksi numeerista arvoa.
5. Tulos tulostuu terminaaliin!
6. Aja ohjelma uudestaan!

## Ohjelman toteutuksessa käytössä oleva Decorator
```python
def printing_result(base_fn):
    def enhanced_fn(*args, **kwargs):
        result = base_fn(*args, **kwargs)
        print(f"{a} {merkki} {b} = {result}")
        return result
    return enhanced_fn
