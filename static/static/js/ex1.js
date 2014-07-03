maFiche={
    id : "7845",
    nom :"Durand",
    prenom :"Jean-Pierre",
    dateNaissance :"17/08/1967"
}

function monControl($scope){
    $scope.infoPerso=maFiche;
}



function monControl2($scope){
    $scope.mesFruits=["banane","pomme", "ananas","pêche","fraise"] ;
}


monTableau=[
                {id : "7845",
                nom :"Durand",
                prenom :"Jean-Pierre",
                dateNaissance :"17/08/1967"},

                {id : "6578",
                nom :"Dupond",
                prenom :"Gérard",
                dateNaissance :"23/04/1984"},

                {id : "9876",
                nom :"Robert",
                prenom :"Gabriel",
                dateNaissance :"21/02/1991"}
            ]


function monControl3($scope){
    $scope.mesClients=monTableau ;
}



monControleur=function($scope){
$scope.tabSerie=[
                    {
                    titre:"Le Trône de fer",
                    titreOr:"Game of Thrones",
                    createur:" David Benioff et D. B. Weiss",
                    urlImage:"image/got.jpg",
                    etat:"en cours saison 04 diffusée au printemps 2014"},

                    {
                    titre:"Lost : Les Disparus",
                    titreOr:"Lost",
                    createur:"J. J. Abrams, Damon Lindelof et Jeffrey Lieber",
                    urlImage:"image/lost.jpg",
                    etat:"terminée"},

                    {
                    titre:"Homeland",
                    titreOr:"Homeland",
                    createur:"Howard Gordon et Alex Gansa",
                    urlImage:"image/homeland.jpg",
                    etat:"en cours, saison 03 diffusée en septembre 2013"
                    }
                ]
}

