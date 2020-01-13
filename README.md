# Web de la secció sindical CGT PAS-L de la UPC

## Preparar l'entorn de desenvolupament

Instal·lar Ruby i Jekyll (entorn de desenvolupament local a l'usuari mitjançant [RVM](https://rvm.io/)):

    gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys \
        409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
    sudo apt install curl
    \curl -sSL https://get.rvm.io | bash -s stable
    source $HOME/.rvm/scripts/rvm
    bash --login            # o bé tancar la sessió i fer login novament
    rvm install 2.7.0       # pot demanar password per instal·lar dependències de compilació
    rvm use 2.7.0
    gem install bundler jekyll
