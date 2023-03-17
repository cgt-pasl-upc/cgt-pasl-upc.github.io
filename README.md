# Web de la secció sindical CGT PAS-L de la UPC

Aquesta web està generada amb [Jekyll](https://jekyllrb.com).

## Preparar l'entorn de desenvolupament

Instal·lar Ruby i Jekyll (entorn de desenvolupament local a l'usuari mitjançant [RVM](https://rvm.io/)):

```bash
gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys \
        409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
sudo apt install curl
\curl -sSL https://get.rvm.io | bash -s stable
source $HOME/.rvm/scripts/rvm
bash --login            # o bé tancar la sessió i fer login novament
rvm install 3.1.2       # pot demanar password per instal·lar dependències de compilació
rvm use 3.1.2
gem install bundler jekyll
```

Dins del directori del repositori, executar:

```bash
    bundle install
```

Per fer proves en local:

```bash
    bundle exec jekyll serve     # connectar-se a http://localhost:4000
```
## Com modificar la web

Per modificar la web, la manera més senzilla és modificar directament el fitxer
des de la web de GitHub. Per fer-ho, cal autenticar-se a GitHub, accedir al
repo del web de CGT, navegar fins al fitxer que volem modificar i, quan el
tinguem obert, clicar a la icona `edit` (icona del llapis).

En acabat, guardem el fitxer. Això afegirà un "commit" al repositori de GitHub,
i en breus moments els canvis ja seran visibles des de la web (si no
es veuen els canvis, recarregueu la pàgina amb `<Ctrl> + <F5>`).

## Estructura de les pàgines

Les pàgines es guarden en fitxers de texte pla, fent servir sintaxi
[Markdown](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).
També es pot fer servir sintaxi HTML (per exemple, a la pàgina inicial,
`index.html`). Jekyll fa servir la extensió del fitxer per deduïr la sintaxi.

Tots els fitxers de pàgines (independentment de la sintaxi utilitzada)
han de tenir una capçalera Jekyll delimitada per tres guionets `---` al
principi i al final, per exemple:

```
---
title: Contacta        # títol de la pàgina
layout: page           # plantilla per generar la pàgina
permalink: /contacta/  # enllaç "maco"
---
```

Després de la capçalera va tot el contingut de la pàgina.

## Afegir una pàgina nova

- Crear un nou fitxer `.md` indicant `layout: page` a la capçalera.
- Si volem que la pàgina aparegui com un enllaç a la barra de navegació, editar
  el fitxer `_config.yml` i afegir la pàgina sota la directiva `header_pages`.

## Afegir una nova entrada al blog

- Crear un nou fitxer sota el directori `_posts/`. El nom del fitxer ha de tenir
  el format `AAAA-MM-DD-titol-del-post.md` (AAAA-MM-DD és la data de publicació
  associada a la nova entrada).
- Afegir la següent capçalera al fitxer:

    ```
    ---
    layout: post
    title: Títol del post
    date: 2020-01-13 13:40:39 +0100    # opcional
    author: Pepito                     # opcional
    categories: etiqueta1 etiqueta2    # opcional. Exemples: 'activitats', 'portada'.
    ---
    ```

- A continuació de la capçalera, escriure el contingut del post.
- Si el post és molt llarg, es pot generar un «fragment» del post afegint la
  cadena `<!--more-->`, en qualsevol punt del contingut. El text que segueix
  serà reemplaçat per un l'enllaç «Segueix llegint...», que enllaçarà al post sencer.

## Categories dels posts

* Indiqueu la categoria `portada` si voleu que un post es mostri a la portada del web.
* Indiqueu la categoria `activitats` si voleu que un post aparegui al registre d'activitats setmanals.

## Obtenir l'informe de tasques del Trello

En primer lloc caldrà obtenir l'exportació del fitxer JSON mitjançant l'adreça https://trello.com/b/QyEgSPJt.json

```bash
virtualenv -p python3 .env
source .env/bin/activate
cat QyEgSPJt.json | bin/trello.py <DATA_INICI> <DATA_FINAL> 
```
