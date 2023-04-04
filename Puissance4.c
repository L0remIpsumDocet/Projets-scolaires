#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define NBLIG 6 //Le nombre de lignes de la grille de puissance 4
#define NBCOL 7 //Le nombre de colonne de la grille de puissance 4

const char PION_A = 'X';
const char PION_B = 'O';
const char VIDE = ' ';
const char INCONNU = ' ';
const int COLONNE_DEBUT = NBCOL/2;

typedef char Grille[NBLIG][NBCOL];

/* 
procédure initGrille(Grille g)
Initialise la grille en affectant la constante VIDE à chacun de ses éléments. 
*/

void initGrille(Grille g) //Permet d'initialiser la grille et de remplir les tableaux d'espaces
{
    int l,c;
    for (l=0;l<NBLIG;l++){
        for (c=0;c<NBCOL;c++){
            g[l][c]=VIDE;
    }
    }
}

void quitter(){
    printf("Merci d'avoir joué");
    exit(0);
}


/* 
procédure afficher(Grille g, char pion, int colonne)
Réalise l’affichage à l’écran du contenu de la grille avec les pions déjà joués. Cette procédure
affiche aussi, au-dessus de la grille, le prochain pion à tomber et les numéros de chacune des colonnes
*/

void afficher(Grille g, char pion, int colonne){
    int i,j;
    //Affichage du numéro des colonnes
    printf("\n");
    for (j=1;j<=NBCOL;j++){
        printf("  %d ",j);
    }
    
    printf("\n");
    
    //Affichage de la position du pion à placer
    printf("  ");
    for (j=1;j<=NBCOL;j++){
        if (j==colonne){
            printf("%c",pion);
        }
        else{
            printf(" ");
        }
        printf("   ");
    }
    
    //Affichage de la grille
    for (i=NBLIG-1;i>=0;i=i-1){
        //Ligne supérieure des cases
        printf("\n|");
        for (j=0;j<NBCOL;j++){
            printf("   |");
        }
        //Ligne du milieu des cases
        printf("\n|");
        for (j=0;j<NBCOL;j++){
            printf(" %c |",g[i][j]);
        }
        //Ligne inférieure des cases
        printf("\n|");
        for (j=0;j<NBCOL;j++){
            printf("___|");
        }
    }
    printf("\n"); //Saut de ligne final pour que le joueur ait de la place pour écrire
}

/* 
fonction choisirColonne(Grille g, char pion, int arrow)
Un joueur voit son pion au-dessus de la grille et cette fonction doit lui permettre de "déplacer"
son pion d’une colonne vers la gauche (par la touche ‘q’) ou d’une colonne vers la droite (par la
touche ‘d’). Après chaque déplacement, la grille est réaffichée. Le joueur peut finalement
choisir la colonne où il souhaite faire tomber son pion (par la touche ESPACE). 
*/
int choisirColonne(Grille g, char pion, int arrow){
    char continu,err;
    afficher(g,pion,arrow);
    scanf("%c%c",&continu,&err);//err permet de s'assurer que le bon caractère soit sélectionné malgré le retour chariot
    while (continu!=' '){
        //Si le joueur décide d'afficher les règles de  jeu
        if (continu=='r'){
            printf("Le but du puissance 4 est d'aligner une suite de 4 jetons de même couleur horizontalement, verticalement ou en diagonale. Attention, les jetons tomberont tout en bas de la grille, sauf s'il y a d'autres jetons en dessous.");
        }
        //Si le joueur décide de quitter le jeu
        else if (continu=='0'){
            quitter();
        }
        //Si le joueur décide de déplacer le curseur à droite
        else if ((continu=='q')&&(arrow>1)){
            arrow=arrow-1;
        }
        //Si le joueur décide de déplacer le curseur à gauche
        else if ((continu=='d')&&(arrow<NBCOL)){
            arrow=arrow+1;
        }
        //Message d'erreur
        else {
            printf("\nLe but du puissance 4 est d'aligner une suite de 4 jetons de même couleur horizontalement, verticalement ou en diagonale. Attention, les jetons tomberont tout en bas de la grille, sauf s'il y a d'autres jetons en dessous.\nEntre q ou d pour déplacer le jeton jusqu'à la colonne voulue, et Espace pour placer le jeton.\nSinon, entre 0 pour arrêter la partie ou r pour relire les règles du jeu:\n");
        }
        afficher(g,pion,arrow);
        printf("\n");
        scanf("%c%c",&continu,&err);
    }
    return arrow;
}

/* 
fonction trouverLigne(Grille g,int colonne)
Consiste à trouver la première case non occupée de la colonne. Si la colonne est pleine, la
fonction retourne -1. 
*/
int trouveLigne(Grille g,int colonne){
    int i,indice;
    i=0;
    indice=-1;
    while ((indice==-1)&&(i<NBLIG)){
        if ((g[i][colonne-1])==VIDE){
            indice=i+1;
        }
        i=i+1;
    }
    return indice;
}

/* 
fonction grillePleine(Grille g)
Teste si toutes les cases de la grille sont occupées ou non.
*/
bool grillePleine(Grille g){
    int l,c;
    bool trouve;
    trouve=true;
    l=0;
    while ((l<NBLIG) && (trouve==true) ){ //Cherche à chaque ligne tant qu'une case n'est pas vide ou que la grille n'a pas été entièrement vérifiée
        c=0;
        while ((c<NBCOL) && (trouve==true)) { //Cherche à chaque colonne tant qu'une case n'est pas vide ou que la grille n'a pas été entièrement vérifiée
            if (g[l][c] == VIDE){ //Verifie si le contenu de la case est vide
            trouve=false;
            }
        c=c+1;
        }
    l=l+1;
    }
    return trouve;
}

/* 
procédure jouer(Grille g, char pion, int *ligne, int *colonne)
permet à un joueur de jouer son pion. La procédure fait appel à choisirColonne, afin que le
joueur indique la colonne dans laquelle il veut jouer ; puis fait appel à trouverLigne pour définir
la case où ajouter le pion.
*/
void jouer(Grille g, char pion, int *ligne, int *colonne){
    int col,lig;
    col=choisirColonne(g, pion,1); //Récupère la colonne demandée par le joueur
    lig=trouveLigne(g, col); //Vérifie à quelle ligne le pion doit être inséré
    while (lig==-1){ //S'assure que la colonne sélectionnée par le joueur n'est pas déjà complète, si elle l'est, le joueur doit rechosiir une colonne
        printf("Tu ne peux pas mettre de jeton dans cette colonne, elle est déjà complète.");
        col=choisirColonne(g, pion,col);
        lig=trouveLigne(g, col);
    }
    g[lig-1][col-1]=pion; //Insère le pion dans la grille
    *colonne=col;
    *ligne=lig;
}

/* 
procédure estVainqueur(Grille g, int ligne, int col)
Indique si le pion situé dans la case repérée par les paramètres ligne et colonne a gagné la partie,
c’est-à-dire s’il y a une ligne, une colonne ou une diagonale formée d’au moins 4 de ses pions (la
ligne et la colonne passées en paramètres correspondent à la case où le joueur vient de jouer,
c’est-à-dire la case à partir de laquelle il faut rechercher 4 pions successifs identiques).
*/
bool estVainqueur(Grille g, int ligne, int col){
    int i,j,comp,indY,indX;
    bool consec;
    consec=true;
    comp=0;
    //Verification HORIZONTALE
    for (i=0;i<NBCOL;i++){
        if (g[ligne-1][i]==g[ligne-1][col-1]){
            comp=comp+1;
        }
        else{
            comp=0;
        }
    }
    if (comp>=4){
        return true;
    }
    else{
        comp=0;
    }
    //Verification VERTICALE
    
    for (i=0;i<ligne;i++){
        if (g[i][col-1]==g[ligne-1][col-1]){
            comp=comp+1;
        }
        else{
            comp=0;
        }
    }
    if (comp>=4){
        return true;
    }
    else{ 
        comp=0;}
    //Verification DIAGONALE (haut-gauche / bas-droite)
    indY=ligne-1;
    indX=col-1;
    while ((indY<NBLIG) && (indX>0)){
        indY=indY+1;
        indX=indX-1;
    }
    while ((indY>=0) && (indX<NBCOL)){
        if (g[indY][indX]==g[ligne-1][col-1]){
            comp=comp+1;
        }
        else{
            comp=0;
        }
        indY=indY-1;
        indX=indX+1;
    }
    if (comp>=4){
        return true;
    }
    else{ 
        comp=0;}
        
    //Verification DIAGONALE (haut-droite / bas-gauche)
    indY=ligne-1;
    indX=col-1;
    while ((indY<NBLIG) && (indX<NBCOL)){
        indY=indY+1;
        indX=indX+1;
    }
    while ((indY>=0) && (indX>=0)){
        if (g[indY][indX]==g[ligne-1][col-1]){
            comp=comp+1;
        }
        else{
            comp=0;
        }
        indY=indY-1;
        indX=indX-1;
    }
    if (comp>=4){
        return true;
    }
    else{ 
        return false;}
}

/* 
procédure finDePartie(char pion, char joueur1[50], char  joueur2[50])
Affiche le résultat d’une partie lorsqu’elle est terminée.
*/
void finDePartie(char pion, char joueur1[50], char  joueur2[50]){
    if (pion=='X'){
        printf("\nFélicitations, %s a remporté la victoire !\n",joueur1);
    }
    else if (pion=='O'){
        printf("\nFélicitations, %s a remporté la victoire !\n",joueur2);
    }
    else{
        printf("\nIl semblerait que tous les problèmes n'ont pas de solutions...\nEgalité !\n");
    }
}

/* 
fonction rejouer()
Demande au joeuur s'il souhaite continuer et retourne vrai si le joueur souhaite continuer de jouer, ou faux s'il souhaite s'arrêter
*/
bool rejouer(){
    int answer;
    printf("Rejouer ?\nAppuie sur 1 pour relancer le jeu ou 0 pour quitter le jeu\n");
    scanf("%d",&answer);
    while ((answer!=1)&&(answer!=0)){
        printf("Rejouer ?\nAppuie sur 1 pour relancer le jeu ou 0 pour quitter le jeu\n");
        scanf("%d",&answer);
    }
    if (answer==0){
        return false;
    }
    else {
        return true;
    }
}

int main(){
    char vainqueur; //vainqueur est le caractère du pion vainqueur qui sera initialement définie comme inconnu
    char err;
    char joueur1[50];
    char joueur2[50];
    bool partie; //Booléen qui fait boucler le jeu tant que le joueur souhaite rejouer
    partie=true;
    int colonne, ligne;
    Grille g; //la grille du jeu de puissance 4
    while (partie==true){
        initGrille(g); //A chaque nouvelle partie, on initialise la grille (on la remplit d'espace)
        vainqueur = INCONNU;
        printf("Bienvenue dans une partie de Puissance 4\n");
        afficher(g,VIDE,COLONNE_DEBUT);
        //On demande le noms des deux joueurs
        printf("\nEntre le nom du JOUEUR 1 qui jouera -> X\n");
        scanf("%s",joueur1);
        printf("\nEntre le nom du JOUEUR 2 qui jouera -> O\n");
        scanf("%s",joueur2);
        scanf("%c",&err); //Récupérer le dernier caractère (le retour chariot) permet de s'assurer que ce caractère ne sera pas mal interpréter lors du prochain scanf
        printf("\nLe but du puissance 4 est d'aligner une suite de 4 jetons de même couleur horizontalement, verticalement ou en diagonale. Attention, les jetons tomberont tout en bas de la grille, sauf s'il y a d'autres jetons en dessous.\nEntre q ou d pour déplacer le jeton jusqu'à la colonne voulue, et Espace pour placer le jeton.\nSinon, entre 0 pour arrêter la partie ou r pour relire les règles du jeu:\n");
        while ((vainqueur==INCONNU)&&(grillePleine(g)==false)){ //A chaque tour il vérifie si la grille n'est pas encore remplie et si le vainqueur est connu. Si l'une des deux conditions n'est pas remplies, on termine la partie
            printf("\n%s(%c) à toi de jouer\n",joueur1,'X'); //Annonce quel joueur doit jouer
            jouer(g,PION_A,&ligne,&colonne);
            afficher(g, PION_B, COLONNE_DEBUT);
            if (estVainqueur(g,ligne,colonne)){//Vrifie si le premier joueur est vainqueur
                vainqueur = PION_A;
            }
            else if (!grillePleine(g)){ //si le premeir joeuur n'est pas vainqueur et que la grille n'est toujours pas remplie, on laisse le second joueur jouer
                printf("\n\n%s(%c) à toi de jouer\n",joueur2,'O');
                jouer(g,PION_B,&ligne,&colonne);
                afficher(g,PION_A,COLONNE_DEBUT);
                if (estVainqueur(g,ligne,colonne)){//Vérifie si le second joueur est vainqueur
                    vainqueur = PION_B;
                }
            }
        }
        finDePartie(vainqueur,joueur1,joueur2); //Annonce les résultats
        partie=rejouer(); //Demande si le joueur veut rejouer ou non
    }
    quitter(); //Quitte le jeu si le joueur refuse de continuer
}
