# Exercice à réaliser pour le TP0

Ce document contient les instructions pour réaliser un exercice pour vous familiariser avec les outils que vous venez d'installer, tels que VS Code, Git et GitHub.

À la fin de cet exercice, vous serez capables de cloner un répertoire GitHub, modifier et exécuter un fichier en Python, et mettre à jour le répertoire GitHub avec vos modifications :smiley: 

## :eight_pointed_black_star: PARTIE 1 : Faire une copie locale d'un répertoire GitHub

Pour utiliser un répertoire situé sur GitHub, il est possible de faire une copie locale du répertoire sur notre ordinateur. On appelle cette copie un `clone`. Une fois cette copie effectuée, il est possible d'effectuer des modifications aux fichiers (par exemple, ajouter du code) sur notre copie locale. Une fois les modifications effectuées, il est ensuite possible de 'pousser' ces changements vers le répertoire situé sur GitHub. De cette façon, tout le monde qui a accès au répertoire GitHub pourra voir la nouvelle version du répertoire avec vos changements. 

Comme premier exercice, vous allez créer un `clone` du répertoire du TP0 sur votre ordinateur. Les étapes à suivre sont les suivantes : 

☑️ **Étape 1.1 :** Si ce n'est pas déjà fait, créer un dossier `INF1007` sur votre ordinateur pour y ajouter le TP0. 

> [!Tip]
> Dans votre dossier `INF1007`, vous pourrez y placer tous les TP et les projets du cours.
   
☑️ **Étape 1.2 :** Ouvrir VS Code
   
☑️ **Étape 1.3 :** Ouvrir un terminal dans VS Code (voir la capture d'écran suivante)

<img width="2809" height="1833" alt="Image" src="https://github.com/user-attachments/assets/420b71c7-f8e8-4e89-9413-9c4cb7c97557" />
<br/>
<br/>

☑️ **Étape 1.4 :** Assurez-vous que votre terminal se retrouve dans le dossier `INF1007`. Si ce n'est pas le cas, utilisez la commande `cd` ("change directory") pour changer le chemin dans votre terminal, comme dans la capture d'écran ci-dessous.

```
cd chemin/vers/votre/dossier/INF1007
```

<img width="3593" height="1205" alt="Image" src="https://github.com/user-attachments/assets/464d5978-c600-45d0-ab49-4c3d8da64565"/>
<br/>
<br/>

☑️ **Étape 1.5 :** Sur la page web du répertoire du TP0 sur GitHub, appuyer sur le bouton suivant pour copier le lien du répertoire (vous pourrez ensuite faire CTRL+V pour le coller). 

<img width="4042" alt="Image" src="https://github.com/user-attachments/assets/0c0fe95d-77e2-4a50-82c4-274310956f62" /> 
<br/>
<br/>

☑️ **Étape 1.6 :** Maintenant, utiliser la commande `git clone`, suivie du lien du répertoire que vous venez de copier. Appuyer sur la touche "Entrée" pour exécuter la commande. 

```
git clone le/lien/du/répertoire/github
```

<img width="3657" height="1205" alt="Image" src="https://github.com/user-attachments/assets/34276d8d-b862-4eb8-b652-87aec3875bbe" />
<br/>
<br/>

Maintenant que vous avez fait le `git clone`, les fichiers du TP0 devraient apparaître dans le dossier que vous avez créé sur votre ordinateur. Vérifiez que c'est le cas en ouvrant le dossier dans VS Code, en suivant la procédure de la capture d'écran ci-dessous (vous pouvez aussi cliquer sur : `File` > `Open Folder`). 

<img width="2823" height="1833" alt="Image" src="https://github.com/user-attachments/assets/64336a6c-177f-4112-a107-15ce08926bde" />
<br/>
<br/>

Une fois le dossier ouvert dans VS Code, vous devriez voir les fichiers du TP0 sur l'onglet de gauche. Cliquez sur le fichier Python `TP0.py` pour l'ouvrir. 

<img width="2809" height="1145" alt="Image" src="https://github.com/user-attachments/assets/a7f63b57-e618-442c-9e97-e1ae10f312a4" />
<br/>
<br/>

## :eight_pointed_black_star: PARTIE 2 : Calcul de l'aire d'un cercle

Maintenant que vous avez ouvert le fichier `TP0.py`, nous allons écrire quelques lignes de code à l'intérieur, pour se pratiquer à exécuter du code dans VS Code. 

Comme exercice, on vous propose de calculer l'aire d'un cercle à partir d'un rayon donné en entrée par l'utilisateur, comme dans l'exemple suivant : 

https://github.com/user-attachments/assets/4b02953f-163a-4be1-aa55-a7818d0e0a11 

Voici quelques étapes pour vous guider : 

☑️ **Étape 2.1 :** En utilisant la fonction `input()`, ajouter une ligne de code qui, lorsque exécutée, permettra de demander à l'utilisateur d'entrer une valeur pour le rayon dans le terminal. 

> [!Tip]
> La fonction `input()` est une fonction déjà intégrée dans Python qui permet de demander à l'utilisateur d'entrer une valeur dans le terminal. Vous pouvez suivre [cet exemple](https://www.w3schools.com/python/ref_func_input.asp) pour vous aider.

☑️ **Étape 2.2 :** Ensuite, dans une autre ligne de code, créer une variable nommée `aire`, qui sera égale à l'équation de l'aire d'un cercle. Pour le rayon, utilisez la valeur entrée par l'utilisateur dans l'étape précédente. 

> [!Tip]
> Vous pouvez consulter [cette ressource](https://www.w3schools.com/python/python_variables.asp) pour la définition d'une variable en Python, et [celui-ci](https://www.w3schools.com/python/python_operators.asp) pour consulter une liste d'opérateurs arithmétiques. 

☑️ **Étape 2.3 :** Finalement, en utilisant la fonction `print()`, ajouter une autre ligne de code pour afficher l'aire du cercle dans le terminal. 
   
> [!Tip]
> La fonction `print()` est une autre fonction intégrée dans Python, qui permet d'afficher un message en sortie dans le terminal. Vous pouvez utiliser [cet exemple](https://www.w3schools.com/python/ref_func_print.asp) pour vous guider.


## :eight_pointed_black_star: PARTIE 3 : Mettre à jour le répertoire sur GitHub avec vos changements  

Maintenant que vous avez effectué des modifications au fichier `TP0.py`, il est maintenant temps de mettre à jour le répertoire sur GitHub en y ajoutant votre code qui calcule l'aire d'un cercle. 

> [!Important]
> Avant de poursuivre, assurez-vous d'avoir sauvegardé votre fichier `TP0.py` avec vos changements (par exemple, avec `File` > `Save`, ou bien `CTRL+S`). 
<br/>

☑️ **Étape 3.1 :** Nous allons d'abord utiliser la commande `git status` pour s'assurer que git reconnaît bien qu'il y a eu des changements au répertoire depuis le `clone`. Avant d'exécuter la commande, assurez-vous que le chemin dans votre terminal se retrouve dans le fichier `2025A-TP0`. Par exemple, si vous êtes dans le dossier `INF1007` et que votre dossier `2025A-TP0` est à l'intérieur de `INF1007`, vous pouvez simplement faire:
```
cd 2025A-TP0
```

Une fois dans le bon chemin, entrez la commande `git status` dans votre terminal de VS Code :
```
git status
```

Ici, on voit que `Git` a identifié des modifications au fichier `TP0.py` : 

<img width="780" height="219" alt="Image" src="https://github.com/user-attachments/assets/c9951436-2c49-42c0-acd5-4ac01e418b34" />
<br/>
<br/>

☑️ **Étape 3.2 :** Maintenant, nous allons utiliser la commande `git add` pour ajouter le fichier TP0.py. Cette commande indique à `Git` que vous souhaitez inclure les modifications d'un certain fichier lorsque vous utiliserez la prochaine commande (c'est-à-dire, `git commit`).

```
git add TP0.py
```

> [!Note]
> Vous pourriez aussi utiliser la commande suivante au lieu :  
> ```
> git add .
> ```
> Le `.` va ajouter tout le contenu du répertoire. Cela évite d'avoir à faire un `git add` pour chaque fichier que vous avez modifié.

> [!Tip]
> Pour vérifier que les fichiers ont bel et bien été ajoutés, vous pouvez réutiliser `git status`. Les fichiers ajoutés vont apparaître en vert comme dans la capture d'écran ci-dessous.
<br/>

<img width="782" height="326" alt="Image" src="https://github.com/user-attachments/assets/f020408d-7461-49e3-a36d-fa072abcd29d" />
<br/>
<br/>

☑️ **Étape 3.3 :** Il est maintenant temps d'utiliser la commande `git commit`, qui permet de créer une "version" de notre travail qui sera répertoriée par `Git`. En d'autres mots, à chaque fois que vous faites un `git commit`, le contenu des fichiers que vous avez ajoutés précedemment avec `git add` est sauvegardé dans l'historique du projet. Vous pourrez ensuite consulter toutes ces versions en naviguant parmi les anciens commits.  

Pour effectuer un `commit`, on utilise la commande `git commit`, suivie de l'option `-m`, qui permet d'ajouter un message personnalisé. Généralement, on ajoute un message qui décrit brièvement les modifications apportées (par exemple : "ajout de l'aire d'un cercle").

```
git commit -m "entrer ici un message descriptif" 
```

> [!Tip]
> Vous pouvez aussi vérifier le `git status`. 
<br/>

<img width="782" height="335" alt="Image" src="https://github.com/user-attachments/assets/44bd43b2-f52e-4a79-9b47-b6f90824546e" />
<br/>
<br/>

☑️ **Étape 3.4 :** Nous sommes rendus à la dernière étape du TP0 : la commande `git push` ! 🎉
Cette commande permet de publier le commit que vous venez de faire dans le répertoire local vers GitHub.

Autrement dit, tant que vous ne faites pas de `git push`, vos changements sont enregistrés uniquement localement sur votre ordinateur, mais ne sont pas visibles sur GitHub.

```
git push
```

Pour votre information, lorsqu'on fait git push, le commit devient visible sur GitHub, comme dans l'exemple ci-dessous :

<br/>
<img width="3822" height="1480" alt="fig13" src="https://github.com/user-attachments/assets/a06823c3-9f9a-413f-a9ed-46fa16f00cb9" />
<br/>

Vous avez maintenant terminé le TP0 ! 🎉 
