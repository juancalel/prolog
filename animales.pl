animal(oso, herviboro).
animal(leon,carnivoro).
animal(gato,carnivoro).
animal(oso,carnivoro).
animal(conejo,herviboro).
animal(oso,herviboro).
vive(oso,30).
vive(leon,25).
vive(gato,10).
vive(conejo,5).
omnivoro(X):- animal(X,carnivoro), animal(X,herviboro).
mayorDiezOmnivoro(X) :- omnivoro, vive(X,Y), Y>=10.
